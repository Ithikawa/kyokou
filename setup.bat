@echo off
cd /d %~dp0

python -m pip install pixivpy
python -m pip install beautifulsoup4
python -m pip install robobrowser
python -m pip install lxml

if not exist files\illustrator.csv (
    echo 11132499,小向 旭 > files\illustrator.csv
)
if not exist files\kyokou_log.txt (
    type nul > files\kyokou_log.txt
)
if not exist config.py (
    echo current_dir:str = "files\\" # By default to the "files" folder in the current directory. > config.py
    echo file_list_csv:str = "files\\file_list.txt" >> config.py
    echo illustrator_csv:str = "files\\illustrator.csv" >> config.py
    echo log_file:str = "files\\kyokou_log.txt" >> config.py
    echo sleep_exception:float = 20.0 >> config.py
    echo illustrator_buttom_sec:float = 5.0 >> config.py
    echo illustrator_interval:float = 4.0 >> config.py
    echo illustid_interval:float = 1.0 >> config.py
    echo get_illust_time:float = 2.0 >> config.py
    echo get_manga_page_time:float = 1.0 >> config.py
    echo pixiv_id:str = "" # pixiv_id is a user setting screen string. >> config.py
    echo password:str = "" >> config.py
    echo user_id:str = "" # user_id is a numeric value of personal url. >> config.py
)

echo sucsess!