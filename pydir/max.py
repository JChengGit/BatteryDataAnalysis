# -*- coding: utf-8 -*-
#找出单个文件的温度最大值

import xlrd

data=xlrd.open_workbook(u'20150402\\vehicle-京B7Y203-20150416094032.xls')
table=data.sheet_by_index(0)

tmp=table.col_values(12)
time=table.col_values(22)

i=int(0)
tmpnum=[]
for t in tmp:
	if i>1:
		t1=t[:-2]
		t2=t1.encode('utf-8')
		t3=int(t2)
		tmpnum.append(t3)
	i+=1

maxtmp=max(tmpnum)

i=0
maxtime=[]
for t in tmp:
	if i>1:
		t1=t[:-2]
		t2=t1.encode('utf-8')
		t3=int(t2)
		if t3==maxtmp:
			maxtime.append(time[i])
	i+=1

print u'最高温度是：'
print maxtmp,u'℃'
print u'其时间点为：'
for x in maxtime:
	print x

