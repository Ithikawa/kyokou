import codecs
import setting
import get_illust

print(
"""
kyokou version 1.0.4
Copyright (C) 2018 by Asahi Ithikawa(@ichikawa_ykhm)
"""
)
temp = 1
while temp != 0:
    print(
"""
<< CENTRAL MENU >>
  1.Setting config file
  2.Setting login pixiv account
  3.Getting illust script

  9.READ ME
  0.EXIT
"""
    )
    del temp
    temp = input(">> ")
    if temp == "1":
        setting.config()
    elif temp == "2":
        setting.pixiv()
    elif temp == "3":
        get_illust.main()
    elif temp == "9":
        f = codecs.open("files\\readme.txt","r","utf-8")
        readme = f.read().split("\r\n")
        f.close()
        print("\n-----------------------------------------------------------------------------------\n")
        for i in readme:
            print(i)
        del readme
        print("\n-----------------------------------------------------------------------------------\n")
    elif temp == "0":
        print("See you again!")
        break
    elif temp == "":
        print("prease any key")
    else:
        print(
"""
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
