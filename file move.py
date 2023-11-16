import os
import shutil
import re

path_store = 'C:\\Users\\AXGATE\\Desktop\\2023.11.14_2018-2019_Payload\\AX_2018-19\\aegisc_CVE_pcap'

folders = os.listdir(path_store)

for name in folders :
    if "CVE" in name :
        front, back =list(os.path.splitext(name))
        shutil.move(path_store+"\\"+name, path_store+"\\"+front[:front.index('_')]+"_pcap")