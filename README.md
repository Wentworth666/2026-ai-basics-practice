# 2026-ai-basics-practice

2025-2026 大一下人工智能应用基础课程个人练习项目  
Personal Practice Projects for 2025-2026 AI Basics Course (Big Data Major)

## 项目简介 / Project Description

使用 Python + pandas + matplotlib 进行简单学生成绩数据分析与可视化，包括：
- 创建 DataFrame
- 计算平均分 & 最高分
- 柱状图 (Bar Chart) & 饼图 (Pie Chart)

## 技术栈 / Tech Stack

- Python 3.11
- pandas 3.0.1
- matplotlib
  ## 环境要求
- Python 3.11
- conda 环境：bigdata
- 依赖：pandas, matplotlib

## 运行方法 / How to Run

1. 激活环境：
   ```bash
   conda activate bigdata
2. 进入文件夹并运行：
   ```Bashcd
   "D:\BigdataLearning\2025-2026-2学期\人工智能应用基础\code"
   python "成绩分析.py"
## 运行效果截图

### 柱状图（学生成绩分布）
![学生成绩柱状图](bar_chart.png)

### 饼图（成绩占比）
![学生成绩饼图](pie_chart.png)

### 终端输出示例（表格 + 平均分 + 最高分）
![终端输出](terminal_output.png)
## 项目亮点 / Highlights
- 完整实现了数据读取、统计分析、可视化全流程，支持 CSV 文件读取（真实数据分析）
- 支持中文显示（解决 matplotlib 中文乱码）
- 代码注释清晰，适合初学者学习 pandas + matplotlib
- 计算多种统计指标（平均、最高、最低、中位数、标准差）

## 未来计划 / Next Steps
- 支持读取 CSV 文件（真实成绩表）
- 添加更多统计：中位数、标准差、成绩分布直方图
- 导出分析结果为 Excel 或 PDF 报告
- 尝试用 seaborn 做更美观的图表

## 致谢 / Thanks
感谢 Cursor AI 辅助代码生成，感谢 Grok 一步步指导环境配置和 GitHub 上传！
