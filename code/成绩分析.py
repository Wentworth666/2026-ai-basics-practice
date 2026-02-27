import pandas as pd  # 导入pandas库，并给它起名为pd

# 定义一个字典data，用来保存学生信息
data = {
    "姓名": ["张三", "李四", "王五"],  # "姓名"这一列，对应三个学生的名字
    "成绩": [92, 85, 78],  # "成绩"这一列，对应三个学生的分数
}

df = pd.DataFrame(data)  # 用字典data创建一个DataFrame表格，命名为df

print("学生成绩表：")  # 打印提示文字
print(df)  # 打印整个表格df

# 计算"成绩"这一列的平均值，保存到avg_score中
avg_score = df["成绩"].mean()
print("平均成绩：", avg_score)  # 打印平均成绩

# 找到"成绩"最高分所在的行索引
max_index = df["成绩"].idxmax()
best_student = df.loc[max_index, "姓名"]  # 根据行索引取出对应的"姓名"
best_score = df.loc[max_index, "成绩"]  # 根据行索引取出对应的"成绩"

print("最高分学生：", best_student, "，成绩：", best_score)  # 打印最高分学生的姓名和成绩

# ==================== 下面是绘图部分（柱状图 + 饼图） ====================

import matplotlib.pyplot as plt

# 设置中文字体（防止中文乱码）
plt.rcParams['font.sans-serif'] = ['SimHei']  # Windows常用字体
plt.rcParams['axes.unicode_minus'] = False

# 柱状图
plt.figure(figsize=(8, 5))
plt.bar(df["姓名"], df["成绩"], color=['#4e79a7', '#f28e2b', '#76b7b2'])
plt.title("学生成绩柱状图")
plt.xlabel("姓名")
plt.ylabel("成绩")
plt.ylim(0, 100)
for i, v in enumerate(df["成绩"]):
    plt.text(i, v + 1, str(v), ha='center')
plt.show()

# 饼图
plt.figure(figsize=(7, 7))
plt.pie(df["成绩"], labels=df["姓名"], autopct='%1.1f%%', colors=['#4e79a7', '#f28e2b', '#76b7b2'])
plt.title("学生成绩占比饼图")
plt.show()