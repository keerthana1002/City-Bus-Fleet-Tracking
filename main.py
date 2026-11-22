"""
Case 28: City Bus Fleet Tracking (600 Buses) - Master Runner for VS Code
Student: Keerthana M | Roll Number: ENG24CS0096 | Class/Section: 3B
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "src"))
from arrival_estimator import ArrivalTimeEstimator, BusTelemetry
from fleet_simulator import run_600_bus_simulation
from roster_manager import generate_driver_roster


def main():
    print("=" * 68)
    print("  CASE 28: CITY BUS FLEET TRACKING (600 BUSES)")
    print("  Student: Keerthana M | Roll No: ENG24CS0096 | Section: 3B")
    print("  Process Model: Spiral | Agile: Kanban | AI Tool: ChatGPT")
    print("=" * 68)

    est = ArrivalTimeEstimator()
    print("\n[1] Arrival Time Estimator Prototype:")
    print("  Surface GPS Active :", est.estimate_eta(BusTelemetry("BUS-028", "R-14", 4.2, 38.0, True, 0.0, False, 1.1)))
    print("  Inside Tunnel Drop :", est.estimate_eta(BusTelemetry("BUS-028", "R-14", 3.5, 0.0, False, 90.0, True, 1.15)))
    print("  Tunnel Exit GPS    :", est.estimate_eta(BusTelemetry("BUS-028", "R-14", 2.1, 34.0, True, 0.0, False, 1.0)))

    print("\n[2] 600-Bus Fleet Live Simulation:")
    sim = run_600_bus_simulation()
    print(f"  Tracked: {sim['total_buses_tracked']} | Live GPS: {sim['buses_live_gps']} | Tunnel Dead-Reckoning: {sim['buses_in_tunnel_dead_reckoning']} | Avg ETA: {sim['fleet_average_eta_minutes']} mins")

    print("\n[3] 600-Bus Driver Duty Roster:")
    roster = generate_driver_roster(600)
    print(f"  Total Duty Assignments: {len(roster)} (Sample: {roster[0]})")


if __name__ == "__main__":
    main()
