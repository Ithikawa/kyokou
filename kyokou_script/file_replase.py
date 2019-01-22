import re
import codecs
import config
import glob

def file_replase():
    print("\tgetting file path trom current dir...")
    file_info= glob.glob(config.current_dir + "**", recursive=True)
    print("\t\tsuccess!")
    
    print("\treplase file list...")
    file_list = []
    data_list = []
    for i in file_info:
        file_list = i.split("\\")
        for j in file_list: 
            if re.match("^\d+_p\d+.(jpg|png|jpeg|gif)$", j):
                data_list.append(j)
    del file_info
    print("\t\tsuccess!")

    print("\toutput file list...")
    f = codecs.open(config.file_list_csv, 'w',"utf-8")
    for i in data_list:
        f.write(i + "\r\n")
    f.close()
    print("\t\tsuccess!")
    del data_list

def illustrator_list_replase():
    print("\treplase illustrator list...")
    f = codecs.open(config.illustrator_csv,"r","utf-8")
    file_list = f.read().split("\r\n")
    f.close()
    file_list = list(set(file_list))

    f = codecs.open(config.illustrator_csv, "w","utf-8")
    for i in file_list:
        f.write( i + "\r\n" )
    f.close()
    print("\t\tsuccess!")
    del file_list
    