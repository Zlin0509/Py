from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

datas, highs, lows = [], [], []
for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[3])
        low = int(row[4])
    except ValueError:
        print(f"Error_data for {current_date}")
    else:
        lows.append(low)
        highs.append(high)
        datas.append(current_date)


# plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(datas, highs, color='red', alpha=0.5)
ax.plot(datas, lows, color='blue', alpha=0.5)
ax.fill_between(datas, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("hhh", fontsize=20)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=12)

plt.show()