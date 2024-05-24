from random import choice

class RandomWalk:
    """一个生成随机游走的类"""

    def __init__(self, num_points=5000):
        """初始化随机游走的属性"""
        self.num_points = num_points

        # 所有都初始于（0， 0）
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机游走中所包含的所有点"""

        # 一直填充，知道满足
        while len(self.x_values) < self.num_points:
            
            # 决定方向和移动距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_distance * x_direction

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_distance * y_direction

            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的坐标
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
