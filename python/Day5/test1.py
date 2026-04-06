import os
import re
import json
from typing import List
import requests
from openai import OpenAI

# ==========================================================
# CONFIGURATION
# ==========================================================

print("\n================= CONFIGURATION =================")

MCP_SERVER_URL = "http://52.172.33.24:45345/mcp"
MCP_API_KEY = "mcpcheck.A1zdjCXKmizep3Kz63EGPy2Qk8Q3Y8GNyiV21rOvdLQ="

ANYTHINGLLM_BASE = "http://52.172.33.24:3001"
WORKSPACE_SLUG = "my-workspace"
ANYTHINGLLM_API_KEY = "ZD0PZKZ-32AMK6Y-QWY7JEP-Q3ZAJQP"

print("MCP URL:", MCP_SERVER_URL)
print("AnythingLLM URL:", ANYTHINGLLM_BASE)
print("Workspace:", WORKSPACE_SLUG)

BASE_HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {MCP_API_KEY}",
    "Accept": "application/json",
}

ANY_HEADERS = {
    "Authorization": f"Bearer {ANYTHINGLLM_API_KEY}",
    "Content-Type": "application/json"
}

# Alert Context
machine_name = "001_Drying_Machine"
alert_type = "Heater_Temperature High Alert"
alertdescription = "heater temperature causing the hot air temperature to increase"

alertdetail = (
    f"alert type is {alert_type} and alert description is {alertdescription} "
    f"for machine_name {machine_name}"
)

# ==========================================================
# STEP 1: CONNECT TO MCP
# ==========================================================

print("\n================= STEP 1: MCP INITIALIZATION =================")

init_payload = {
    "jsonrpc": "2.0",
    "id": 0,
    "method": "initialize",
    "params": {
        "protocolVersion": "2025-06-18",
        "clientInfo": {"name": "mcp-client", "version": "1.0"},
        "capabilities": {}
    },
}

try:
    print("Sending MCP initialize request...")
    print(json.dumps(init_payload, indent=2))

    init_response = requests.post(
        MCP_SERVER_URL,
        json=init_payload,
        headers=BASE_HEADERS,
        timeout=30
    )

    print("MCP Status Code:", init_response.status_code)
    print("MCP Raw Response:", init_response.text)

    init_response.raise_for_status()

    session_id = init_response.headers.get("Mcp-Session-Id")

    if not session_id:
        raise RuntimeError("No MCP session id received")

    print("✅ MCP Session ID:", session_id)

except Exception as e:
    print("❌ MCP Initialization Failed:", e)
    raise SystemExit(1)

headers_with_session = BASE_HEADERS.copy()
headers_with_session["Mcp-Session-Id"] = session_id

# ==========================================================
# STEP 2: LIST MCP TOOLS
# ==========================================================

print("\n================= STEP 2: LIST TOOLS =================")

tools_payload = {
    "jsonrpc": "2.0",
    "id": 2,
    "method": "tools/list",
    "params": {}
}

try:
    print("Requesting tool list...")
    tools_response = requests.post(
        MCP_SERVER_URL,
        json=tools_payload,
        headers=headers_with_session,
        timeout=30
    )

    print("Tool List Status Code:", tools_response.status_code)
    print("Tool List Raw Response:", tools_response.text)

    tools_response.raise_for_status()

    tools_catalog = tools_response.json()
    tools_list = tools_catalog.get("result", {}).get("tools", [])

    if not tools_list:
        raise RuntimeError("No tools returned by MCP")

    print("✅ Tools Retrieved Successfully")

except Exception as e:
    print("❌ Tool List Failed:", e)
    raise SystemExit(1)

tool_map = {
    t.get("name", "").strip(): (t.get("description", "") or "").strip()
    for t in tools_list if t.get("name")
}

tools: List[str] = list(tool_map.keys())
descriptions: List[str] = list(tool_map.values())

print("Available Tools:", tools)

# ==========================================================
# STEP 3: OLLAMA RANKING
# ==========================================================

print("\n================= STEP 3: OLLAMA RANKING =================")

