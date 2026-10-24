# 2023 数学建模：蔬菜销售分析

销售预处理、相关性、回归及 LSTM 需求预测尝试。

本项目整理自本科本地材料，作为独立课程作品档案保存。可能包含课程模板或参考实现，尚未逐段确认原创贡献，不把整个目录声称为独立原创。

## 文件

- `notebooks/lstm_demand_draft.ipynb`
- `python/sales_preprocessing.py`
- `python/correlation_filter.py`
- `stata/regression_draft.do`
- `stata/sales_correlations.do`
- `stata/category_pie.do`

## 环境

pandas、openpyxl、NumPy、Matplotlib、scikit-learn、TensorFlow，以及 Stata。

不包含数据集、权重、讲义、题目、报告、旧输出或打包程序。`./local-data/` 是原电脑路径的替代标记，需要映射到获准使用的数据。Notebook 请重启内核后按顺序执行；不保证可完整运行。

## 已知问题

原 q3 Notebook 留有 reshape 异常：64 个元素不能重塑为 4×7×4；归一化先于训练测试划分，需检查泄漏。预处理含硬编码行数和类别位置。correlation_filter.py 中 if "***" in lines 的判定对象应复查。不是完整可复现的获奖作品或定价系统。

## 来源

[SOURCES.json](SOURCES.json) 记录原文件哈希、来源和处理方式。Notebook 仅保留代码单元，清除全部输出、题目正文和个人元数据；R Markdown 仅抽取 R 代码块。原始本地文件未改动。

除贪吃蛇列出的修复外，本次仅整理归档，没有静默修正算法。未提供覆盖课程衍生内容的开源许可证；公开展示前需确认课程要求和贡献归属。
