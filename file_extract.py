import glob
import os
import pandas as pd

path_extract = '/snort/tmp_pcap/'
path_store = '/snort/aegisc_CVE_pcap'
list_csv='/snort/pcaplist.csv'


folders = os.listdir(path_extract)
pcap_list = pd.read_csv(list_csv)
filename = pcap_list.loc[:,"File name"]
listofpcap = filename.values+'.pcap'
foldername =list("aegis_"+filename.values+'_pcap')


for name in folders :
    if 'Payload' in name :
       path_from =path_extract+"/"+name
       pcapname = os.listdir(path_from)
       filenum = path_from[-1]
       for i in range(0,len(foldername)) :
            if not os.path.exists(path_store+"/"+foldername[i]) :
                os.makedirs(path_store+"/"+foldername[i])
            else:
                continue
       for pcap in listofpcap: 
         ext_path, ext_file = os.path.splitext(pcap)
         if os.path.isfile(path_from+"/"+pcap) :
           os.rename(path_from+"/"+pcap, path_store+"/"+"aegis_"+ext_path+"_pcap"+"/"+ext_path+"_"+filenum+ext_file)


