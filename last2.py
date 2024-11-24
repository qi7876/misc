import numpy as np
import matplotlib.pyplot as plt

# 给定数据
data = [135, 167, 261, 119, 176, 279, 271, 326, 392, 434, 409, 306, 222, 287, 263, 156, 293, 262, 158, 289, 225, 160, 176, 187, 189, 159, 164, 164, 155, 143, 131, 123, 134, 120, 111, 173]

# 数据归一化
data_max = np.max(data)
normalized_data = np.array(data) / data_max
print(normalized_data)

# 极坐标角度设置（每两个数据间隔10度）
angles = np.linspace(0, 2 * np.pi, len(normalized_data), endpoint=False)

# 添加首尾点以闭合曲线
angles = np.append(angles, angles[0])
normalized_data = np.append(normalized_data, normalized_data[0])

# 绘制极坐标图
fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(angles, normalized_data, label='Normalized Data', marker='o')
ax.fill(angles, normalized_data, alpha=0.3)  # 添加填充
ax.legend(loc='upper right')
ax.set_title("Polar Plot with Normalized Data")
plt.show()

# 输出归一化后的结果
print(normalized_data)  # 去除重复的闭合点