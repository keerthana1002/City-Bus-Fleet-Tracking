"""
Case 28: City Bus Fleet Tracking (600 Buses)
Prototype Module: Arrival Time Estimator (with Tunnel Dead-Reckoning)
Student: Keerthana M | Roll No: ENG24CS0096 | Class/Section: 3B
"""

from dataclasses import dataclass

MODE_LIVE_GPS = "LIVE_GPS_EMA"
MODE_TUNNEL = "TUNNEL_DEAD_RECKONING"
MODE_ARRIVED = "ARRIVED"


@dataclass
class BusTelemetry:
    bus_id: str
    route_id: str
    distance_to_stop_km: float
    current_speed_kmh: float
    gps_signal_active: bool
    time_in_tunnel_sec: float = 0.0
    in_tunnel: bool = False
    traffic_factor: float = 1.0


class ArrivalTimeEstimator:
    """
    Estimates stop-level arrival time (ETA) across a 600-bus fleet,
    automatically falling back to dead-reckoning when GPS signals drop in tunnels.
    """

    def __init__(self, alpha: float = 0.4, default_tunnel_speed_kmh: float = 32.0, min_speed_kmh: float = 5.0):
        if not (0.0 < alpha <= 1.0):
            raise ValueError("alpha must be in (0.0, 1.0]")
        if default_tunnel_speed_kmh <= 0 or min_speed_kmh <= 0:
            raise ValueError("Speed thresholds must be positive")
        self.alpha = alpha
        self.default_tunnel_speed_kmh = default_tunnel_speed_kmh
        self.min_speed_kmh = min_speed_kmh
        self._ema_speeds: dict[str, float] = {}

    def update_smoothed_speed(self, bus_id: str, observed_speed_kmh: float) -> float:
        if observed_speed_kmh < 0:
            raise ValueError("observed_speed_kmh cannot be negative")
        safe_speed = max(observed_speed_kmh, self.min_speed_kmh)
        if bus_id not in self._ema_speeds:
            self._ema_speeds[bus_id] = safe_speed
        else:
            prev = self._ema_speeds[bus_id]
            self._ema_speeds[bus_id] = (self.alpha * safe_speed) + ((1 - self.alpha) * prev)
        return self._ema_speeds[bus_id]

    def _compute_tunnel_state(self, telemetry: BusTelemetry) -> tuple[float, float]:
        last_known_speed = self._ema_speeds.get(
            telemetry.bus_id,
            telemetry.current_speed_kmh if telemetry.current_speed_kmh > 0 else self.default_tunnel_speed_kmh,
        )
        effective_speed = max(last_known_speed, self.min_speed_kmh)
        distance_covered = effective_speed * (telemetry.time_in_tunnel_sec / 3600.0)
        remaining_distance = max(0.0, telemetry.distance_to_stop_km - distance_covered)
        return effective_speed, remaining_distance

    def estimate_eta(self, telemetry: BusTelemetry) -> dict:
        if not telemetry.bus_id or not telemetry.bus_id.strip():
            raise ValueError("bus_id must be a non-empty string")
        if telemetry.distance_to_stop_km < 0:
            raise ValueError("distance_to_stop_km cannot be negative")
        if telemetry.current_speed_kmh < 0:
            raise ValueError("current_speed_kmh cannot be negative")
        if telemetry.time_in_tunnel_sec < 0:
            raise ValueError("time_in_tunnel_sec cannot be negative")
        if telemetry.traffic_factor <= 0:
            raise ValueError("traffic_factor must be strictly positive")

        if telemetry.distance_to_stop_km == 0:
            return {
                "bus_id": telemetry.bus_id,
                "mode": MODE_ARRIVED,
                "remaining_distance_km": 0.0,
                "effective_speed_kmh": 0.0,
                "eta_seconds": 0,
                "eta_minutes": 0.0,
            }

        if telemetry.gps_signal_active and not telemetry.in_tunnel:
            mode = MODE_LIVE_GPS
            effective_speed = self.update_smoothed_speed(telemetry.bus_id, telemetry.current_speed_kmh)
            remaining_distance = telemetry.distance_to_stop_km
        else:
            mode = MODE_TUNNEL
            effective_speed, remaining_distance = self._compute_tunnel_state(telemetry)

        adjusted_speed = max(effective_speed / max(telemetry.traffic_factor, 0.5), self.min_speed_kmh)
        eta_hours = remaining_distance / adjusted_speed
        eta_seconds = round(eta_hours * 3600)
        eta_minutes = round(eta_seconds / 60.0, 2)

        return {
            "bus_id": telemetry.bus_id,
            "mode": mode,
            "remaining_distance_km": round(remaining_distance, 3),
            "effective_speed_kmh": round(adjusted_speed, 2),
            "eta_seconds": eta_seconds,
            "eta_minutes": eta_minutes,
        }


if __name__ == "__main__":
    estimator = ArrivalTimeEstimator()
    print("=== Case 28: City Bus Fleet Tracking (600 Buses) - ETA Prototype ===")
    t1 = BusTelemetry("BUS-028", "R-14", 4.2, 38.0, True, in_tunnel=False, traffic_factor=1.1)
    print("1. Surface Road (GPS Active):", estimator.estimate_eta(t1))
    t2 = BusTelemetry("BUS-028", "R-14", 3.5, 0.0, False, time_in_tunnel_sec=90.0, in_tunnel=True, traffic_factor=1.15)
    print("2. Inside Tunnel (GPS Dropped - Dead Reckoning):", estimator.estimate_eta(t2))
    t3 = BusTelemetry("BUS-028", "R-14", 2.1, 34.0, True, in_tunnel=False, traffic_factor=1.0)
    print("3. Tunnel Exit (GPS Restored):", estimator.estimate_eta(t3))
