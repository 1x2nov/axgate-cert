FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y install apt install -y build-essential libpcap-dev libpcre3-dev libdumbnet-dev zlib1g-dev liblzma-dev openssl libssl-dev bison flex libhwloc-dev pkg-config openssh-server net-tools iputils-ping

# Install Snort
RUN apt-get -y install snort
RUN snort -v
