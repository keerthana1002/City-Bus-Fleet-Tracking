# L1.2 — Weighted Process Model Decision Matrix: City Bus Fleet Tracking

| Evaluation Criterion | Weight | Waterfall | Iterative / Incremental | Prototyping | RAD | Spiral |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Risk & Uncertainty Management** (GPS dropouts, traffic spikes, ETA accuracy) | 0.25 | 4 | 7 | 6 | 5 | 10 |
| **Iterative Prototyping & Telemetry** (early GPS ingestion & ETA model validation) | 0.25 | 3 | 8 | 8 | 7 | 9 |
| **Changing Requirements Adaptability** (route changes, roster & SLA adjustments) | 0.20 | 2 | 7 | 7 | 7 | 9 |
| **Schedule & Milestone Predictability** (phased delivery across 600 buses) | 0.15 | 7 | 7 | 5 | 8 | 8 |
| **Stakeholder & Roster Integration** (dispatchers, drivers, commuters, IT ops) | 0.15 | 4 | 7 | 6 | 6 | 8 |
| **Weighted Score (out of 10.00)** | **1.00** | **3.80** | **7.25** | **6.55** | **6.50** | **8.95** |

## Conclusion (Spiral Selection)
Spiral scores highest (**8.95/10**) because it pairs iterative delivery with formal risk analysis at every cycle. In a 600-bus fleet system, GPS signal loss, peak-hour congestion, and real-time ETA drift pose high technical risk early on. Each spiral lets the team prototype telemetry ingestion and ETA models, evaluate risks, and refine requirements with dispatchers before scaling. This prevents costly late-stage rework while keeping milestones structured and predictable.
