def moving_average(values, window=3):
    """Calculate moving average trend"""
    if len(values) < window:
        return None

    return sum(values[-window:]) / window


def predict_next(values):
    """Simple prediction using last trend"""
    if len(values) < 2:
        return None

    return values[-1] + (values[-1] - values[-2])
