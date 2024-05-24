import plotly.express as px

from die import Die

die = Die()

# 储存投骰子的结果
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果可视化
title = "Results of Rolling One D6 1,000 Times"
labels = {'x':'Result', 'y':'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies,title=title, labels=labels)
fig.show()