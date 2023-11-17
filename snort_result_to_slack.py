import pandas as pd
from slack_sdk import WebhookClient
from slack_sdk.errors import SlackApiError

slack_hook = "https://hooks.slack.com/services/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"

webhook = WebhookClient(url=slack_hook)

result = pd.read_csv('C:\\actions-runner\\_work\\axgate-cert\\axgate-cert\\snort_result.csv')
result = result.values.tolist()




format_message = []
for index in range(0,len(result)) :
    format_message.append("CVE : {} 성공 : {} 실패 : {}".format(result[index][0], result[index][1], result[index][2]))

for index in range(0, len (format_message)) : 
    msg = '{}'.format(format_message[index])
    try : 
        response = webhook.send(text=msg)
    except SlackApiError as e :
        print(e)
