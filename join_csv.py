#coding:utf-8
import os

def load_tab(f):
	res = []
	f = open(f)
	f = f.readlines()
	for l in f:
		l = l.split('\n')[0]
		l = l.replace(', ', ';;')
		l = l.replace('\N', '')
		l = l.split(',')
		
		for i in range(len(l)):
			l[i] = l[i].replace(';;', ', ')
		
		res.append(l)
	return res

def split_author(l_author):
	res = {}
	for a in l_author:
		paper_key = a[0]
		position_author = a[1]
		name_author = a[2]
		
		res[(paper_key, name_author)] = position_author
		
	return res

def split_conferences(l_conferences):
	res = {}
	for c in l_conferences:
		global_key = c[0]
		conf_key = c[1]
		year = c[2]
		publisher = c[3]
		title = c[4]
		link = c[5]
		domain_1 = c[6]
		domain_2 = c[7]
		domain_3 = c[8]
		domain_4 = c[9]
		
		res[(global_key, conf_key)] = (year, publisher, title, link, domain_1, domain_2, domain_3, domain_4)
		
	return res

def aux(x):
	r = 0
	if x != "":
		r = 1
	return r

def split_ethnicity(et):
	res = {}
	for e in et:
		name = e[0]
		l0 = e[1]
		l1=e[2]
		l2=e[3]
		
		l0 = aux(l0)
		l1 = aux(l1)
		l2 = aux(l2)

		gender = e[4]
		if (gender == '\"-\"'): gender = ''
		
		res[name] = (l0,l1,l2,gender)
	return res

def split_papers(papers):
	res = {}
	for p in papers:
		global_key = p[0]
		paper_key = p[1]
		conf_key = p[2]
		link = p[3]
		title = p[4]
		pages = p[5]
		citations = p[6]
		
		res[paper_key] = (global_key, conf_key, link, title, pages, citations)
	return res


tab_join = []

f_author = "tabs/authors.csv"
f_conferences = "tabs/conferences.csv"
f_ethnicity = "tabs/ethnicity.csv"
f_papers = "tabs/papers.csv"

l_author = load_tab(f_author)
authors = split_author(l_author)
l_conferences = load_tab(f_conferences)
conferences = split_conferences(l_conferences)
l_ethnicity = load_tab(f_ethnicity)
ethnicity = split_ethnicity(l_ethnicity)
l_papers = load_tab(f_papers)
papers = split_papers(l_papers)

res = []
f_out = open('out.csv', 'w')
f_out.write('paper_key,l2,gender,global_key,conf_key,domain_1,domain_2,domain_3,domain_4\n')
for a in authors:
	et = (0,0,0,0)
	if (a[1] in ethnicity): et = ethnicity[a[1]]
	if (a[0] in papers):
		p = papers[a[0]]
		global_key = papers[a[0]][0]
		conf_key = papers[a[0]][1]
		c = conferences[(global_key, conf_key)]
		if (et[3] == ""):
			print "sem sexo"
			continue		
		f_out.write('%s,%s,%s,%s,%s,%s,%s,%s,%s\n' % (a[0],et[2], et[3], p[0],p[1], c[4], c[5], c[6], c[7]) )

f_out.close()			
	




'''
Authors table consists of 3 attributes: paper key, position of author (1st, 2nd,...nth author) and the full name appeared in the dblp records (including the padding bits 0001, 0002 etc)

Conferences table consists of 10 attributes: global_key (name of the conf), conf_key (specific to the year), year, publisher (ACM/springer/ieee etc), title, link (url to the conference website), and cs | de | se | th (domain of the conference- Computer Science, Data Engineering, Software Engineering and Theory)

Ethnicity table consists of 5 attributes: name (name of the author), l0, l1, and l2 (ethnicity levels ) and gender

Papers table consists of 7 attributes: global_key (key of the conference), paper_key (dblp key of the paper), conf_key , link (doi link to the digital library). title, pages, and citations

Perguntas elaboradas:

1- Qual a conferência que mais tem artigos publicados?

2- Qual autor (primeiro autor) que mais publicou artigos?

3-Qual a conferência que mais tem artigos publicados por autores com o grau de etnia 2?

4- Qual o nível de etnia dos autores que mais publicam?

5-Qual o autor que mais publica em conferências da Engenharia de Software?

6-Qual o domínio da conferência que mais tem artigos publicados?

7-Qual o gênero dos autores que mais publicam artigos científicos, homens ou mulheres?

 

Perguntas Escolhidas:

1- Qual a conferência que mais tem artigos publicados?

3-Qual a conferência que mais tem artigos publicados por autores com o grau de etnia 2?

6-Qual o domínio da conferência que mais tem artigos publicados?

7-Qual o gênero dos autores que mais publicam artigos científicos, homens ou mulheres?
'''

