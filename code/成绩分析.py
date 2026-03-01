# ==================== CSV 文件读取 + 统计分析 + 导出 Excel ====================

import pandas as pd
import matplotlib.pyplot as plt
import os

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

print("=== 开始读取 CSV 文件 ===\n")

file_path = 'students.csv'

if not os.path.exists(file_path):
    print(f"错误：文件 '{file_path}' 不存在！")
    print("请把 students.csv 文件放到和 成绩分析.py 同一文件夹里")
else:
    # 读取 CSV
    df = pd.read_csv(file_path)
    print("文件读取成功！原始数据如下：")
    print(df)

    # 计算统计结果
    print("\n=== 统计结果 ===")
    avg = df['成绩'].mean()
    max_score = df['成绩'].max()
    min_score = df['成绩'].min()
    median = df['成绩'].median()
    std = df['成绩'].std()

    print(f"平均成绩：{avg:.1f}")
    print(f"最高成绩：{max_score}")
    print(f"最低成绩：{min_score}")
    print(f"中位数：{median}")
    print(f"标准差：{std:.2f}")

    # ==================== 导出 Excel ====================
    results = {
        "统计项目": ["平均成绩", "最高成绩", "最低成绩", "中位数", "标准差"],
        "结果": [avg, max_score, min_score, median, std]
    }
    results_df = pd.DataFrame(results)
    
    excel_file = 'analysis_results.xlsx'
    results_df.to_excel(excel_file, index=False)
    print(f"\n统计结果已导出为：{excel_file}")

        # ==================== 保存图表为文件（适合 WSL 和 GitHub） ====================

    # 柱状图
    plt.figure(figsize=(8, 5))
    plt.bar(df["姓名"], df["成绩"], color=['#4e79a7', '#f28e2b', '#76b7b2'])
    plt.title("学生成绩柱状图")
    plt.xlabel("姓名")
    plt.ylabel("成绩")
    plt.ylim(0, 100)
    for i, v in enumerate(df["成绩"]):
        plt.text(i, v + 1, str(v), ha='center')
    plt.savefig('bar_chart.png')   # 保存为文件
    print("柱状图已保存为 bar_chart.png")

    # 饼图
    plt.figure(figsize=(7, 7))
    plt.pie(df["成绩"], labels=df["姓名"], autopct='%1.1f%%',
            colors=['#4e79a7', '#f28e2b', '#76b7b2'])
    plt.title("学生成绩占比饼图")
    plt.savefig('pie_chart.png')   # 保存为文件
    print("饼图已保存为 pie_chart.png")