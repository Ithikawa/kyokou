import re
import codecs
import config
import output
import glob

def output_file(output_list,file_path):
    f = codecs.open( file_path, 'w', "utf-8" )
    for temp_line in output_list:
        f.write( temp_line + "\r\n" )
    f.close()


def input_file(file_path):
    f = codecs.open(file_path,"r","utf-8")
    file_info = f.read().split("\r\n")
    f.close()
    return file_info


def file_replase():
    output.print_prosess("file_replase","getting...")
    file_info= glob.glob(config.current_dir + "**", recursive=True)
    file_list = []
    data_list = []
    for i in file_info:
        file_list = i.split("\\")
        for j in file_list: 
            if re.match("^\d+_p\d+.(jpg|png|jpeg|gif)$", j):
                data_list.append(j)
    del file_info
    output_file(data_list, config.file_list_csv)
    output.print_prosess("file_replase","\tsuccess!")
    del data_list


def illustrator_list_replase():
    output.print_prosess("illustrator_list_replase","getting...")
    file_list = input_file(config.illustrator_csv)
    file_list = list(set(file_list))
    output_file(file_list, config.illustrator_csv)
    output.print_prosess("illustrator_list_replase","\tsuccess!")
    del file_list
    

def import_file_and_sprit(file_path,func_str):
    file_info = input_file(file_path)
    file_list = []
    for line in file_info:
        if line != "":
            file_list.append(eval( func_str ) )
    return file_list


def get_file_list(file_path):
    file_list = import_file_and_sprit(file_path , "int(re.sub(\"_p\\d+.(jpg|png|jpeg|gif)$\", \"\", line))")
    file_list = list(set(file_list))
    return file_list


def get_illustrator_list(file_path):
    illustrator_list = import_file_and_sprit(file_path,"line.split(\",\")")
    return illustrator_list
