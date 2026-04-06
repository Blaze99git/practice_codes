import json
from router.llm_router import decide_next
from crew.agents import preanalysis, diagnostics, action


def run_pipeline():
    with open("data/telemetry_sample.json") as f:
        asset_data = json.load(f)

    state = {
        "asset_data": asset_data,
        "steps_done": []
    }

    print("\n🚀 Starting LLM Agent Pipeline\n")

    while True:
        step = decide_next(state)
        print(f"\n🔀 LLM Routing → {step}")

        if step == "stop":
            print("\n✅ Pipeline finished safely")
            break

        if step in state["steps_done"]:
            print("🛑 Loop detected. Exiting.")
            break

        state["steps_done"].append(step)

        # ---------- PREANALYSIS ----------
        if step == "preanalysis":
            result = preanalysis(asset_data)
            state["preanalysis"] = result

            print("📊 Preanalysis Output")
            print(json.dumps(result, indent=2))

        # ---------- DIAGNOSTICS ----------
        elif step == "diagnostics":
            result = diagnostics(asset_data)
            state["diagnostics"] = result

            print("📊 Diagnostics Output")
            print(json.dumps(result, indent=2))

        # ---------- ACTION ----------
        elif step == "action":
            result = action(
                asset_data,
                state.get("diagnostics"),
                state.get("preanalysis")
            )

            state["action"] = result

            print("\n🛠 FINAL ACTION")
            print("=" * 50)
            print(json.dumps(result, indent=2))
            print("=" * 50)

            break


if __name__ == "__main__":
    run_pipeline()
