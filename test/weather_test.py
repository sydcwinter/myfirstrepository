import pandas as pd
from app.weather import get_location, display_forecast


def test_get_location():
    assert isinstance(get_location("20007"), pd.Series)

def test_display_forecast():
    assert display_forecast(latitude = 38.914, longitude = -77.074) == 7

