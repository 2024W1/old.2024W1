import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义桌腿数量和桌面数量的范围
x = np.arange(0, 21, 1)  # 桌腿数量
y = np.arange(0, 21, 1)  # 桌面数量

# 创建网格
X, Y = np.meshgrid(x, y)

# 计算能生产的桌子数量
Z = np.minimum(X // 4, Y)  # 每张桌子需要4条腿，桌子数量受桌腿和桌面数量的限制

# 创建三维图形
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 绘制三维阶梯图
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='k', rstride=1, cstride=1, linewidth=0, antialiased=False)

# 设置轴标签
ax.set_xlabel('Beine (x)')
ax.set_ylabel('Platte (y)')
ax.set_zlabel('Tisch (z)')

# 添加颜色条
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

# 显示图形
plt.show()
