import math
from typing import Optional


def estimate_arrival_minutes(
    distance_km: float,
    average_speed_kmph: float,
    traffic_factor: float = 1.0,
    stops_remaining: int = 0,
    avg_stop_delay_min: float = 0.5,
) -> Optional[float]:
    """Estimate remaining bus arrival time in minutes with input validation."""
    values = (distance_km, average_speed_kmph, traffic_factor, stops_remaining, avg_stop_delay_min)
    if any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in values):
        raise ValueError("All inputs must be finite numeric values.")

    if distance_km < 0 or average_speed_kmph <= 0 or traffic_factor <= 0 or stops_remaining < 0 or avg_stop_delay_min < 0:
        raise ValueError("Distance, stops, and delays must be non-negative; speed and traffic_factor must be positive.")

    effective_speed = average_speed_kmph * traffic_factor
    driving_minutes = (distance_km / effective_speed) * 60.0
    stop_minutes = stops_remaining * avg_stop_delay_min
    return round(driving_minutes + stop_minutes, 1)
