import pytest
from L1_3_eta_estimator_after import estimate_arrival_minutes


# Normal cases
def test_tc01_happy_path():
    assert estimate_arrival_minutes(12.0, 36.0, 1.0, 4, 0.5) == 22.0


def test_tc02_heavy_traffic():
    assert estimate_arrival_minutes(10.0, 40.0, 0.5, 3, 1.0) == 33.0


def test_tc03_fast_traffic():
    assert estimate_arrival_minutes(15.0, 30.0, 1.25, 2, 0.5) == 25.0


# Boundary cases
def test_tc04_zero_distance():
    assert estimate_arrival_minutes(0.0, 40.0, 1.0, 0, 1.0) == 0.0


def test_tc05_zero_stops():
    assert estimate_arrival_minutes(6.0, 30.0, 1.0, 0, 2.0) == 12.0


def test_tc06_zero_stop_delay():
    assert estimate_arrival_minutes(6.0, 30.0, 1.0, 5, 0.0) == 12.0


def test_tc07_very_small_speed():
    assert estimate_arrival_minutes(1.0, 0.001, 1.0, 0, 0.0) == 60000.0


def test_tc08_rounding_halfway():
    assert estimate_arrival_minutes(1.0, 60.0, 1.0, 0, 0.05) == 1.1


# Negative cases
@pytest.mark.parametrize(
    "args",
    [
        (10.0, 0.0, 1.0, 2, 0.5),
        (10.0, -25.0, 1.0, 2, 0.5),
        (-5.0, 30.0, 1.0, 2, 0.5),
        (10.0, 30.0, 0.0, 2, 0.5),
        (10.0, 30.0, -0.8, 2, 0.5),
        (10.0, 30.0, 1.0, -1, 0.5),
        (10.0, 30.0, 1.0, 2, -0.5),
        (True, 30.0, 1.0, 2, 0.5),
        (float("nan"), 30.0, 1.0, 2, 0.5),
        (None, 30.0, 1.0, 2, 0.5),
    ],
)
def test_negative_inputs(args):
    with pytest.raises(ValueError):
        estimate_arrival_minutes(*args)
