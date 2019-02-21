cd /d %~dp0

pip install pixivpy
pip install beautifulsoup4
pip install robobrowser
pip install lxml

echo 11132499,小向 旭 > files\illustrator.csv
type nul > files\kyokou_log.txt
echo current_dir:str =  > config.py
echo file_list_csv:str = \"files\\file_list.txt\" >> config.py
echo illustrator_csv:str = "files\\illustrator.csv" >> config.py
echo log_file:str = "files\\kyokou_log.txt" >> config.py
echo sleep_exception:float = 20.0 >> config.py
echo illustrator_buttom_sec:float = 5.0 >> config.py
echo illustrator_interval:float = 4.0 >> config.py
echo illustid_interval:float = 1.0 >> config.py
echo get_illust_time:float = 2.0 >> config.py
echo get_manga_page_time:float = 1.0 >> config.py
echo pixiv_id:str = >> config.py
echo password:str = >> config.py
echo user_id:str = >> config.py
