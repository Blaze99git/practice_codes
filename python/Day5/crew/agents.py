import numpy as np


def preanalysis(data):
    t = np.array(data["temperature"])
    v = np.array(data["vibration"])

    slope_t = np.polyfit(range(len(t)), t, 1)[0]
    slope_v = np.polyfit(range(len(v)), v, 1)[0]

    score = abs(slope_t) + abs(slope_v)
    confidence = min(0.95, 0.5 + score / 10)

    return {
        "anomaly": bool(score > 4),
        "confidence": float(round(confidence, 2)),
        "score": float(round(score, 2))
    }


def diagnostics(data):
    temp = max(data["temperature"])
    vib = max(data["vibration"])
    curr = max(data["current"])

    degradation = (
        0.5 * (temp / 120) +
        0.3 * (vib / 8) +
        0.2 * (curr / 20)
    )

    if degradation >= 0.85:
        severity = "HIGH"
    elif degradation >= 0.65:
        severity = "MEDIUM"
    elif degradation >= 0.40:
        severity = "LOW"
    else:
        severity = "NORMAL"

    return {
        "severity": severity,
        "remaining_life": int((1 - degradation) * 500),
        "degradation_index": round(degradation, 2)
    }


def action(data, diagnostics=None, preanalysis=None):

    if diagnostics:
        sev = diagnostics["severity"]

        if sev == "HIGH":
            return {
                "action": "CREATE_WORK_ORDER",
                "priority": "P1",
                "reason": "Critical degradation detected"
            }

        if sev == "MEDIUM":
            return {
                "action": "MONITOR",
                "priority": "P2",
                "reason": "Moderate degradation observed"
            }

        if sev == "LOW":
            return {
                "action": "LOG_ANOMALY",
                "priority": "P3",
                "reason": "Mild anomaly detected"
            }

    # fallback
    return {
        "action": "NO_ACTION",
        "priority": "P4",
        "reason": "System operating normally"
    }

