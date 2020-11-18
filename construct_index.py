import os
import stopwords
from lxml import html,etree
from io import StringIO
from nltk.tokenize import RegexpTokenizer
import store_extract_data
from collections import Counter
import document_structure
import codecs
import re

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

def find_terms(content, tokenizer,file_id, dictionary):
	tokenized_words = dict()
	for element in content.iter("body", "strong", "title", "h1", "h2", "h3"):
		# body = 1, strong =2, title =3,  h1h2h3 =4
		if element.text != None:
			for term in tokenizer.tokenize(element.text):
				if term.lower() not in stopwords.stopwords:
					if term.lower() not in tokenized_words:
						if element.tag == "body":
							tokenized_words[term.lower()] = {1:1, 2:0, 3:0, 4:0, 'freq':1}
						elif element.tag == "strong":
							tokenized_words[term.lower()] = {1:0, 2:1, 3:0, 4:0, 'freq':1}
						elif element.tag == "title":
							tokenized_words[term.lower()] = {1:0, 2:0, 3:1, 4:0, 'freq':1}
						else:
							tokenized_words[term.lower()] = {1:0, 2:0, 3:0, 4:1, 'freq':1}
					else:
						if element.tag == "body":
							tokenized_words[term.lower()][1] += 1
							tokenized_words[term.lower()]['freq'] +=1 
						elif element.tag == "strong":
							tokenized_words[term.lower()][2] += 1
							tokenized_words[term.lower()]['freq'] +=1 
						elif element.tag == "title":
							tokenized_words[term.lower()][3] += 1
							tokenized_words[term.lower()]['freq'] +=1 
						else:
							tokenized_words[term.lower()][4] += 1
							tokenized_words[term.lower()]['freq'] +=1 


	for k in tokenized_words:
		if k not in dictionary:
			dictionary[k] = {'total_freq': 0, 'Documents':[]}
		if len(dictionary[k]['Documents']) == 0 or dictionary[k]['Documents'][-1].docID != file_id:
			doc_obj = document_structure.Document(file_id)
			doc_obj.word_freq += tokenized_words[k]['freq']
			doc_obj.body += tokenized_words[k][1]
			doc_obj.strong += tokenized_words[k][2]
			doc_obj.title += tokenized_words[k][3]
			doc_obj.h += tokenized_words[k][4]
			dictionary[k]['Documents'].append(doc_obj)
			dictionary[k]['total_freq'] += tokenized_words[k]['freq']
		else:
			dictionary[k]['Documents'][-1].word_freq += tokenized_words[k]['freq']
			dictionary[k]['Documents'][-1].body += tokenized_words[k][1]
			dictionary[k]['Documents'][-1].strong += tokenized_words[k][2]
			dictionary[k]['Documents'][-1].title += tokenized_words[k][3]
			dictionary[k]['Documents'][-1].h += tokenized_words[k][4]
			dictionary[k]['total_freq'] += tokenized_words[k]['freq']
	


def indexlize():
	# counter = 0
	dic = dict() #store index
	for (root, dirs, files) in os.walk("./WEBPAGES_RAW"):
		if len(files) != 0:  
			for filename in files:
				file_location = os.path.join(root, filename)
				try:
					# with open(file_location) as file:
					with codecs.open(file_location, encoding='utf-8', errors='ignore') as file:
						first_line = file.readline()# skip the first line of code
						''' some files contain "<?xml version="1.0" encoding="UTF-8"?>" in their first lines. This line of code will rasie exception becasue etree can't handle it.

						'''
						while(first_line == '\n' or first_line == '\r\n'):
							first_line = file.readline()
						content = file.read()
						parser = etree.HTMLParser()
						tree = etree.parse(StringIO(content), parser)
						tokenizer = RegexpTokenizer(r'\w+')
						file_location = file_location[15:]
						# file_location = file_location[7:]
						find_terms(tree, tokenizer, file_location, dic)
						# counter += 1
				except ValueError as e:
					print "File_Location: {}".format(file_location)
					print e


	store_extract_data.store_index(dic, "./picklefile/", "inverted_index_all_20")
	# print dic
	# for i in dic:
	# 	print i.encode('utf-8')
	# 	print dic[i]['total_freq']
	# 	print "**********"
	# 	for j in dic[i]['Documents']:
	# 		print j
	# 	print "**********"




if __name__ == '__main__':
	indexlize()
	