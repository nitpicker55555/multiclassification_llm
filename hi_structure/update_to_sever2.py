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
scp -r C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\update_to_sever2.py TUM_LfK@10.162.94.1:D:\puzhen\hi_structure
scp -r C:\Users\Morning\Desktop\hiwi\heart\paper\hi_structure\aaa_model_set_label.py TUM_LfK@10.162.94.1:D:\puzhen\hi_structure
scp -r "C:\Users\Morning\Documents\WeChat Files\wxid_pv2qqr16e4k622\FileStorage\File\2023-11\Twitter Data\Twitter Data\2019-1-1_2019-12-31_without_profile.jsonl" TUM_LfK@10.162.94.1:D:\puzhen\hi_structure\twitter_files\

D:
cd puzhen\hi_structure

conda activate puzhenenv

python aaa_model_set_label.py --file_path twitter_files\2019-1-1_2019-12-31_without_profile.jsonl --col_name content --thread_num 10
python aaa_model_set_label.py --file_path twitter_files\2020-1-1_2020-20-31_without_profile.jsonl --col_name content --thread_num 10
python aaa_model_set_label.py --file_path twitter_files\2018-1-1_2018-12-31_without_profile.jsonl --col_name content --thread_num 10
python aaa_model_set_label.py --file_path twitter_files\2017-1-1_2017-12-31_without_profile.jsonl --col_name content --thread_num 10
python aaa_model_set_label.py --file_path twitter_files\2016-1-1_2016-12-31_without_profile.jsonl --col_name content --thread_num 10
python aaa_model_set_label.py --file_path twitter_files\2015-1-1_2015-12-31_without_profile.jsonl --col_name content --thread_num 20


python fff_sentiment_analyse.py --file_path twitter_files\2019-1-1_2019-12-31_without_profile.jsonl --col_name content --thread_num 10

python fff_sentiment_analyse.py --file_path twitter_files\2018-1-1_2018-12-31_without_profile.jsonl --col_name content --thread_num 10
python fff_sentiment_analyse.py --file_path twitter_files\2017-1-1_2017-12-31_without_profile.jsonl --col_name content --thread_num 10
python fff_sentiment_analyse.py --file_path twitter_files\2016-1-1_2016-12-31_without_profile.jsonl --col_name content --thread_num 10
python fff_sentiment_analyse.py --file_path twitter_files\2015-1-1_2015-12-31_without_profile.jsonl --col_name content --thread_num 10
python fff_sentiment_analyse.py --file_path twitter_files\2021-1-1_2021-12-31_without_profile.jsonl --col_name content --thread_num 10
python fff_sentiment_analyse.py --file_path twitter_files\2020-1-1_2020-12-31_without_profile.jsonl --col_name content --thread_num 10
python fff_sentiment_analyse.py --file_path twitter_files\2022-1-1_2022-12-31_without_profile.jsonl --col_name content --thread_num 10


