import store_extract_data
import stopwords
import math
from collections import Counter



def retrive(user_input):
    # result_lst = dict()
    # N = 37497
    # index = store_extract_data.extract_index("./picklefile/inverted_index_all_10.pickle")
    # #user_input = "irvine"
    # user_input = user_input.split()
    # for query in user_input:
    #     if query not in stopwords.stopwords:
    #         for doc in index[query]['Documents']:
    #             itf_idf = 1 + math.log(doc.word_freq)
    #             itf_idf += math.log(N/len(index[query]['Documents']))
    #             itf_idf += (doc.title*1.5 + doc.h*1 + doc.body*2.5 + doc.strong*2)
    #             if doc.docID in result_lst:
    #                 result_lst[doc.docID] += itf_idf
    #             else:
    #                 result_lst[doc.docID] = itf_idf
    # result_lst = sorted(result_lst.items(), key=lambda kv: kv[1])
    # with open('test_results.txt', mode='w') as f:
    #     f.write(result_lst.__repr__())
    # return result_lst
################################################    
 #    	result_lst = dict()
	# query_count = None
	# N = 37497
	# query_vector = dict()
	# norm_query_vector = dict()
	# doc_vectors = dict()
	# norm_doc_vector = dict()
	# index = store_extract_data.extract_index("./picklefile/inverted_index_all_20.pickle")
	# # user_input = "irvine student"
	# user_input = user_input.split()
	# query_count = Counter(user_input) # becomes a dictionary
	# for k in query_count.keys():
	# 	if (k in stopwords.stopwords) or (k not in index):
	# 		del query_count[k]
	# if len(query_count) > 1:
	# 	for query in query_count:
	# 		q_itf_idf = 1 + math.log(query_count[query], 10)
	# 		q_itf_idf =  q_itf_idf * math.log((N), 10)
	# 		query_vector[query] = q_itf_idf
	# 	magnitute = math.sqrt(sum([i[1]**2 for i in query_vector.items()]))
	# 	# print query_vector
	# 	for query in query_vector:
	# 		norm_query_vector[query] = query_vector[query]/magnitute
	# 	# print norm_query_vector

	# 	for query in norm_query_vector:
	# 		for doc in index[query]['Documents']:
	# 			itf_idf = 1 + math.log(doc.word_freq, 10)
	# 			itf_idf = itf_idf * math.log(N/len(index[query]['Documents']), 10)
	# 			if doc.docID in doc_vectors:
	# 				doc_vectors[doc.docID][query] = itf_idf
	# 			else:
	# 				doc_vectors[doc.docID] = dict()
	# 				doc_vectors[doc.docID][query] = itf_idf
	# 	for docid in doc_vectors:
	# 		magnitute = math.sqrt(sum([i[1]**2 for i in doc_vectors[docid].items()]))

	# 		norm_doc_vector[docid] = dict()
	# 		for i in doc_vectors[docid]:
	# 			norm_doc_vector[docid][i] = (doc_vectors[docid][i]/magnitute)
	# 	# print query_vector
	# 	# print norm_query_vector
	# 	# print doc_vectors
	# 	# print norm_doc_vector
	# 	for docid in norm_doc_vector:
	# 		score = 0
	# 		for query in norm_query_vector:
	# 			if query not in norm_doc_vector[docid]:
	# 				score += 0
	# 			else:
	# 				score += norm_query_vector[query] * norm_doc_vector[docid][query]
	# 		result_lst[docid] = score
	# 	result_lst = sorted(result_lst.items(), key=lambda kv: kv[1], reverse= True)
	# 	# print result_lst
	# 	return result_lst
	# elif len(query_count) == 1:
	# 	for query in query_count.keys():
	# 		for doc in index[query]['Documents']:
	# 			itf_idf = 1 + math.log(doc.word_freq, 10)
	# 			itf_idf = itf_idf * math.log(N/len(index[query]['Documents']), 10)
	# 			itf_idf += (doc.title*1.5 + doc.h*1 + doc.body*2.5 + doc.strong*2)
	# 			if doc.docID in result_lst:
	# 				result_lst[doc.docID] += itf_idf
	# 			else:
	# 				result_lst[doc.docID] = itf_idf
	# 	result_lst = sorted(result_lst.items(), key=lambda kv: kv[1], reverse= True)
	# 	return result_lst
##################################################
    	result_lst = dict()
	query_count = None
	N = 37497
	query_vector = dict()
	norm_query_vector = dict()
	doc_vectors = dict()
	norm_doc_vector = dict()
	index = store_extract_data.extract_index("./picklefile/inverted_index_all_20.pickle")
	# user_input = "irvine student"
	user_input = user_input.split()
	user_input = [i.lower() for i in user_input]
	query_count = Counter(user_input) # becomes a dictionary
	for k in query_count.keys():
		if (k in stopwords.stopwords) or (k not in index):
			del query_count[k]
	if len(query_count) > 1:
		for query in query_count.keys():
			q_itf_idf = 1 + math.log(query_count[query], 10)
			q_itf_idf =  q_itf_idf * math.log((N), 10)
			query_vector[query] = q_itf_idf
		magnitute = math.sqrt(sum([i[1]**2 for i in query_vector.items()]))
		# print query_vector
		for query in query_vector.keys():
			norm_query_vector[query] = query_vector[query]/magnitute
		# print norm_query_vector

		for query in norm_query_vector.keys():
			for doc in index[query]['Documents']:
				itf_idf = 1 + math.log(doc.word_freq, 10)
				itf_idf = itf_idf * math.log(N/len(index[query]['Documents']), 10)
				if doc.docID in doc_vectors:
					doc_vectors[doc.docID][query] = itf_idf
				else:
					doc_vectors[doc.docID] = dict()
					doc_vectors[doc.docID][query] = itf_idf
		for docid in doc_vectors.keys():
			magnitute = math.sqrt(sum([i[1]**2 for i in doc_vectors[docid].items()]))

			norm_doc_vector[docid] = dict()
			for i in doc_vectors[docid].keys():
				norm_doc_vector[docid][i] = (doc_vectors[docid][i]/magnitute)
		# print query_vector
		# print norm_query_vector
		# print doc_vectors
		# print norm_doc_vector
		for docid in norm_doc_vector.keys():
			score = 0
			for query in norm_query_vector.keys():
				if query not in norm_doc_vector[docid].keys():
					score += 0
				else:
					score += norm_query_vector[query] * norm_doc_vector[docid][query]
			result_lst[docid] = score
		result_lst = sorted(result_lst.items(), key=lambda kv: kv[1], reverse= True)
		# print result_lst
		return result_lst
	elif len(query_count) == 1:
		for query in query_count.keys():
			for doc in index[query]['Documents']:
				itf_idf = 1 + math.log(doc.word_freq, 10)
				itf_idf = itf_idf * math.log(N/len(index[query]['Documents']), 10)
				itf_idf += (doc.title*1.5 + doc.h*1 + doc.body*2.5 + doc.strong*2)
				if doc.docID in result_lst.keys():
					result_lst[doc.docID] += itf_idf
				else:
					result_lst[doc.docID] = itf_idf
		result_lst = sorted(result_lst.items(), key=lambda kv: kv[1], reverse= True)
		return result_lst
	else:
		return dict()


if __name__ == '__main__':
    retrive('irvine')
    # test()
