import pandas as pd
import slack_sdk
import base64

slack_token_decrypt = 'eG94Yi0yMjEwMzc1NzU3NTkxLTYyMTgwMDQ3NTIxMzUtMnVXZmlYYlNKSzc3Z3dRWDBWN05vRk16='# Github처럼 Public한 곳에 slack token이 노출될 경우 자동으로 비활성화 되기 때문에, base64로 암호화
slack_token_decrypt = slack_token_decrypt.encode('ascii')
slack_token = base64.b64decode(slack_token_decrypt)
slack_token = str(slack_token)
slack_token = slack_token[2:-1] # base64로 암호화 한 slack token을 decode하고, b' 부분을 제거 하고 slack_token에 값 저장

client = slack_sdk.WebClient(token=slack_token)
result = pd.read_csv('/snort/snort_result.csv')
result = result.values.tolist() #csv 파일에서 DataFrame을 불러와 List형으로 저장

result_msg = result[0][3].split(',') # 불러온 데이터 중 Log 부분 데이터 리스트로 저장

success_log = []
for index in range(0,len(result_msg)) :
    if 'CVE' in result_msg[index] : # 리스트로 정리한 Log데이터 중 성공 부분은
        success_log.append(result_msg[index][result_msg[index].index('[*'):-1])
                # 보기 편하게 슬라이싱 

result_msg=[]
for index in range(0,len(success_log)):
    if index == len(success_log)-1 :
        result_msg.append(success_log[index][:-1])
                # 슬라이싱 한 리스트의 마지막 데이터에 있는 ] 값은 제외하고 저장
    else :
       result_msg.append(success_log[index]) # 슬라이싱 한 데이터 저장



format_message = []
for index in range(0,len(result)) :
     tmp_msg = [] # 메시지 정형 전 임시 저장
     count = 0 # 최초 실행 시
     if count == 0 :
        for num in range(0,len(result_msg)) :
            if "CVE" in result_msg[num] : # 취약점 명과 로그의 매핑 확인
                if result_msg[num][result_msg[num].index('C'):result_msg[num].index('_')] == result[index][0] :
                  tmp_msg.append(result_msg[num])  #임시 저장 공간에 로그 저장
        format_message.append("취약점 명 : {} 성공 : {} 실패 : {}  ".format(result[index][0], result[index][1], result[index][2])) # 테스트 결과 저장
        format_message.append("{}".format(tmp_msg)) # 테스트 로그 저장
        count +=1


for message in format_message :
    tmp_log=""
    if '[**]' in message : # Slack 으로 전송할 메세지가 로그인 경우
        log_msg = message.split(',')
        for index in range(0,len(log_msg)):
            tmp_log += log_msg[index][log_msg[index].index("[*"):]
            tmp_log = tmp_log.rstrip(']')
            tmp_log = tmp_log.rstrip("'") #불필요한 문자열 제거 및 편집하여
            tmp_log += '\n'
        message="Log :"+'\n'+tmp_log #가독성을 위해 개행하여 message에 저장
    client.chat_postMessage(channel='#snort-auto', text=message)
        #message 변수에 저장된 값을 Slack으로 전송
