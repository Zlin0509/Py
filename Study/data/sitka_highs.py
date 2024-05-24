from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

datas, highs, lows = [], [], []
for row in reader:
    low = int(row[5])
    lows.append(low)
    current_data = datetime.strptime(row[2], '%Y-%m-%d')
    datas.append(current_data)
    high = int(row[4])
    highs.append(high)

# plt.style.use('seaborn')
fig,ax = plt.subplots()
ax.plot(datas, highs, color='red', alpha=0.5)
ax.plot(datas, lows, color='blue', alpha=0.5)
ax.fill_between(datas, highs, lows, facecolor='blue', alpha=0.1)

ax.set_title("hhh", fontsize=24)
ax.set_xlabel('', fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()

# for index, column_header in enumerate(header_row):
#     print(index, column_header)