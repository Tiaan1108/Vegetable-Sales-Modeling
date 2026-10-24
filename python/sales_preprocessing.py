import pandas as pd
import openpyxl
openpyxl.workbook.Workbook.max_rows = 10000000
openpyxl.workbook.Workbook.max_columns = 10000000
df = pd.read_excel('./local-data/23建模/问题1/raw/附件1.xlsx')
df2 = pd.read_excel('./local-data/23建模/问题1/raw/附件2.xlsx')
df3 = pd.read_excel('./local-data/23建模/问题1/raw/附件3.xlsx')
count = 0
huaye = []
huacai = []
shuisheng = []
qielei = []
lajiao = []
shiyongjun = []
huayexiaoliang = 0
huacaixiaoliang = 0
shuishengxiaoliang = 0
qieleixiaoliang = 0
lajiaoxiaoliang = 0
shiyongjunxiaoliang = 0
huayexiaodan = 0
huacaixiaodan = 0
shuishengxiaodan = 0
qieleixiaodan = 0
lajiaoxiaodan = 0
shiyongjunxiaodan = 0
huayechengben = 0
huacaichengben = 0
shuishengchengben = 0
qieleichengben = 0
lajiaochengben = 0
shiyongjunchengben = 0

for i in df['单品编码']:
    if count <= 99:
        huaye.append(i)
    elif count > 99 and count <= 104:
        huacai.append(i)
    elif count > 104 and count <= 123:
        shuisheng.append(i)
    elif count > 123 and count <= 133:
        qielei.append(i)
    elif count > 133 and count <= 178:
        lajiao.append(i)
    else:
        shiyongjun.append(i)
    count += 1

for k in range(33596):
    riqi = df2['销售日期'][k]
    ma = df2['单品编码'][k]
    xiaoliang = df2['销量(千克)'][k]
    jiage = df2['销售单价(元/千克)'][k]
    number = 0
    for p in range(1139):
        if df3['日期'][p] == riqi:
            if df3['单品编码'][p] == ma:
                pifa = df3['批发价格(元/千克)'][p]
                number = p
                break
    if (ma in huaye):
        huayexiaoliang += xiaoliang
        huayexiaodan += jiage * xiaoliang
        huayechengben += pifa * xiaoliang
    elif (ma in huacai):
        huacaixiaoliang += xiaoliang
        huacaixiaodan += jiage * xiaoliang
        huacaichengben += pifa * xiaoliang
    elif (ma in shuisheng):
        shuishengxiaoliang += xiaoliang
        shuishengxiaodan += jiage * xiaoliang
        shuishengchengben += pifa * xiaoliang
    elif (ma in qielei):
        qieleixiaoliang += xiaoliang
        qieleixiaodan += jiage * xiaoliang
        qieleichengben += pifa * xiaoliang
    elif (ma in lajiao):
        lajiaoxiaoliang += xiaoliang
        lajiaoxiaodan += jiage * xiaoliang
        lajiaochengben += pifa * xiaoliang
    else:
        shiyongjunxiaoliang += xiaoliang
        shiyongjunxiaodan += jiage * xiaoliang
        shiyongjunchengben += pifa * xiaoliang
        
for k in range(347263,374057):
    riqi = df2['销售日期'][k]
    ma = df2['单品编码'][k]
    xiaoliang = df2['销量(千克)'][k]
    jiage = df2['销售单价(元/千克)'][k]
    number = 0
    for p in range(16637,18264):
        if df3['日期'][p] == riqi:
            if df3['单品编码'][p] == ma:
                pifa = df3['批发价格(元/千克)'][p]
                number = p
                break
    if (ma in huaye):
        huayexiaoliang += xiaoliang
        huayexiaodan += jiage * xiaoliang
        huayechengben += pifa * xiaoliang
    elif (ma in huacai):
        huacaixiaoliang += xiaoliang
        huacaixiaodan += jiage * xiaoliang
        huacaichengben += pifa * xiaoliang
    elif (ma in shuisheng):
        shuishengxiaoliang += xiaoliang
        shuishengxiaodan += jiage * xiaoliang
        shuishengchengben += pifa * xiaoliang
    elif (ma in qielei):
        qieleixiaoliang += xiaoliang
        qieleixiaodan += jiage * xiaoliang
        qieleichengben += pifa * xiaoliang
    elif (ma in lajiao):
        lajiaoxiaoliang += xiaoliang
        lajiaoxiaodan += jiage * xiaoliang
        lajiaochengben += pifa * xiaoliang
    else:
        shiyongjunxiaoliang += xiaoliang
        shiyongjunxiaodan += jiage * xiaoliang
        shiyongjunchengben += pifa * xiaoliang

for k in range(593473,618702):
    riqi = df2['销售日期'][k]
    ma = df2['单品编码'][k]
    xiaoliang = df2['销量(千克)'][k]
    jiage = df2['销售单价(元/千克)'][k]
    number = 0
    for p in range(37537,39428):
        if df3['日期'][p] == riqi:
             if df3['单品编码'][p] == ma:
                pifa = df3['批发价格(元/千克)'][p]
                number = p
                break
    if (ma in huaye):
        huayexiaoliang += xiaoliang
        huayexiaodan += jiage * xiaoliang
        huayechengben += pifa * xiaoliang
    elif (ma in huacai):
        huacaixiaoliang += xiaoliang
        huacaixiaodan += jiage * xiaoliang
        huacaichengben += pifa * xiaoliang
    elif (ma in shuisheng):
        shuishengxiaoliang += xiaoliang
        shuishengxiaodan += jiage * xiaoliang
        shuishengchengben += pifa * xiaoliang
    elif (ma in qielei):
        qieleixiaoliang += xiaoliang
        qieleixiaodan += jiage * xiaoliang
        qieleichengben += pifa * xiaoliang
    elif (ma in lajiao):
        lajiaoxiaoliang += xiaoliang
        lajiaoxiaodan += jiage * xiaoliang
        lajiaochengben += pifa * xiaoliang
    else:
        shiyongjunxiaoliang += xiaoliang
        shiyongjunxiaodan += jiage * xiaoliang
        shiyongjunchengben += pifa * xiaoliang

print('花叶2020-2022年7月的总销量是:' + str(huayexiaoliang) + '花叶2020-2022年7月的总销售额是' + str(huayexiaodan) + '花叶2020-2022年7月的总成本是:' + str(huayechengben))
print('花菜2020-2022年7月的总销量是:' + str(huacaixiaoliang) + '花菜2020-2022年7月的总销售额是' + str(huacaixiaodan) + '花菜2020-2022年7月的总成本是:' + str(huacaichengben))
print('水生2020-2022年7月的总销量是:' + str(shuishengxiaoliang) + '水生2020-2022年7月的总销售额是' + str(shuishengxiaodan) + '水生2020-2022年7月的总成本是:' + str(shuishengchengben))
print('茄类2020-2022年7月的总销量是:' + str(qieleixiaoliang) + '茄类2020-2022年7月的总销售额是' + str(qieleixiaodan) + '茄类2020-2022年7月的总成本是:' + str(qieleichengben))
print('辣椒2020-2022年7月的总销量是:' + str(lajiaoxiaoliang) + '辣椒2020-2022年7月的总销售额是' + str(lajiaoxiaodan) + '辣椒2020-2022年7月的总成本是:' + str(lajiaochengben))
print('食用菌2020-2022年7月的总销量是:' + str(shiyongjunxiaoliang) + '食用菌2020-2022年7月的总销售额是' + str(shiyongjunxiaodan) + '食用菌2020-2022年7月的总成本是:' + str(shiyongjunchengben))