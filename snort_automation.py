import subprocess
import os

# 실행할 명령어
snort = "snort -A console -r"  #snort 수행 결과 출력
path_store = 'C:\\Users\\AXGATE\\Desktop\\2023.11.14_2018-2019_Payload\\AX_2018-19\\aegisc_CVE_pcap' #snort로 검증할 pcap이 있는 경로
path_snort_conf= 'C:\\Snort\\etc\\snort.conf' #Snort 설정파일 경로
path_snort_rule = 'C:\\Snort\\rules\\vulnerability.rules' #Snort Rule 파일. 추후 git으로 변경

with open(path_snort_rule, 'r') as file :
    file_content = file.readlines() #file_content에 rules 파일을 불러와 저장
file.close()

line =[]
for lines in file_content:
   line.append(lines[lines.find("CVE"):lines.find("_")]) 
line = list(set(line)) #Rule에서 검증할 pcap대상을 CVE이름으로 가져와 저장

pcap_folder = os.listdir(path_store) #path_store에 있는 파일 목록을 저장

data=[]# 결과값 저장 변수
for name in pcap_folder : 
    split = name.split('_')
    cve_name = split[1] #파일 목록에서 CVE코드 부분만 저장
    if cve_name in line : # 파일 목록의 CVE코드와 Rule에서 저장한 CVE코드가 일치할 경우
        pcap_list=os.listdir(path_store+"\\"+name)
        for num in range(0,len(pcap_list)) :
            command = snort+path_store+"\\"+name+"\\"+pcap_list[num]+" -c "+path_snort_conf+" -q"
            result = subprocess.Popen(command, stdout=subprocess.PIPE, encoding="cp949").stdout # 해당 CVE에 대해서 snort 수행
            data.append(result.read().strip()) #결과값을 data에 저장

            result.close()
print (*data, sep='\n') #결과값 출력
