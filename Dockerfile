FROM ubuntu:latest

# Dependancy Install
RUN apt-get update
RUN apt install -y build-essential libpcap-dev libpcre3-dev libdumbnet-dev zlib1g-dev liblzma-dev openssl libssl-dev bison flex libhwloc-dev pkg-config openssh-server net-tools iputils-ping

# Install Snort
RUN DEBIAN_FRONTEND=noninteractive apt-get -q -y install snort

RUN mkdir -p /snort/{aegis_CVE_pcap, tmp_pcap}
WORKDIR  /snort
RUN ls -al

# COPY snort.conf /etc/snort/snort.conf
