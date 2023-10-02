import openai
completion = openai.ChatCompletion.create(
  model="ft:gpt-3.5-turbo-0613:personal::7tkIkRMB",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)