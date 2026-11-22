@echo off
echo ====================================================
echo   Case 28: City Bus Fleet Tracking (600 Buses)
echo   Arrival Time Estimator Prototype
echo ====================================================
python src/arrival_estimator.py
echo.
python src/fleet_simulator.py
echo.
pytest tests/
pause
