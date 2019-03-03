import codecs
import os
import config
from pixivpy3 import *
from time import sleep
import time
import file_controller
import output
import core4pixivpy


def input_and_setting_config(file_list,config_file,config_dim_name:str,config_dim_char:str,config_line_num:int,help_str):
    print("\n"+help_str)
    print( config_dim_name + " : " + str(eval( "%s.%s" % (config_file,config_dim_name) ) ) )
    temp = input("\t>> ")
    if temp != "":    
        file_list[config_line_num] = "%s:%s = \"" %(config_dim_name,config_dim_char) + temp + "\""
    return file_list


def setting_config_file():
    output.setting_config_menu()
    file_list = file_controller.input_file(os.getcwd() + "\\config.py")
    try:
        file_list = input_and_setting_config(file_list,"config","current_dir","str",0,"(full path) current directory as save picture")
        file_list = input_and_setting_config(file_list,"config","file_list_csv","str",1,"(full path) file path as put illust list file")
        file_list = input_and_setting_config(file_list,"config","illustrator_csv","str",2,"(full path) file path is crawl target illustrator list file")
        file_list = input_and_setting_config(file_list,"config","log_file",3,"str","(full path) file path as log file")
        file_list = input_and_setting_config(file_list,"config","sleep_exception","float",4,"sec")
        file_list = input_and_setting_config(file_list,"config","illustrator_buttom_sec","float",5,"sec")
        file_list = input_and_setting_config(file_list,"config","illustrator_interval","float",6,"sec")
        file_list = input_and_setting_config(file_list,"config","illustid_interval","float",7,"sec")
        file_list = input_and_setting_config(file_list,"config","get_illust_time","float",8,"sec")
        file_list = input_and_setting_config(file_list,"config","get_manga_page_time","float",9,"sec")
        
        print("\nrewrite config file...")
        file_controller.output_file(file_list,os.getcwd() + "\\config.py")
        print("\nSuccess rewrite config file!")
    except:
        print("\nERROR!\nsorry DON'T CHANGE config file")
    del file_list


def setting_pixiv():
    output.setting_config_menu()
    file_list = file_controller.input_file(os.getcwd() +"\\config.py")
    try:
        file_list = input_and_setting_config(file_list,"config","pixiv_id","str",10,"pixiv account id")
        file_list = input_and_setting_config(file_list,"config","password","str",11,"pixiv account password")
        file_list = input_and_setting_config(file_list,"config","user_id","str",12,"pixiv account user id")
        print("\nrewrite config file...")
        file_controller.output_file(file_list,os.getcwd() + "\\config.py")
        print("\nSuccess rewrite config file!")
    except:
        print("\nERROR!\nsorry DON'T CHANGE config file")
    del file_list


def get_illust():
    print("Getting illust script")
    output.print_prosess("START PROGRAM")
    file_controller.file_replase()
    file_controller.illustrator_list_replase()
    api = PixivAPI()
    file_list = file_controller.get_file_list(config.file_list_csv)
    illustrator_list = file_controller.get_illustrator_list(config.illustrator_csv)
    output.print_prosess("Start Prosess")

    # 入力されたuserIDからイラストレーターの情報を取得
    for illustrator in illustrator_list:
        try:
            output.print_prosess( illustrator[1], "Start" )
            saving_direcory_path = config.current_dir +  illustrator[1] + "\\"
            if not os.path.exists(saving_direcory_path):
                os.mkdir(saving_direcory_path)
            core4pixivpy.get_illust_main(file_list,int(illustrator[0]),config.pixiv_id,config.password,saving_direcory_path,config.get_manga_page_time,config.get_illust_time,config.illustid_interval)
        except:
            output.print_prosess(illustrator[1],"ERROR")
            sleep(config.sleep_exception)
        output.print_prosess(illustrator[1],"Finish")
        sleep(config.illustrator_interval)
    del file_list
    del illustrator_list
    output.print_prosess("End Prosess")


def exit_menu():
    print("See you again!")


def not_intger():
    print("prease any key")


if __name__ == '__main__':
    output.top_title()
    temp = 1
    while temp != 0:
        output.controle_pannel()
        del temp
        temp = input(">> ")
        if temp == "1":
            setting_config_file()
        elif temp == "2":
            setting_pixiv()
        elif temp == "3":
            get_illust()
        elif temp == "9":
            output.read_me()
        elif temp == "0":
            exit_menu()
            break
        elif temp == "":
            not_intger()
        else:
            output.others()