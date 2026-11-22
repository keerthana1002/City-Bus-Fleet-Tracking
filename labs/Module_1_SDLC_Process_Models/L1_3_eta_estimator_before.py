def estimate_arrival_minutes(distance_km, average_speed_kmph, traffic_factor, stops_remaining, avg_stop_delay_min):
    if average_speed_kmph <= 0:
        return None
    driving_hours = distance_km / (average_speed_kmph * traffic_factor)
    driving_minutes = driving_hours * 60
    stop_minutes = stops_remaining * avg_stop_delay_min
    total_minutes = driving_minutes + stop_minutes
    return round(total_minutes, 1)
