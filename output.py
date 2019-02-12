import datetime
import re
import codecs
import config

def print_prosess(status):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\t" + status)
    f = codecs.open(config.log_file,"a","utf-8")
    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\t" + status + "\r\n")
    f.close()

def print_response(illustrator_name, status):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\t" + status + "\t" + illustrator_name)
    f = codecs.open(config.log_file,"a","utf-8")
    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\t" + status + "\t" + illustrator_name + "\r\n")
    f.close()

def file_list_replase(file_path):
    file_info = import_file_and_sprit(file_path)

    file_list = []
    for line in file_info:
        if line != "":
            file_list.append( int (re.sub("_p\d+.(jpg|png|jpeg|gif)$", "", line) ) )
    file_list = list(set(file_list))
    del file_info
    return file_list

def illustrator_list_replase(file_path):
    illustrator_info = import_file_and_sprit(file_path)

    illustrator_list = []
    for line in illustrator_info:
        if line != "":
            illustrator_list.append(line.split(","))
    del illustrator_info
    return illustrator_list

def import_file_and_sprit(file_path):
    f = codecs.open(file_path,"r","utf-8")
    file_info = f.read().split("\r\n")
    f.close()
    return file_info
    