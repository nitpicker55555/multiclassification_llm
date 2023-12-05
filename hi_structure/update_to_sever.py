"""



        IP: 10.162.94.1 Account: lfkserver4080/tum_lfk
(PS. lfkserver4080 is the domain and tum_lfk is the user account)        Password: TUM_LfK_4080
        To login your own acccount, use IP: 10.162.94.1 Account: lfkserver4080/(your created account) and Password: (no password)
    Or 2 SSH connection
        ssh TUM_LfK@10.162.94.1
Password: TUM_LfK_4080




ssh TUM_LfK@10.162.94.1

scp -r C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure TUM_LfK@10.162.94.1:D:\puzhen\
scp -r C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure TUM_LfK@10.162.94.1:D:\puzhen\
scp -r C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\requirements.txt TUM_LfK@10.162.94.1:D:\puzhen\hi_structure
scp -r C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\update_to_sever.py TUM_LfK@10.162.94.1:D:\puzhen\hi_structure
scp -r C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\fff_sentiment_analyse.py TUM_LfK@10.162.94.1:D:\puzhen\hi_structure
scp -r C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\aaa_model_set_label.py TUM_LfK@10.162.94.1:D:\puzhen\hi_structure
scp -r "C:\Users\Morning\Documents\WeChat Files\wxid_pv2qqr16e4k622\FileStorage\File\2023-11\Twitter Data\Twitter Data\2018-1-1_2018-12-31_without_profile.jsonl" TUM_LfK@10.162.94.1:D:\puzhen\hi_structure\twitter_files\
scp -r "C:\Users\Morning\Documents\WeChat Files\wxid_pv2qqr16e4k622\FileStorage\File\2023-11\Twitter Data\Twitter Data\2017-1-1_2017-12-31_without_profile.jsonl" TUM_LfK@10.162.94.1:D:\puzhen\hi_structure\twitter_files\
scp -r "C:\Users\Morning\Documents\WeChat Files\wxid_pv2qqr16e4k622\FileStorage\File\2023-11\Twitter Data\Twitter Data\2016-1-1_2016-12-31_without_profile.jsonl" TUM_LfK@10.162.94.1:D:\puzhen\hi_structure\twitter_files\
scp -r "C:\Users\Morning\Documents\WeChat Files\wxid_pv2qqr16e4k622\FileStorage\File\2023-11\Twitter Data\Twitter Data\2015-1-1_2015-12-31_without_profile.jsonl" TUM_LfK@10.162.94.1:D:\puzhen\hi_structure\twitter_files\
scp -r "C:\Users\Morning\Documents\WeChat Files\wxid_pv2qqr16e4k622\FileStorage\File\2023-11\Twitter Data\Twitter Data\2020-1-1_2020-12-31_without_profile.jsonl" TUM_LfK@10.162.94.1:D:\puzhen\hi_structure\twitter_files\
scp -r "C:\Users\Morning\Desktop\hiwi\gpt_score\twitter_spider\2021-1-1_2021-12-31_without_profile.jsonl" TUM_LfK@10.162.94.1:D:\puzhen\hi_structure\twitter_files\
scp -r "C:\Users\Morning\Documents\WeChat Files\wxid_pv2qqr16e4k622\FileStorage\File\2023-11\Twitter Data\Twitter Data\2022-1-1_2022-12-31_without_profile.jsonl" TUM_LfK@10.162.94.1:D:\puzhen\hi_structure\twitter_files\


scp -r TUM_LfK@10.162.94.1:D:\puzhen\hi_structure\update_to_sever.py C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\update_to_sever2.py




scp -r TUM_LfK@10.162.94.1:D:\puzhen\hi_structure\update_to_sever2.py C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\update_to_sever2.py
D:
cd puzhen\hi_structure

conda activate puzhenenv

start /B python aaa_model_set_label.py --file_path twitter_files\2019-1-1_2019-12-31_without_profile.jsonl --col_name content --thread_num 10
"""