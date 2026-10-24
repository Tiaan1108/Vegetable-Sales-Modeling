# 打开文本文件以读取
with open("./local-data/Table2_corr.txt", "r") as file:
    # 读取每一行
    lines = file.readlines()

# # 创建一个新的文本文件以写入
# with open("output.txt", "w") as output_file:
#     # 遍历每一行
#     for line in lines:
#         # 根据条件筛选行，例如仅保留包含关键词 "筛选条件" 的行
#         if "筛选条件" in line:
#             output_file.write(line)
for line in lines:
    if "***" in lines:
        print(line)