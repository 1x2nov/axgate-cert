FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y install libpcre3 libpcre3-dbg libpcre3-dev libpcap-dev\
    build-essential autoconf automake libtool libnet1-dev \
    libyaml-0-2 libyaml-dev zlib1g zlib1g-dev libcap-ng-dev libcap-ng0 \
    make flex bison git wget libmagic-dev pkg-config libnuma-dev strace \
    perl libio-socket-ssl-perl libcrypt-ssleay-perl ca-certificates libwww-perl \
    python-pip python-pcapy python-dpkt supervisor openssh-server net-tools \
    iputils-ping

# Install Snort
RUN apt-get -y install snort
RUN snort -v
