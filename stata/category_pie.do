clear
input sale1 sale2 sale3 sale4 sale5 sale6
	40581.35  198521 41766.45 22431.78 91588.63 76086.73
end

label var sale1 "水生根茎类"
label var sale2 "花叶类"
label var sale3 "花菜类"
label var sale4 "茄类"
label var sale5 "辣椒类"
label var sale6 "食用菌"

#d;
graph pie sale1 sale2 sale3 sale4 sale5 sale6 , 
plabel(_all name, size(*1.5) color(white))       
legend(off)                                  
plotregion(lstyle(none))                        
title("各品类总销售价格饼状图")
subtitle("2020.7-2023.6")；
#d cr
