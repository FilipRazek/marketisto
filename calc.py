def get_daily_variations(time_series):
    variations = []
    for i in range(1, len(time_series)):
        current = time_series[i].value
        previous = time_series[i - 1].value
        variations.append((current - previous) / previous)
    return variations


def get_expected_yearly_variation(time_series):
    daily_variations = get_daily_variations(time_series)
    total_growth = 1
    for variation in daily_variations:
        total_growth *= 1 + variation
    return total_growth ** (365 / len(daily_variations)) - 1
