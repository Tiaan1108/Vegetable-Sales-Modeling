import excel "./local-data/附件1.xlsx", sheet("Sheet1") firstrow
nmissing
npresent
save "./local-data/蔬菜字典.dta"
///检查数据缺失情况，发现所有数据均有251条，未出现缺失

import excel "./local-data/附件2.xlsx", sheet("Sheet1") firstrow clear
nmissing
npresent
save "./local-data/交易记录.dta"
///检查数据缺失情况，发现所有数据均有878,503条，未出现缺失

import excel "./local-data/附件3.xlsx", sheet("Sheet1") firstrow clear
nmissing
npresent
save "./local-data/成本字典.dta"
///检查数据缺失情况，发现所有数据均有55,982条，未出现缺失

import excel "./local-data/附件4.xlsx", sheet("平均损耗率(%)_小分类编码_不同值") firstrow clear
nmissing
npresent
save "./local-data/损耗率.dta"
///检查数据缺失情况，发现所有数据均有6条，未出现缺失

use "./local-data/交易记录.dta"
rename 销售日期 日期
merge m:1 日期 单品编码 using "./local-data/成本字典.dta"
keep if _merge==3
drop _merge
///检查后发现有9383种成本记录未在销售记录中出现
merge m:1 单品编码 using "./local-data/蔬菜字典.dta"
keep if _merge==3
drop _merge
///检查后发现有5种蔬果代码未在销售记录中出现

gen 收入 = 销量千克* 销售单价元千克
bysort 分类名称 : egen 分类总收入=sum( 收入 )
bysort 分类名称 ：egen 分类总销量=sum（销量千克）
bysort 日期 单品名称 : egen 分种日收入=sum( 收入 )
///饼状图绘制数据准备

duplicates drop 日期 单品名称 分种日收入 , force
save "./local-data/相关性分析.dta"
drop 扫码销售时间 单品编码 销量千克 销售单价元千克 销售类型 是否打折销售 批发价格元千克 分类编码 分类名称 收入 分类总收入
rename 分种日收入 a
label variable a "分种日收入"
generate 名称 = subinstr( 单品名称 , "(", "", .)
replace 名称 = subinstr( 名称 , ")", "", .)
drop 单品名称 
reshape wide a , i(日期) j(名称) string
logout, save("`s'") excel replace: pwcorr_a *
///输出相关性矩阵
