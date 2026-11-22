# Software Requirements Specification (SRS)
## Case 28: City Bus Fleet Tracking
**Student:** Keerthana M | **Roll Number:** ENG24CS0096 | **Class/Section:** 3B

### Functional Requirements
1. **FR-1 (Live Location):** Track real-time coordinates and speed of **600 buses**.
2. **FR-2 (Tunnel Dead-Reckoning):** Automatically switch to dead-reckoning using last known EMA speed when GPS signals drop inside tunnels.
3. **FR-3 (Arrival Prediction):** Estimate stop-level arrival time (ETA) in seconds and minutes adjusted for congestion.
4. **FR-4 (Driver Duty Roster):** Assign drivers across Shift-A (06:00–14:00), Shift-B (14:00–22:00), and Shift-C (22:00–06:00) for all **600 buses**.

### Non-Functional Requirements
1. **NFR-1 (Scale):** Support 600 concurrent buses within `< 500 ms` latency.
2. **NFR-2 (Reliability):** 99.9% uptime during daily transit hours.
