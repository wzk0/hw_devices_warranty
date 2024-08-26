import os
import json
from openpyxl import Workbook
import ctypes

# 创建一个新的Excel工作簿
wb = Workbook()
ws = wb.active

# 获取当前文件夹下的所有JSON文件
json_files = [f for f in os.listdir('.') if f.endswith('.json')]

# 合并所有JSON文件中的数据
all_data = []

for file in json_files:
    with open(file, 'r', encoding='utf-8') as f:
        for ff in json.load(f):
            all_data.append(ff)

headers = list(all_data[0].keys())
ws.append(headers)

for item in all_data:
    ws.append([item.get(header, '') for header in headers])

wb.save('all.xlsx')

ctypes.windll.user32.MessageBoxW(0, "合并完毕！数据已导出至 all.xlsx\n【共%s条】" % len(all_data), "提示", 0x40 | 0x1)
