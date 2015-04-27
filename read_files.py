# __author__ = 'Erin'

import pandas

def read_files(file_names):
    train = pandas.read_csv(file_names, header=0, delimiter="\t", quoting=3)
    return train

def read_by_line(file_names):
    file = open(file_names)
    datalist=[]
    while 1:
        lines = file.readlines()
        if not lines:
            break
        for line in lines:
            line=line.replace("\n","")
            datalist.append(line)
    return datalist