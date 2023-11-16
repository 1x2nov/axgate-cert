import subprocess
import os

# 실행할 명령어
snort = "snort -A console -r"  # 예: "dir"은 현재 디렉토리의 파일 목록을 출력하는 명령어입니다.
path_store = 'C:\\Users\\AXGATE\\Desktop\\2023.11.14_2018-2019_Payload\\AX_2018-19\\aegisc_CVE_pcap'
path_snort_conf= 'C:\\Snort\\etc\\snort.conf'
path_snort_rule = 'C:\\Snort\\rules\\vulnerability.rules'

with open(path_snort_rule, 'r') as file :
    file_content = file.readlines()
file.close()

line =[]
for lines in file_content:
   line.append(lines[lines.find("CVE"):lines.find("_")])
line = list(set(line))

pcap_folder = os.listdir(path_store)

for name in pcap_folder :
    split = name.split('_')
    cve_name = split[1]
    if cve_name in line :
        pcap_list=os.listdir(path_store+"\\"+name)
        for num in range(0,len(pcap_list)) :
            command = snort+path_store+"\\"+name+"\\"+pcap_list[num]+" -c "+path_snort_conf+" -q"
#           command = snort, path_store+"\\"+name+"\\"+pcap_list[num], '-c '+path_snort_conf+' -q'
            result = subprocess.Popen(command, stdout=subprocess.PIPE, encoding="cp949").stdout
            data = result.read().strip()
            result.close()
            print (data)