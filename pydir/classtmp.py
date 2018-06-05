# -*- coding: utf-8 -*-
import os,xlrd

class tmpdata(object):
	
	def __init__(self,path):
		self.path=path
		
	def maxtmp(self):
		tmp=talbe=[]
	
		data=xlrd.open_workbook(path)
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
		
a=tmpdata(u'E:\\毕设\\20150402vehicle-京B7Y201-20150416093720.xls')
print a.maxtmp()