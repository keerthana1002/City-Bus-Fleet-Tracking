"""
Lab L4.2: 8 Automated Unit Tests for Arrival Time Estimator (Case 28: 600 Buses)
"""
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from arrival_estimator import ArrivalTimeEstimator, BusTelemetry
from fleet_simulator import run_600_bus_simulation
from roster_manager import generate_driver_roster


class TestArrivalTimeEstimator(unittest.TestCase):
    def test_01_live_gps_initial_eta(self):
        est = ArrivalTimeEstimator(alpha=0.5)
        res = est.estimate_eta(BusTelemetry("BUS-001", "R-01", 6.0, 30.0, True))
        self.assertEqual(res["mode"], "LIVE_GPS_EMA")
        self.assertEqual(res["eta_minutes"], 12.0)

    def test_02_ema_speed_smoothing_across_updates(self):
        est = ArrivalTimeEstimator(alpha=0.5)
        est.estimate_eta(BusTelemetry("BUS-002", "R-01", 5.0, 40.0, True))
        res = est.estimate_eta(BusTelemetry("BUS-002", "R-01", 3.0, 20.0, True))
        self.assertEqual(res["effective_speed_kmh"], 30.0)
        self.assertEqual(res["eta_minutes"], 6.0)

    def test_03_tunnel_dead_reckoning_fallback(self):
        est = ArrivalTimeEstimator(alpha=1.0)
        est.update_smoothed_speed("BUS-028", 36.0)
        res = est.estimate_eta(BusTelemetry("BUS-028", "R-05", 4.6, 0.0, False, time_in_tunnel_sec=100.0, in_tunnel=True))
        self.assertEqual(res["mode"], "TUNNEL_DEAD_RECKONING")
        self.assertEqual(res["remaining_distance_km"], 3.6)
        self.assertEqual(res["eta_minutes"], 6.0)

    def test_04_tunnel_distance_clamp_at_zero(self):
        est = ArrivalTimeEstimator(alpha=1.0)
        est.update_smoothed_speed("BUS-028", 36.0)
        res = est.estimate_eta(BusTelemetry("BUS-028", "R-05", 0.5, 0.0, False, time_in_tunnel_sec=200.0, in_tunnel=True))
        self.assertEqual(res["remaining_distance_km"], 0.0)
        self.assertEqual(res["eta_seconds"], 0)

    def test_05_arrived_boundary_state(self):
        est = ArrivalTimeEstimator()
        res = est.estimate_eta(BusTelemetry("BUS-100", "R-10", 0.0, 25.0, True))
        self.assertEqual(res["mode"], "ARRIVED")
        self.assertEqual(res["eta_minutes"], 0.0)

    def test_06_traffic_congestion_and_min_speed_floor(self):
        est = ArrivalTimeEstimator(alpha=1.0, min_speed_kmh=5.0)
        res = est.estimate_eta(BusTelemetry("BUS-200", "R-12", 5.0, 10.0, True, traffic_factor=4.0))
        self.assertEqual(res["effective_speed_kmh"], 5.0)
        self.assertEqual(res["eta_minutes"], 60.0)

    def test_07_invalid_negative_and_empty_inputs_raise_value_error(self):
        est = ArrivalTimeEstimator()
        with self.assertRaises(ValueError):
            est.estimate_eta(BusTelemetry("", "R-01", 3.0, 25.0, True))
        with self.assertRaises(ValueError):
            est.estimate_eta(BusTelemetry("BUS-001", "R-01", -1.0, 25.0, True))
        with self.assertRaises(ValueError):
            est.estimate_eta(BusTelemetry("BUS-001", "R-01", 3.0, 25.0, True, traffic_factor=0.0))

    def test_08_600_bus_fleet_and_roster_integration(self):
        sim = run_600_bus_simulation()
        self.assertEqual(sim["total_buses_tracked"], 600)
        self.assertEqual(sim["buses_in_tunnel_dead_reckoning"], 75)
        roster = generate_driver_roster(600)
        self.assertEqual(len(roster), 1320)


if __name__ == "__main__":
    unittest.main()
