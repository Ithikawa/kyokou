import codecs
import os

from config import config
from config import pixiv_account

def config():
    print("""
|| |  |   -=<( setthing config )>=-   |  | ||

key : current value
    >> < input new value >
< Notice >
    if you not input any sentence. not rewrite that value. 
    
- key name -     | - role -
current dir      | (full path) current directory as save picture
illust list path | (full path) file path as put illust list file
illustrator list | (full path) file path is crawl target illustrator list file
    """)
    f = codecs.open("config\\config.py","r","utf-8")
    file_list = f.read().split("\r\n")
    f.close()
    bak_file_list = file_list

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
        f = codecs.open(".\\config.py", "w","utf-8")
        for i in file_list:
            f.write( i + "\r\n" )
        f.close()
        print("\nSuccess rewrite config file!")
    except:
        file_list = bak_file_list
        print("\nERROR!\nsorry DON'T CHANGE config file")
    del file_list

def pixiv():
    print("""
|| |  |   -=<( pixiv account )>=-   |  | ||

key : current value
    >> < input new value >
< Notice >
    if you not input any sentence. not rewrite that value. 
    
- key name -     | - role -
    pixiv id     |     that account id
    password     |     that account password
    user id      |     that account user id
    """)
    
    if os.path.isfile("config\\pixiv_account.py"):
        f = codecs.open("config\\pixiv_account.py","r","utf-8")
        file_list = f.read().split("\r\n")
        f.close()
        bak_file_list = file_list
    else:
        file_list = []

    try:
        print("\npixiv account")
        print("pixiv id : " + config.pixiv_account["pixiv_id"])
        temp = input("\t>> ")
        if temp != "":    
            file_list[0] = "pixiv_id = \"" + temp + "\"," 

        print("password : " + config.pixiv_account["password"])
        temp = input("\t>> ")
        if temp != "":    
            file_list[1] = "password = \"" + temp + "\"," 
        
        print("user id : " + config.pixiv_account["user_id"])
        temp = input("\t>> ")
        if temp != "":    
            file_list[2] = "user_id = \"" + temp + "\"" 

        print("\nreplase config file...")
        f = codecs.open(".\\pixiv_account.py", "w","utf-8")
        for i in file_list:
            f.write( i + "\r\n" )
        f.close()
        print("\nSuccess rewrite config file!")
    except:
        file_list = bak_file_list
        print("\nERROR!\nsorry DON'T CHANGE config file")
    del file_list
