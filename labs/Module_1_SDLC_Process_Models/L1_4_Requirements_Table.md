# L1.4 — Requirements Conversion: Before & After Table

| Req ID | Type | Before (AI Scenario Draft) | After (Testable Requirement) |
| :---: | :---: | :--- | :--- |
| **FR-01** | Functional | The system should track bus locations using GPS. | The system shall ingest and store GPS latitude, longitude, heading, and timestamp updates from each active bus at least once every 5 seconds. |
| **FR-02** | Functional | The system should predict bus arrival times. | The system shall compute and update estimated time of arrival (ETA) for every active bus across all remaining stops on its route within 2 seconds of each GPS update. |
| **FR-03** | Functional | Dispatchers should see live bus positions on a map. | The dispatcher web map shall render live positions for all 600 buses with status indicators (on-time, delayed, offline) within 3 seconds of telemetry ingestion. |
| **FR-04** | Functional | Commuters should be able to check bus arrivals at a stop. | The commuter interface shall return the next 3 arriving buses and their ETAs for any valid stop ID queried by route or stop code. |
| **FR-05** | Functional | The system should manage driver rosters and shifts. | A fleet supervisor shall be able to create, edit, and publish daily driver-to-bus shift assignments while blocking overlapping shift assignments for the same driver. |
| **FR-06** | Functional | The system should detect when a bus is delayed. | The system shall flag a bus as `DELAYED` and log an alert when its actual progress falls more than 5 minutes behind its scheduled timetable. |
| **FR-07** | Functional | The system should handle temporary GPS signal loss. | When no GPS ping is received from a bus for 30 seconds, the system shall mark the bus `STALE_SIGNAL` and project position using last known speed/route until fresh GPS arrives. |
| **FR-08** | Functional | Supervisors should be able to reassign a bus or driver during disruptions. | A supervisor shall be able to reassign an active bus or substitute driver in under 15 seconds, immediately updating the active roster and ETA calculations. |
| **FR-09** | Functional | The system should record historical trip and delay data. | The system shall persist GPS telemetry, actual vs. predicted arrival times, and shift logs in queryable historical storage for at least 180 days. |
| **FR-10** | Functional | Administrators should generate daily operational reports. | The system shall generate and export a daily fleet summary report (on-time percentage, completed trips, roster coverage, delay count) in CSV/PDF format within 10 seconds. |
| **NFR-01** | Non-Functional | The system should scale to 600 buses smoothly. | Under a simulated load of 600 concurrent buses sending telemetry every 5 seconds (120 updates/sec) plus 500 concurrent queries/min, the system shall maintain p95 API response time under 500 ms. |
| **NFR-02** | Non-Functional | The system should be highly available. | The core tracking, ETA, and roster services shall achieve at least 99.9% monthly uptime excluding scheduled maintenance windows. |
| **NFR-03** | Non-Functional | Unauthorized users should not access fleet controls. | All roster modification and dispatch endpoints shall enforce role-based access control (RBAC) and reject unauthenticated requests with HTTP 401 and unauthorized roles with HTTP 403. |
| **NFR-04** | Non-Functional | Data in transit and at rest should be protected. | All GPS telemetry, API traffic, and stored driver/operational records shall use TLS 1.2+ in transit and AES-256 encryption at rest. |
| **NFR-05** | Non-Functional | The UI should be easy for dispatchers and commuters to use. | A trained dispatcher shall complete a bus/driver reassignment workflow in 3 or fewer UI actions with a 100% task completion rate in usability testing. |