Traceback (most recent call last):
  File "C:\Users\TUM_LfK\anaconda3\envs\puzhenenv\lib\threading.py", line 932, in _bootstrap_inner
    self.run()
  File "C:\Users\TUM_LfK\anaconda3\envs\puzhenenv\lib\threading.py", line 870, in run
    self._target(*self._args, **self._kwargs)
  File "fff_sentiment_analyse.py", line 36, in one_process
    result_dict['sentiment']=str(with_model(content))
  File "fff_sentiment_analyse.py", line 131, in with_model
    output = model(**encoded_input)
  File "C:\Users\TUM_LfK\anaconda3\envs\puzhenenv\lib\site-packages\torch\nn\modules\module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "C:\Users\TUM_LfK\anaconda3\envs\puzhenenv\lib\site-packages\torch\nn\modules\module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "C:\Users\TUM_LfK\anaconda3\envs\puzhenenv\lib\site-packages\transformers\models\roberta\modeling_roberta.py", line 1198, in forward
    outputs = self.roberta(
  File "C:\Users\TUM_LfK\anaconda3\envs\puzhenenv\lib\site-packages\torch\nn\modules\module.py", line 1518, in _wrapped_call_impl
    return self._call_impl(*args, **kwargs)
  File "C:\Users\TUM_LfK\anaconda3\envs\puzhenenv\lib\site-packages\torch\nn\modules\module.py", line 1527, in _call_impl
    return forward_call(*args, **kwargs)
  File "C:\Users\TUM_LfK\anaconda3\envs\puzhenenv\lib\site-packages\transformers\models\roberta\modeling_roberta.py", line 801, in forward
    buffered_token_type_ids_expanded = buffered_token_type_ids.expand(batch_size, seq_length)
RuntimeError: The expanded size of the tensor (637) must match the existing size (514) at non-singleton dimension 1.  Target sizes: [1, 637].  Tensor sizes: [1, 514]

C:\actions-runner\_work\pytorch\pytorch\builder\windows\pytorch\aten\src\ATen\native\cuda\Indexing.cu:1292: block: [42,0,0], thread: [0,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
C:\actions-runner\_work\pytorch\pytorch\builder\windows\pytorch\aten\src\ATen\native\cuda\Indexing.cu:1292: block: [42,0,0], thread: [1,0,0] Assertion `srcIndex < srcSelectDimSize` failed.
C:\actions-runner\_work\pytorch\pytorch\builder\windows\pytorch\aten\src\ATen\native\cuda\Indexing.cu:1292: block: [42,0,0], thread: [2,0,0] Assertion `srcIndex < srcSelectDimSize` failed.

Traceback (most recent call last):
  File "C:\Users\TUM_LfK\anaconda3\envs\puzhenenv\lib\threading.py", line 932, in _bootstrap_inner
    self.run()
  File "C:\Users\TUM_LfK\anaconda3\envs\puzhenenv\lib\threading.py", line 870, in run
    self._target(*self._args, **self._kwargs)
  File "fff_sentiment_analyse.py", line 36, in one_process
    result_dict['sentiment']=str(with_model(content))
  File "fff_sentiment_analyse.py", line 126, in with_model
    model = AutoModelForSequenceClassification.from_pretrained(MODEL).to(device)
  File "C:\Users\TUM_LfK\anaconda3\envs\puzhenenv\lib\site-packages\transformers\modeling_utils.py", line 2271, in to
    return super().to(*args, **kwargs)
  File "C:\Users\TUM_LfK\anaconda3\envs\puzhenenv\lib\site-packages\torch\nn\modules\module.py", line 1160, in to
    return self._apply(convert)
  File "C:\Users\TUM_LfK\anaconda3\envs\puzhenenv\lib\site-packages\torch\nn\modules\module.py", line 810, in _apply
    module._apply(fn)
  File "C:\Users\TUM_LfK\anaconda3\envs\puzhenenv\lib\site-packages\torch\nn\modules\module.py", line 810, in _apply
    module._apply(fn)
  File "C:\Users\TUM_LfK\anaconda3\envs\puzhenenv\lib\site-packages\torch\nn\modules\module.py", line 810, in _apply
    module._apply(fn)
  File "C:\Users\TUM_LfK\anaconda3\envs\puzhenenv\lib\site-packages\torch\nn\modules\module.py", line 833, in _apply
    param_applied = fn(param)
  File "C:\Users\TUM_LfK\anaconda3\envs\puzhenenv\lib\site-packages\torch\nn\modules\module.py", line 1158, in convert
    return t.to(device, dtype if t.is_floating_point() or t.is_complex() else None, non_blocking)
RuntimeError: CUDA error: device-side assert triggered
CUDA kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing CUDA_LAUNCH_BLOCKING=1.
Compile with `TORCH_USE_CUDA_DSA` to enable device-side assertions.

The provided hypothesis_template "This text is about deepfake." was not able to be formatted with the target labels. Make sure the passed template includes formatting syntax such as {} where the label should go.

Error processing batch: The provided hypothesis_template "This text is about social media." was not able to be formatted with the target labels. Make sure the passed template includes formatting syntax such as {} where the label should go.
Error processing batch: The provided hypothesis_template "This text is about world war ii." was not able to be formatted with the target labels. Make sure the passed template includes formatting syntax such as {} where the label should go.
Error processing batch: The provided hypothesis_template "This text is about neurocontroller." was not able to be formatted with the target labels. Make sure the passed template includes formatting syntax such as {} where the label should go.
"""
