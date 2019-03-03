import datetime
import re
import codecs
import config
import file_controller

def top_title():
    print("""kyokou version 1.0.9
Copyright (C) 2018 by Asahi Ithikawa(@ichikawa_ykhm)""")


def controle_pannel():
    print("""
    << CENTRAL MENU >>
    1.Setting config file
    2.Setting login pixiv account
    3.Getting illust script

    9.READ ME
    0.EXIT""")


def setting_config_menu():
    print("""key : current value
    >> < input new value >
< Notice >
    if you not input any sentence. not rewrite that value. """)


def read_me():
    readme = file_controller.input_file("files\\readme.txt")
    print("\n-----------------------------------------------------------------------------------\n")
    for i in readme:
        print(i)
    del readme
    print("\n-----------------------------------------------------------------------------------\n")


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
　 　　　　/　 //｀´|　 　 ヽ 　　　　 |""")


def print_prosess(status,notice = ""):
    print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\t" + status + "\t" + notice)
    f = codecs.open(config.log_file,"a","utf-8")
    f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\t" + status + "\t" + notice + "\r\n")
    f.close()
    