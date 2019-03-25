import os

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

dir_path = os.path.dirname(os.path.realpath('__file__'))

def label(cate):
    return {
        'business': 0,
        'entertainment': 1,
        'health': 2,
        'sport': 3
    }.get(cate, 4)

listFolder = ['business', 'entertainment', 'health', 'sport']

def count_number_of_files(cate):
    return len(next(os.walk("{}\\{}".format(dir_path, cate)))[2])

def get_all_filelists():
    file_list = []
    for cate in listFolder:
        num_of_files = count_number_of_files(cate)
        file_list.extend([dir_path + "\\" + cate + "\\" + str(i) + ".txt" for i in range(0, num_of_files - 1)])
    return file_list

def exportTFIDF():
    filelist = get_all_filelists()
    tf_idf =  TfidfVectorizer(input="filename").fit_transform(filelist).toarray()
    return tf_idf

def label_tf_idf():
    tf_idf = exportTFIDF()
    lb = [[]]
    for cate in listFolder:
        num_of_files = count_number_of_files(cate)
        label_num = label(cate)
        label_matrix = np.full((1, num_of_files - 1), label_num, dtype=int)
        lb = np.append(lb, label_matrix, axis=1)
    tf_idf =  np.append(tf_idf, np.matrix.transpose(lb), axis=1)
    np.savetxt('tf_idf.csv',tf_idf,fmt='%.5f', delimiter=',')

label_tf_idf()
