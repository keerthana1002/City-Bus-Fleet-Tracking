# L1.5 — Test Cases for Arrival Time Estimator (Normal, Boundary & Negative)

| Test ID | Category | Inputs (`distance_km`, `average_speed_kmph`, `traffic_factor`, `stops_remaining`, `avg_stop_delay_min`) | Expected Result |
| :---: | :---: | :--- | :--- |
| **TC-01** | Normal / Happy Path | `(12.0, 36.0, 1.0, 4, 0.5)` | Returns `22.0` |
| **TC-02** | Normal / Heavy Traffic | `(10.0, 40.0, 0.5, 3, 1.0)` | Returns `33.0` |
| **TC-03** | Normal / Fast Traffic | `(15.0, 30.0, 1.25, 2, 0.5)` | Returns `25.0` |
| **TC-04** | Boundary (Zero Distance) | `(0.0, 40.0, 1.0, 0, 1.0)` | Returns `0.0` |
| **TC-05** | Boundary (Zero Remaining Stops) | `(6.0, 30.0, 1.0, 0, 2.0)` | Returns `12.0` |
| **TC-06** | Boundary (Zero Stop Delay) | `(6.0, 30.0, 1.0, 5, 0.0)` | Returns `12.0` |
| **TC-07** | Boundary (Very Small Positive Speed) | `(1.0, 0.001, 1.0, 0, 0.0)` | Returns `60000.0` |
| **TC-08** | Boundary (Rounding Halfway) | `(1.0, 60.0, 1.0, 0, 0.05)` | Returns `1.1` |
| **TC-09** | Negative (Zero Speed) | `(10.0, 0.0, 1.0, 2, 0.5)` | Raises `ValueError` |
| **TC-10** | Negative (Negative Speed) | `(10.0, -25.0, 1.0, 2, 0.5)` | Raises `ValueError` |
| **TC-11** | Negative (Negative Distance) | `(-5.0, 30.0, 1.0, 2, 0.5)` | Raises `ValueError` |
| **TC-12** | Negative (Zero / Negative Traffic Factor) | `(10.0, 30.0, 0.0, 2, 0.5)` and `(10.0, 30.0, -0.8, 2, 0.5)` | Raises `ValueError` |
| **TC-13** | Negative (Negative Stops / Delay) | `(10.0, 30.0, 1.0, -1, 0.5)` and `(10.0, 30.0, 1.0, 2, -0.5)` | Raises `ValueError` |
| **TC-14** | Negative (Boolean / `NaN` / `None` / String) | `(True, 30.0, 1.0, 2, 0.5)` and `(float('nan'), 30.0, 1.0, 2, 0.5)` | Raises `ValueError` |
