import os

path_extract = '/snort/tmp_pcap/'
path_store = '/snort/aegis_CVE_pcap'


folders = os.listdir(path_extract)
pcap_list=[]


for name in folders :
    if "Payload" in name :
        pcap_name=os.listdir(path_extract+'/'+name)
        pcap_list.append([name,pcap_name]) 

for makedir in range(0,len(pcap_list)) :
    path_from = path_extract+'/'+pcap_list[makedir][0]
    for namecheck in pcap_list[makedir][1] :
        if '.pcap' in namecheck :
            namecheck = namecheck.rstrip('.pcap')
            namecheck = namecheck.replace(" ","_")
            namecheck = 'aegis_'+namecheck+'_pcap'
            if not os.path.exists(path_store+'/'+namecheck) :
                os.makedirs(path_store+'/'+namecheck)
            else :
                continue


for count in range(0,len(pcap_list)) : 
    number=1
    for movepcap in pcap_list[count][1] :
        if '.pcap' in movepcap :
            pcapcheck = movepcap.rstrip('.pcap')
            pcapcheck = pcapcheck.replace(" ","_") 
        
            if os.path.exists(path_store+"/"+'aegis_'+pcapcheck+'_pcap') :
               os.rename(path_extract+'/'+pcap_list[count][0]+'/'+movepcap, path_store+"/"+'aegis_'+pcapcheck+'_pcap'+"/"+pcapcheck+"_"+number+".pcap")
               number+=1