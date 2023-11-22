import requests
import pandas as pd
import slack_sdk
import base64

slack_token_base64 = 'eG94Yi0yMjEwMzc1NzU3NTkxLTYyMTgwMDQ3NTIxMzUtdWI0UlYxcFJkWGdqcG9IbWtwbExOVGZN'
slack_token = slack_token_base64.encode('ascii')
slack_token = base64.b64decode(slack_token)
slack_token = slack_token.decode('UTF-8')

print(slack_token)
client = slack_sdk.WebClient(token=slack_token)
result = pd.read_csv('snort_result.csv')
result = result.values.tolist()

format_message = []
for index in range(0,len(result)) :
    format_message.append("취약점 명 : {} 성공 : {} 실패 : {}".format(result[index][0], result[index][1], result[index][2]))


for message in format_message :
    client.chat_postMessage(channel='#snort-automation', text=message)

