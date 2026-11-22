# L1.3 — Arrival Time Estimator Change Log

| Change ID | Modification Made by AI | Valid? | Reason |
| :---: | :--- | :---: | :--- |
| **C1** | Added type annotations and `Optional[float]` return hint | **Yes** | Improves readability, IDE tooling, and static type clarity without altering runtime logic. |
| **C2** | Added default parameter values (`traffic_factor=1.0`, `stops_remaining=0`, `avg_stop_delay_min=0.5`) | **Yes** | Makes optional parameters ergonomic while preserving explicit positional/keyword calls. |
| **C3** | Rejected `bool`, non-numeric, and non-finite (`NaN`/`inf`) inputs with `ValueError` | **Yes** | Prevents silent bugs (`True == 1`, `NaN` propagation, `OverflowError` on `inf`). |
| **C4** | Changed invalid inputs from returning `None` to raising `ValueError` | **Yes (with caller contract note)** | Explicit exceptions prevent silent `None` propagation in ETA pipelines, provided callers handle `ValueError`. |
| **C5** | Added explicit checks for negative `distance_km`, `stops_remaining`, `avg_stop_delay_min`, and `traffic_factor <= 0` | **Yes** | Prevents physically invalid distances/delays and division-by-zero or reversed time when `traffic_factor <= 0`. |
