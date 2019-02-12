import codecs
import os
import config
import pixiv_account
from pixivpy3 import *
from time import sleep
import time
import file_controller
import output
import core4pixivpy


def input_and_setting_config(config_file,config_dim_name:str,config_line_num:int,help_str):
    print("\n"+help_str)
    print( config_dim_name + " : " + eval( "%s.%s" % (config_file,config_dim_name) ) )
    temp = input("\t>> ")
    if temp != "":    
        file_list[config_line_num] = "%s:str = \"" % config_dim_name + temp + "\""


def setting_config_file():
    output.setting_config_menu()
    file_list = file_controller.input_file(os.getcwd() + "\\config.py")
    try:
        input_and_setting_config("config","current_dir",0,"(full path) current directory as save picture")
        input_and_setting_config("config","file_list_csv",1,"(full path) file path as put illust list file")
        input_and_setting_config("config","illustrator_csv",2,"(full path) file path is crawl target illustrator list file")
        print("\nrewrite config file...")
        file_controller.output_file(file_list,os.getcwd() + "\\config.py")
        print("\nSuccess rewrite config file!")
    except:
        print("\nERROR!\nsorry DON'T CHANGE config file")
    del file_list


def setting_pixiv():
    output.setting_config_menu()
    if os.path.isfile( os.getcwd() + "\\pixiv_account.py" ):
        file_list = file_controller.input_file(os.getcwd() +"\\pixiv_account.py")
    else:
        file_list = []
    try:
        input_and_setting_config("pixiv_account","pixiv_id",0,"pixiv account id")
        input_and_setting_config("pixiv_account","password",1,"pixiv account password")
        input_and_setting_config("pixiv_account","user_id",2,"pixiv account user id")
        print("\nrewrite config file...")
        file_controller.output_file(file_list,os.getcwd() + "\\pixiv_account.py")
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
            start = time.time()
            saving_direcory_path = config.current_dir + "\\" + illustrator[1] + "\\"
            if not os.path.exists(saving_direcory_path):
                os.mkdir(saving_direcory_path)
            core4pixivpy.get_illust_main(file_list,int(illustrator[0]),pixiv_account.pixiv_id,pixiv_account.password,saving_direcory_path,config.get_manga_page_time,config.get_illust_time,config.illustid_interval)
            elapsed_time = time.time() - start
        except:
            output.print_prosess(illustrator[1],"ERROR")
            sleep(config.sleep_exception)
        output.print_prosess(illustrator[1],"Finish")
        if float(elapsed_time) < config.illustrator_buttom_sec:
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