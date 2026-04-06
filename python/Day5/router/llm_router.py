import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def is_critical(data):
    return (
        max(data["temperature"]) > 120 or
        max(data["vibration"]) > 9 or
        max(data["current"]) > 20
    )


def decide_next(state):
    data = state["asset_data"]

    # ---------------------------
    # 1️⃣ HARD SAFETY OVERRIDE
    # ---------------------------
    if is_critical(data):
        return "action"

    # ---------------------------
    # 2️⃣ DIAGNOSTICS DECISION
    # ---------------------------
    if "diagnostics" in state:
        # Diagnostics already done → must act
        return "action"

    # ---------------------------
    # 3️⃣ PREANALYSIS DECISION
    # ---------------------------
    if "preanalysis" in state:
        return "diagnostics"

    # ---------------------------
    # 4️⃣ LLM ONLY FOR INITIAL ROUTING
    # ---------------------------
    prompt = f"""
You are an industrial AI router.

Rules:
- If anomaly likely → diagnostics
- If system looks healthy → stop
- NEVER repeat a step

Telemetry:
{json.dumps(data, indent=2)}

Return ONLY:
preanalysis | diagnostics | action | stop
"""

    res = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1
    )

    decision = res.choices[0].message.content.strip().lower()

    if decision in state.get("steps_done", []):
        return "stop"

    return decision
