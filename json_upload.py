import openai
import os
openai.api_key = "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"
def upload():

    # training_response=openai.File.create(file=open("data.jsonl", "rb"), purpose="fine-tune")
    # training_file_id=training_response["id"]
    # print("Training_file_ID:", training_file_id)
    response = openai.FineTuningJob.create(training_file="file-PLdPS5yuufYDulsfjJec5DGi", model="gpt-3.5-turbo")
    job_id = response["id"]

    print(job_id)
    print("Job ID:", response["id"])
    print("Status:", response["status"])


# print(openai.File.list())

print(openai.FineTuningJob.list(limit=10))
# upload()

