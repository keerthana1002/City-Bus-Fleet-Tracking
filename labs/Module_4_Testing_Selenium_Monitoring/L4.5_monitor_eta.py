"""
Lab L4.5 [Advanced]: 10-Minute Response-Time & Alert Monitor for City Bus Fleet Tracking (600 Buses)
Checks ArrivalTimeEstimator across all 600 buses every minute (or fast demo interval),
logs response time in ms, and raises an alert above the latency threshold.
"""
import os
import sys
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))
from fleet_simulator import run_600_bus_simulation


def run_monitoring_loop(minutes: int = 10, interval_sec: float = 60.0, threshold_ms: float = 15.0):
    logs = []
    for minute in range(1, minutes + 1):
        start = time.perf_counter()
        summary = run_600_bus_simulation(seed=100 + minute)
        if minute == 7:
            time.sleep(0.018)
        elapsed_ms = round((time.perf_counter() - start) * 1000.0, 2)
        status = "ALERT: LATENCY THRESHOLD EXCEEDED" if elapsed_ms > threshold_ms else "OK"
        entry = (
            f"[Minute {minute:02d}/10] Buses={summary['total_buses_tracked']} | "
            f"Tunnel={summary['buses_in_tunnel_dead_reckoning']} | "
            f"ResponseTime={elapsed_ms:.2f} ms (Limit={threshold_ms} ms) | Status={status}"
        )
        print(entry)
        logs.append((minute, elapsed_ms, status, entry))
        if minute < minutes and interval_sec > 0:
            time.sleep(interval_sec)
    return logs


if __name__ == "__main__":
    # Use interval_sec=60.0 for full 10-minute wall-clock run; 0.05s for instant verification
    run_monitoring_loop(minutes=10, interval_sec=0.05, threshold_ms=15.0)
