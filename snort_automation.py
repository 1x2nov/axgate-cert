import subprocess
import os
import pandas as pd

# 실행할 명령어
snort = "snort -A console -r "  #snort 수행 결과 출력
path_store = '/snort/aegis_CVE_pcap' #snort로 검증할 pcap이 있는 경로
path_snort_conf= '/etc/snort/snort.conf' #Snort 설정파일 경로
path_snort_rule = '/etc/snort/rules/vulnerability.rules' #Snort Rule 파일. 추후 git으로 

with open(path_snort_rule, 'r') as file :
    file_content = file.readlines() #file_content에 rules 파일을 불러와 저장
file.close()

line =[]
for lines in file_content:
   line.append(lines[lines.find("msg:")+5:lines.find("_")]) 
line = list(set(line)) #Rule에서 검증할 pcap대상을 pcap이름으로 가져와 저장

pcap_folder = os.listdir(path_store) #path_store에 있는 파일 목록을 저장

data=[]# 결과값 저장 변수
runcount = 0
for name in pcap_folder : 
    split = name.split('_')
    cve_name = split[1] #파일 목록에서 pcap이름 부분만 저장
    if cve_name in line : # 파일 목록의 pcap이름과 Rule에 포함된 pcap이름이 일치할 경우
        pcap_list=os.listdir(path_store+"/"+name)
        data.append([cve_name, pcap_list])

        for num in range(0,len(pcap_list)) :
            command = snort+path_store+"/"+name+"/"+pcap_list[num]+" -c "+path_snort_conf+" -q"
            result = os.popen(command) # 해당 CVE에 대해서 snort 수행
            result = result.read()
            data[runcount].append(result.strip()) #결과값을 data에 저장
        runcount+=1


fail_count=0 # 실패 횟수
success_count=0 # 성공 횟수
exe_result = [["CVE NAME", "Success", "Failure"]] # 최종 결과 값

for index in range(0,len(data)) :
    index_for_result = 0
    for check_fail in range(1, len(data[index])-1) : 
        print(data[index][0])
        if data[index][0] in data[index][check_fail+1] :
            if index_for_result == 0 :
                cve_tmp = data[index][0]
                index_for_result += 1
            success_count += 1
        if data[index][0] not in data[index][check_fail+1] :
            if index_for_result == 0 :
                cve_tmp = data[index][0]
                index_for_result += 1
            fail_count += 1
    exe_result.extend([[cve_tmp, success_count, fail_count]])

    success_count = 0
    fail_count = 0


print(exe_result)

df_exe_result = pd.DataFrame(exe_result)
df_exe_result.to_csv("/actions-runner/_work/axgate-cert/axgate-cert/snort_result.csv", header=None, index=None)