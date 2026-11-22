"""
600-Bus Fleet Telemetry Simulator (with Tunnel GPS Dropouts)
"""
import os
import sys
import random

sys.path.insert(0, os.path.dirname(__file__))
from arrival_estimator import ArrivalTimeEstimator, BusTelemetry


def run_600_bus_simulation(seed: int = 42) -> dict:
    random.seed(seed)
    estimator = ArrivalTimeEstimator()
    total_buses = 600
    tunnel_buses = 0
    results = []

    for i in range(1, total_buses + 1):
        bus_id = f"BUS-{i:03d}"
        route_id = f"R-{(i % 25) + 1:02d}"
        base_speed = random.uniform(22.0, 48.0)
        estimator.update_smoothed_speed(bus_id, base_speed)

        in_tunnel = (i % 8 == 0)
        if in_tunnel:
            tunnel_buses += 1

        telemetry = BusTelemetry(
            bus_id=bus_id,
            route_id=route_id,
            distance_to_stop_km=round(random.uniform(0.5, 12.0), 2),
            current_speed_kmh=0.0 if in_tunnel else round(random.uniform(18.0, 50.0), 1),
            gps_signal_active=not in_tunnel,
            in_tunnel=in_tunnel,
            time_in_tunnel_sec=random.uniform(20.0, 140.0) if in_tunnel else 0.0,
            traffic_factor=round(random.uniform(0.9, 1.4), 2),
        )
        results.append(estimator.estimate_eta(telemetry))

    avg_eta = round(sum(r["eta_minutes"] for r in results) / len(results), 2)
    return {
        "total_buses_tracked": total_buses,
        "buses_in_tunnel_dead_reckoning": tunnel_buses,
        "buses_live_gps": total_buses - tunnel_buses,
        "fleet_average_eta_minutes": avg_eta,
        "sample_outputs": results[:5],
    }


if __name__ == "__main__":
    summary = run_600_bus_simulation()
    print("600-Bus Fleet Simulation Summary:")
    for k, v in summary.items():
        print(f"  {k}: {v}")
