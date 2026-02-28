# 2026-ai-basics-practice

**大一下人工智能应用基础课程个人实践项目**  
（2025-2026 学年上学期）

## 项目简介

使用 Python + pandas + matplotlib 实现学生成绩数据的读取、统计分析与可视化。  
支持从 CSV 文件读取真实数据，计算多种统计指标，并生成柱状图和饼图。

## 技术栈

- Python 3.11
- conda 环境：bigdata
- 依赖库：pandas, matplotlib

## 运行方法

1. 激活环境：
   ```bash
   conda activate bigdata
   ```

2. 进入项目文件夹并运行：
   ```bash
   cd "D:\BigdataLearning\2025-2026-2学期\人工智能应用基础\code"
   python "成绩分析.py"
   ```

**注意**：请确保 `students.csv` 文件与 `成绩分析.py` 在同一文件夹中。  
示例 CSV 格式（第一行是表头）：

## 运行效果截图（CSV 版本）

### 柱状图（学生成绩分布）
![柱状图](bar_chart.png)

### 饼图（成绩占比）
![饼图](pie_chart.png)

### 终端输出示例（读取 CSV 后）
![终端输出](terminal_output.png)

## 项目亮点

- 支持从 CSV 文件读取真实数据（更贴近实际应用）
- 计算完整统计指标：平均分、最高分、最低分、中位数、标准差
- 中文图表显示正常（已解决 matplotlib 乱码问题）
- 代码结构清晰，注释详细，适合初学者学习
- 完整 GitHub 项目流程：代码 + README + 运行截图

## 未来计划

- 支持导出统计结果为 Excel 报告
- 添加成绩分段统计（优秀/良好/及格/不及格）
- 使用 seaborn 美化图表
- 尝试集成简单异常检测（分数异常预警）

欢迎 Star & Fork！

## 联系方式

- GitHub: @Wentworth666
- 项目链接: https://github.com/Wentworth666/2026-ai-basics-practice

最后更新：2026-02-28
