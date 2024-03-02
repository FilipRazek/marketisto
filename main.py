from api import get_time_series
import matplotlib.pyplot as plt

symbol = "AAPL"


def get_daily_variations(time_series):
    variations = []
    for i in range(1, len(time_series)):
        current = time_series[i].value
        previous = time_series[i - 1].value
        variations.append((current - previous) / previous)
    return variations


def get_expected_daily_variation(time_series):
    daily_variations = get_daily_variations(time_series)
    total_growth = 1
    for variation in daily_variations:
        total_growth *= 1 + variation
    return total_growth ** (1 / len(daily_variations)) - 1


def get_cycles(time_series):
    expected_daily_variation = get_expected_daily_variation(time_series)
    expected_value = time_series[0].value
    dates = [time_series[0].date]
    cycles = [1]

    for eod in time_series[1:]:
        expected_value *= 1 + expected_daily_variation
        cycles.append(eod.value / expected_value)
        dates.append(eod.date)

    return dates, cycles


time_series = get_time_series(symbol)
dates, cycles = get_cycles(time_series)
values = [eod.value for eod in time_series]

fig, ax = plt.subplots()
ax.plot(dates, cycles, label="Cycles", color="blue")
ax.set_xlabel("Date")
ax.set_ylabel("Cycle")
ax.legend(loc="center")

ax2 = ax.twinx()
ax2.plot(dates, values, label="Stock price", color="red")
ax2.set_xlabel("Date")
ax2.set_ylabel("Stock price")
ax2.legend(loc="right")

plt.show()
