# Software Engineering Project Report
## Case 28: City Bus Fleet Tracking

| Field | Value |
| :--- | :--- |
| **Student Name** | Keerthana M |
| **Roll Number** | ENG24CS0096 |
| **Class / Section** | 3B |
| **Your Case** | Case 28: City Bus Fleet Tracking |
| **Submission Date** | 22-11-2026 |

---

## 1. Scenario & System Targets
A transport corporation with **600 buses** requires live location tracking, arrival prediction, and a driver duty roster, with special handling for **GPS signal drops in tunnels**.
- **Target Fleet Size:** 600 buses
- **Telemetry Ingestion Target:** 5-second update cycle across 600 buses (120 updates/sec)
- **Tunnel Fallback Target:** Dead-reckoning ETA calculation when GPS signal drops inside tunnels
- **Driver Duty Roster Target:** 3-shift allocation covering all 600 buses

---

## 2. Process Model (Module 1): Spiral
- **Risk-Driven Iterations:** Each Spiral cycle explicitly evaluates technical risks—primarily **GPS signal loss in tunnels** and **600-bus concurrency load**—before scaling to full deployment.
- **Spiral Cycles:**
  1. *Cycle 1:* Core GPS ingestion & basic ETA formula prototype.
  2. *Cycle 2:* Tunnel dead-reckoning prototype & speed smoothing risk mitigation.
  3. *Cycle 3:* Driver duty roster integration & 600-bus load testing.
  4. *Cycle 4:* Production release & commuter ETA alerts.

### Weighted Decision Matrix
| Criteria | Weight | Waterfall | Spiral | V-Model | Incremental | Prototyping |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Risk Management (Tunnel GPS Drop) | 30% | 2 | **5** | 3 | 3 | 4 |
| Scalability to 600 Buses | 25% | 3 | **5** | 4 | 4 | 3 |
| Iterative Stakeholder Feedback | 20% | 2 | **4** | 2 | 4 | 5 |
| Requirements Evolution Handling | 15% | 2 | **4** | 2 | 4 | 4 |
| Schedule & Cost Control | 10% | 4 | **3** | 4 | 4 | 3 |
| **Weighted Score (Max 5.0)** | **100%** | **2.45** | **4.50** | **3.00** | **3.70** | **3.85** |

---

## 3. Agile Method (Module 2): Kanban
- **Continuous Delivery:** Handles ongoing route changes, tunnel closures, and driver roster swaps without waiting for fixed sprint boundaries.
- **WIP Limits:** `Backlog` -> `Ready (WIP: 4)` -> `In Development (WIP: 3)` -> `Tunnel & Load Testing (WIP: 2)` -> `Deployed (600 Buses)`.

---

## 4. AI Tools Used: ChatGPT
- **SRS & Edge-Case Analysis:** Generated tunnel GPS-dropout edge cases (tunnel congestion, GPS reacquisition lag).
- **Algorithm Refactoring:** Added Exponential Moving Average (EMA) speed smoothing and tunnel dead-reckoning projection to the arrival time estimator.
- **Test & Dataset Generation:** Created 600-bus telemetry datasets and unit tests.
