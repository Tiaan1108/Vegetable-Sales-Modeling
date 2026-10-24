clear
import delimited ./local-data/df38.csv, encoding(UTF-8) 
gen datetime_variable = clock( 销售日期 , "YMD hms")
reg 销售单价元千克 datetime_variable 销量千克 是否打折销售
append using append.dta
predict predicted_values
keep if 销售日期 == "2023-07-01 8:00:00"
