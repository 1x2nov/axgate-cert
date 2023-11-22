import requests
import pandas as pd
import slack_sdk


slack_token = 'xoxb-2210375757591-6218004752135-xQqq3zLadV1bT8KUs41IxbOz'
client = slack_sdk.WebClient(token=slack_token)
result = pd.read_csv('snort_result.csv')
result = result.values.tolist()

format_message = []
for index in range(0,len(result)) :
    format_message.append("취약점 명 : {} 성공 : {} 실패 : {}".format(result[index][0], result[index][1], result[index][2]))


for message in format_message :
    client.chat_postMessage(channel='#snort-automation', text=message)

