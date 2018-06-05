# -*- coding: utf-8 -*-

import os,xlrd

def maxtmp(filepath):
	data=xlrd.open_workbook(filepath)
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
		
	return maxtmp

print maxtmp(u'E:\\毕设\\20150402\\vehicle-京B7Y201-20150416093720.xls')