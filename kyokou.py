import codecs
import os
import config
import pixiv_account
import sys
from pixivpy3 import *
from time import sleep
import time
import file_replase
import output
import core4pixivpy

def top_title():
    print("""
kyokou version 1.0.4
Copyright (C) 2018 by Asahi Ithikawa(@ichikawa_ykhm)""")

def controle_pannel():
    print("""
    << CENTRAL MENU >>
    1.Setting config file
    2.Setting login pixiv account
    3.Getting illust script

    9.READ ME
    0.EXIT""")

def setting_config_file():
    print("""
|| |  |   -=<( setthing config )>=-   |  | ||

key : current value
    >> < input new value >
< Notice >
    if you not input any sentence. not rewrite that value. 
    
- key name -     | - role -
current dir      | (full path) current directory as save picture
illust list path | (full path) file path as put illust list file
illustrator list | (full path) file path is crawl target illustrator list file""")
    f = codecs.open( os.getcwd() + "\\config.py", "r", "utf-8" )
    file_list = f.read().split("\r\n")
    f.close()
    bak_file_list = file_list
    print(file_list)

    try:
        print("- current value -")
        print("current dir : " + config.current_dir)
        temp = input("\t>> ")
        if temp != "":    
            file_list[0] = "current_dir = \"" + temp + "\"" 

        print("\nillust list path : " + config.file_list_csv)
        temp = input("\t>> ")
        if temp != "":    
            file_list[1] = "file_list_csv = \"" + temp + "\"" 

        print("\nillustrator list : " + config.illustrator_csv)
        temp = input("\t>> ")
        if temp != "":    
            file_list[2] = "illustrator_csv = \"" + temp + "\"" 

        print("\nreplase config file...")
        f = codecs.open( os.getcwd() + "\\config.py", "w", "utf-8" )
        for i in file_list:
            f.write( i + "\r\n" )
        f.close()
        print("\nSuccess rewrite config file!")
    except:
        file_list = bak_file_list
        print("\nERROR!\nsorry DON'T CHANGE config file")
    del file_list

def setting_pixiv():
    print("""
|| |  |   -=<( pixiv account )>=-   |  | ||

key : current value
    >> < input new value >
< Notice >
    if you not input any sentence. not rewrite that value. 
    
- key name -     | - role -
    pixiv id     |     that account id
    password     |     that account password
    user id      |     that account user id""")
    
    if os.path.isfile( os.getcwd() + "\\pixiv_account.py" ):
        f = codecs.open( os.getcwd() +"\\pixiv_account.py", "r", "utf-8" )
        file_list = f.read().split("\r\n")
        f.close()
        bak_file_list = file_list
    else:
        file_list = []

    try:
        print("\npixiv account")
        print("pixiv id : " + pixiv_account.pixiv_id)
        temp = input("\t>> ")
        if temp != "":    
            file_list[0] = "pixiv_id = \"" + temp + "\"," 

        print("password : " + pixiv_account.password)
        temp = input("\t>> ")
        if temp != "":    
            file_list[1] = "password = \"" + temp + "\"," 
        
        print("user id : " + pixiv_account.user_id)
        temp = input("\t>> ")
        if temp != "":    
            file_list[2] = "user_id = \"" + temp + "\"" 

        print("\nreplase config file...")
        f = codecs.open( os.getcwd() + "\\pixiv_account.py", "w", "utf-8" )
        for i in file_list:
            f.write( i + "\r\n" )
        f.close()
        print("\nSuccess rewrite config file!")
    except:
        file_list = bak_file_list
        print("\nERROR!\nsorry DON'T CHANGE config file")
    del file_list

def get_illust():
    print("Getting illust script")
    output.print_prosess("START PROGRAM")
    file_replase.file_replase()
    file_replase.illustrator_list_replase()
    api = PixivAPI()
    file_list = output.file_list_replase(config.file_list_csv)
    illustrator_list = output.illustrator_list_replase(config.illustrator_csv)
    output.print_prosess("Start Prosess")

    # 入力されたuserIDからイラストレーターの情報を取得
    for illustrator in illustrator_list:
        try:
            output.print_response( illustrator[1], "Start" )
            start = time.time()
            saving_direcory_path = config.current_dir + "\\" + illustrator[1] + "\\"
            if not os.path.exists(saving_direcory_path):
                os.mkdir(saving_direcory_path)
            core4pixivpy.get_illust_main(file_list,int(illustrator[0]),pixiv_account.pixiv_id,pixiv_account.password,saving_direcory_path,config.get_manga_page_time,config.get_illust_time,config.illustid_interval)
            elapsed_time = time.time() - start
        except:
            output.print_response(illustrator[1],"ERROR")
            print(e)
            sleep(config.sleep_exception)
        output.print_response(illustrator[1],"Finish")
        if float(elapsed_time) < config.illustrator_buttom_sec:
            sleep(config.illustrator_interval)
    del file_list
    del illustrator_list
    output.print_prosess("End Prosess")

def read_me():
    f = codecs.open("files\\readme.txt","r","utf-8")
    readme = f.read().split("\r\n")
    f.close()
    print("\n-----------------------------------------------------------------------------------\n")
    for i in readme:
        print(i)
    del readme
    print("\n-----------------------------------------------------------------------------------\n")

def exit_menu():
    print("See you again!")

def not_intger():
    print("prease any key")

def others():
    print("""
　　　　　　 　　＿　　＿_
　　　　　　_／　　｀/　 　　￣ヽ、
　 　　 _／　　　　　　　　　　　　ヽ
　　／／　　,　　　　　 ､ ､ ､ ヽヽ. .!
　/ /|　/　// |　| |　| | | |　|　| | | |
　|/　|　|　|_|ノ|　| |ヽ!⊥|_|　|　| | | |
　 　 Ｗレﾚ, ､V V　,⊥_ ､l､ V|/ﾚ'　|
　 　　 | |　|| .}　 　　|.　j｀| 　| 　 | | | . 　 ／￣￣￣￣￣￣￣￣￣
　 　　 | |　!￣'、　　 ￣　| 　|　　| | |　＜　そんなこと言う人、嫌いです
　 　 　 | |　＼　 　 　　 ,.| 　!　　| | .|　　 ＼＿＿＿＿＿＿＿＿＿
　 　　 ヽ | 　 /｀　 Ｔ　　/　/　 /ﾚﾚ′
　 　 　　ヽ|,,/　 ,-|Т￣/,〃´´ヽ、
　　　　　 　／￣/7￣ヽ、　 　 　 ヽ
　 　　　　/　 //｀´|　 　 ヽ 　　　　 |        
"""
    )

if __name__ == '__main__':
    top_title
    temp = 1
    while temp != 0:
        controle_pannel()
        del temp
        temp = input(">> ")
        if temp == "1":
            setting_config_file()
        elif temp == "2":
            setting_pixiv()
        elif temp == "3":
            get_illust()
        elif temp == "9":
            read_me()
        elif temp == "0":
            exit_menu()
            break
        elif temp == "":
            not_intger()
        else:
            others()