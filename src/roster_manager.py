"""
Driver Duty Roster Manager for 600 Buses across 3 Daily Shifts
"""
def generate_driver_roster(total_buses: int = 600) -> list[dict]:
    shifts = [
        ("Shift-A (Morning)", "06:00 - 14:00"),
        ("Shift-B (Afternoon)", "14:00 - 22:00"),
        ("Shift-C (Night)", "22:00 - 06:00"),
    ]
    roster = []
    driver_counter = 1
    for bus_num in range(1, total_buses + 1):
        bus_id = f"BUS-{bus_num:03d}"
        active_shifts = shifts if bus_num % 5 == 0 else shifts[:2]
        for shift_name, timing in active_shifts:
            roster.append({
                "bus_id": bus_id,
                "driver_id": f"DRV-{driver_counter:04d}",
                "shift": shift_name,
                "timing": timing,
                "status": "SCHEDULED",
            })
            driver_counter += 1
    return roster


if __name__ == "__main__":
    roster = generate_driver_roster(600)
    print(f"Total Duty Assignments for 600 Buses: {len(roster)}")
    print("First 5 Assignments:", roster[:5])
