import pandas as pd
import slack_sdk
import base64

slack_token_decrypt = 'eG94Yi0yMjEwMzc1NzU3NTkxLTYyMTgwMDQ3NTIxMzUtMnVXZmlYYlNKSzc3Z3dRWDBWN05vRk16='
slack_token_decrypt = slack_token_decrypt.encode('ascii')
slack_token = base64.b64decode(slack_token_decrypt)
slack_token = str(slack_token)
slack_token = slack_token[2:-1]

print(slack_token)

client = slack_sdk.WebClient(token=slack_token)
result = pd.read_csv('/snort/snort_result.csv')
result = result.values.tolist()

format_message = []
for index in range(0,len(result)) :
    format_message.append("취약점 명 : {} 성공 : {} 실패 : {}".format(result[index][0], result[index][1], result[index][2]))


for message in format_message :
    client.chat_postMessage(channel='#snort-auto', text=message)