together = ""
for index, (name, description) in enumerate(zip(tools, descriptions), start=1):
    together += f"# Tool {index}: {name}\n\n{description}\n\n"

judge = (
    f"Rank best tool for alert:\n{alertdetail}\n\n"
    'Respond JSON: {"results": ["1","2","3"]}\n\n'
    f"{together}"
)

try:
    print("Sending ranking request to Ollama...")
    ollama = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

    response = ollama.chat.completions.create(
        model="llama3.2:latest",
        messages=[{"role": "user", "content": judge}],
        timeout=60
    )

    content = response.choices[0].message.content.strip()
    print("Ollama Response:", content)

except Exception as e:
    print("❌ Ollama Failed:", e)
    raise SystemExit(1)

def parse_results(text):
    try:
        data = json.loads(text)
    except:
        match = re.search(r"\{.*\}", text, re.S)
        if not match:
            return list(range(len(tools)))
        data = json.loads(match.group(0))

    raw = data.get("results", [])
    indices = []

    for r in raw:
        try:
            idx = int(r) - 1
            if 0 <= idx < len(tools):
                indices.append(idx)
        except:
            continue

    return indices if indices else list(range(len(tools)))

ranks = parse_results(content)

print("Ranking Order:", ranks)

# ==========================================================
# STEP 4: CALL TOP TOOL
# ==========================================================

print("\n================= STEP 4: CALL TOP TOOL =================")

best_tool = tools[ranks[0]]
print("Top Tool Selected:", best_tool)

call_payload = {
    "jsonrpc": "2.0",
    "id": 999,
    "method": "tools/call",
    "params": {
        "name": best_tool,
        "arguments": {
            "machine_name": machine_name,
            "alert_type": alert_type
        }
    }
}

try:
    print("Calling MCP tool with payload:")
    print(json.dumps(call_payload, indent=2))

    tool_response = requests.post(
        MCP_SERVER_URL,
        json=call_payload,
        headers=headers_with_session,
        timeout=60
    )

    print("Tool Call Status Code:", tool_response.status_code)
    print("Tool Call Raw Response:", tool_response.text)

    tool_response.raise_for_status()

    tool_data = tool_response.json()
    hb_rows = tool_data.get("result", {}).get("content", [])

    if not hb_rows:
        raise RuntimeError("No data returned from tool")

    print("✅ Tool Data Retrieved")

except Exception as e:
    print("❌ Tool Call Failed:", e)
    raise SystemExit(1)

# ==========================================================
# STEP 5: ANYTHINGLLM
# ==========================================================

print("\n================= STEP 5: ANYTHINGLLM =================")

prompt = f"Diagnostic data:\n{json.dumps(hb_rows, indent=2)}"

try:
    print("Creating AnythingLLM thread...")

    thread_response = requests.post(
        f"{ANYTHINGLLM_BASE}/api/v1/workspace/{WORKSPACE_SLUG}/thread/new",
        headers=ANY_HEADERS,
        json={"name": "debug-session"},
        timeout=30
    )

    print("Thread Status Code:", thread_response.status_code)
    print("Thread Response:", thread_response.text)

    thread_response.raise_for_status()

    thread_slug = thread_response.json()["thread"]["slug"]

    print("Sending prompt to AnythingLLM...")

    chat_response = requests.post(
        f"{ANYTHINGLLM_BASE}/api/v1/workspace/{WORKSPACE_SLUG}/thread/{thread_slug}/chat",
        headers=ANY_HEADERS,
        json={"message": prompt, "mode": "query"},
        timeout=300
    )

    print("Chat Status Code:", chat_response.status_code)
    print("Chat Raw Response:", chat_response.text)

    chat_response.raise_for_status()

    ai_response = chat_response.json().get("textResponse", "")

    print("\n✅ FINAL AI RESPONSE:\n")
    print(ai_response)

except Exception as e:
    print("❌ AnythingLLM Failed:", e)
    raise SystemExit(1)

print("\n================= FLOW COMPLETED SUCCESSFULLY =================")