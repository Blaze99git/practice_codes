def pretty_print(state):
    data = state["data"]
    results = state["results"]

    print("\n" + "="*50)
    print("📊 ASSET HEALTH REPORT")
    print("="*50)

    print(f"Asset ID: {data.get('asset_id', 'N/A')}\n")

    # Preanalysis
    pre = results.get("preanalysis", {})
    print("🔍 Preanalysis")
    print(f"  • Anomaly Detected : {'YES' if pre.get('anomaly') else 'NO'}")
    print(f"  • Confidence       : {round(pre.get('confidence', 0)*100)}%")
    print(f"  • Trend Score      : {round(pre.get('score', 0), 2)}\n")

    # Diagnostics
    diag = results.get("diagnostics", {})
    if diag:
        print("🧠 Diagnostics")
        print(f"  • Severity         : {diag.get('severity')}")
        print(f"  • Remaining Life   : {diag.get('remaining_life')} hours")
        print(f"  • Degradation Index: {diag.get('degradation_index')}\n")

    # Action
    action = results.get("action", {})
    if action:
        print("🛠️ Action")
        print(f"  • Action           : {action.get('action')}")
        print(f"  • Priority         : {action.get('priority')}\n")

    print("✅ Status: Processing Complete")
    print("="*50)
