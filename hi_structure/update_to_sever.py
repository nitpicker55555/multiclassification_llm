"""



        IP: 10.162.94.1 Account: lfkserver4080/tum_lfk
(PS. lfkserver4080 is the domain and tum_lfk is the user account)        Password: TUM_LfK_4080
        To login your own acccount, use IP: 10.162.94.1 Account: lfkserver4080/(your created account) and Password: (no password)
    Or 2 SSH connection
        ssh TUM_LfK@10.162.94.1
Password: TUM_LfK_4080




ssh TUM_LfK@10.162.94.1

scp -r C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure TUM_LfK@10.162.94.1:D:\puzhen\
scp -r C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\requirements.txt TUM_LfK@10.162.94.1:D:\puzhen\hi_structure
scp -r C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\aaa_model_set_label.py TUM_LfK@10.162.94.1:D:\puzhen\hi_structure
scp -r "C:\Users\Morning\Documents\WeChat Files\wxid_pv2qqr16e4k622\FileStorage\File\2023-11\Twitter Data\Twitter Data\2019-1-1_2019-12-31_without_profile.jsonl" TUM_LfK@10.162.94.1:D:\puzhen\hi_structure\twitter_files\

D:
cd puzhen\hi_structure

conda activate puzhenenv

start /B python aaa_model_set_label.py --file_path twitter_files\2019-1-1_2019-12-31_without_profile.jsonl --col_name content --thread_num 10
"""