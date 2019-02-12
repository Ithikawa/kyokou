# -*- coding: utf-8 -*-
import sys
from pixivpy3 import *
from time import sleep
import argparse
import codecs

def get_illust_main(filelist: str,illustrator_pixiv_id: int,account: str,passwd: str,saving_direcory_path: str,get_manga_page_time: float,get_illust_time: float,illustid_interval: float):
    api = PixivAPI()
    api.login( account, passwd )

    json_result = api.users_works(illustrator_pixiv_id, per_page=5000) # とりあえずmax5000作品と定義
    total_works = json_result.pagination.total
    illust = json_result.response[0]
    aapi = AppPixivAPI()
    # ダウンロード
    for work_no in range(0, total_works):
        try:
            illust = json_result.response[work_no]
            if int(illust.id) not in filelist:
                # 漫画の場合
                if illust.is_manga:
                    work_info = api.works(illust.id)
                    for page_no in range(0, work_info.response[0].page_count):
                        page_info = work_info.response[0].metadata.pages[page_no]
                        aapi.download(page_info.image_urls.large, saving_direcory_path)
                        sleep(float(get_manga_page_time))
                # イラストの場合
                else:
                    aapi.download(illust.image_urls.large, saving_direcory_path)
                    sleep(float(get_illust_time))
                sleep(float(illustid_interval))
        except:
            return

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--filelist", help="file path for illust file path list csv")
    
    parser.add_argument("-a","--account", help="pixiv account id")
    parser.add_argument("-p","--passwd", help="pixiv account password")
    parser.add_argument("-i","--illustratorid", help="target illustrator pixiv account id")
    parser.add_argument("-d","--dir", help="saving dir")
    args = parser.parse_args()

    f = codecs.open(args.filelist,"r","utf-8")
    file_info = f.read().split("\r\n")
    f.close()
    get_illust_main(file_info,args.illustratorid,args.account,args.passwd,args.dir)