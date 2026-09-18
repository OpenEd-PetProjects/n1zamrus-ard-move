"""Pure motion-detection logic that can be reused by an Arduino adapter."""


def motion_detected(previous_value: int, current_value: int, threshold: int = 10) -> bool:
    """Return whether the sensor value changed by at least ``threshold``."""
    if threshold <= 0:
        raise ValueError("threshold must be greater than zero")

    return abs(current_value - previous_value) >= threshold
