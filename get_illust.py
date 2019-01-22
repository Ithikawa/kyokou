# -*- coding: utf-8 -*-
import sys
from pixivpy3 import *
from time import sleep
import os
import codecs
import time

# ユーザー定義のスクリプト
from config import config
from config import pixiv_account
from kyokou_script import file_replase
from kyokou_script import output

def main():
    print("""
Getting illust script
    """)
    output.print_prosess("START PROGRAM")
    api = PixivAPI()
    file_replase.file_replase()
    file_replase.illustrator_list_replase()

    # file_list.txtを取得
    file_list = output.file_list_replase(config.file_list_csv)

    # illustrator.csvを取得
    illustrator_list = output.illustrator_list_replase(config.illustrator_csv)

    output.print_prosess("Start Prosess")

    # 入力されたuserIDからイラストレーターの情報を取得
    for illustrator in illustrator_list:
        try:
            # ログイン処理
            api.login( pixiv_account.pixiv_id, pixiv_account.password )
            
            illustrator_pixiv_id = int( illustrator[0] )
            output.print_response( illustrator[1], "Start" )

            json_result = api.users_works(illustrator_pixiv_id, per_page=5000) # とりあえずmax5000作品と定義
            total_works = json_result.pagination.total
            illust = json_result.response[0]
            saving_direcory_path = config.current_dir + "\\" + illustrator[1] + "\\"
            aapi = AppPixivAPI()
        
            # 時刻の取得
            start = time.time()

            # ダウンロード
            if not os.path.exists(saving_direcory_path):
                os.mkdir(saving_direcory_path)
            for work_no in range(0, total_works):
                illust = json_result.response[work_no]
                if int(illust.id) not in file_list:
                    # 漫画の場合
                    if illust.is_manga:
                        work_info = api.works(illust.id)
                        for page_no in range(0, work_info.response[0].page_count):
                            page_info = work_info.response[0].metadata.pages[page_no]
                            aapi.download(page_info.image_urls.large, saving_direcory_path)
                            sleep(float(config.get_manga_page_time))
                    # イラストの場合
                    else:
                        aapi.download(illust.image_urls.large, saving_direcory_path)
                        sleep(float(config.get_illust_time))
                    sleep(float(config.illustid_interval))
            
            # 終了時刻の取得
            elapsed_time = time.time() - start

        except:
            output.print_response(illustrator[1],"ERROR")
            sleep(float(config.sleep_exception))
        output.print_response(illustrator[1],"Finish")
        
        if elapsed_time < float(config.illustrator_buttom_sec):
            sleep(float(config.illustrator_interval))

    output.print_prosess("End Prosess")
    del file_list
    del illustrator_list
    print("All Processes Finish")
