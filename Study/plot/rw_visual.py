import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断模拟
while True:
    # 创建一个RandomWalk实例
    rw = RandomWalk()
    rw.fill_walk()

    # 绘制所有点
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(10, 9))
    point_number = range(rw.num_points)
    ax.scatter(
        rw.x_values, rw.y_values,
        c=point_number, cmap=plt.cm.Blues,
        edgecolors='none', s=15)
    ax.set_aspect('equal') #让刻度的间距相等

    # 突出起点和终点
    ax.scatter(0, 0, c='green', edgecolor='none', s=100)
    # 定义起点为(0,0)，所以输入00
    ax.scatter(
        rw.x_values[-1], rw.y_values[-1],
        c='red', edgecolor='none', s=100
        )
    
    # 隐藏坐标轴
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break