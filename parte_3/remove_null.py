#coding:utf-8

f = open('despesa_anual_2017_PB_copy.csv')

f = f.readlines()
out = 'despesa_anual_2017_PB__.csv'
o = open(out, 'w')
for i in f:
	line = i.split(',')
	if line[16] == "\"#NULO#\"":
		continue
	o.write(i)
