import requests
from lxml import etree
import json
import openpyxl

url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia'
headers = {
    "User-Agent": "rhd"
}
response = requests.get(url=url, headers=headers).text


html = etree.HTML(response)
# print(html)
json_text = html.xpath('//script[@type="application/json"]/text()')
json_text = json_text[0]
# print(json_text)

#文件内容在component中
result = json.loads(json_text)["component"]
# print(result)
# 获取国内疫情
result = result[0]['caseList']
print(result)
#
#
wb = openpyxl.Workbook()
# 创建工作表ws = wb.active# 设置表的标题
ws = wb.active
wb.title = "国内疫情"
# 写入表头
ws.append(["省份","新增","现有","累计确诊","治愈","死亡"])
# 按要求写入
for line in result:
    line_name = [line["area"], line["confirmedRelative"], line["curConfirm"], line["confirmed"], line["crued"], line["died"]]
    for ele in line_name:
        if ele == '':
             ele = 0
    ws.append(line_name)
wb.save('./covoid.csv')