FROM ubuntu:latest

RUN apt-get update
RUN apt -y install gcc libpcre3-dev zlib1g-dev libluajit-5.1-dev \
    libpcap-dev openssl libssl-dev libnghttp2-dev libdumbnet-dev \ 
    make wget bison flex libdnet autoconf libtool

# Fetch source
RUN mkdir /tmp/snort-daq && cd /tmp/snort-daq \
    wget https://www.snort.org/downloads/snort/daq-2.0.7.tar.gz && \
    tar xzf daq-2.0.7.tar.gz && \
    mkdir /tmp/snort && cd /tmp/snort \
    wget https://www.snort.org/downloads/snort/snort-2.9.20.tar.gz && \
    tar -xvzf snort-2.9.20.tar.gz && \
    cd /usr/local/src && \

# Build DAQ
RUN cd /tmp/snort-daq/daq-* && \
    autoreconf -f -i && \
    ./configure && make && sudo make install

# Build snort
RUN cd /tmp/snort/snort-* && \
    ./configure --enable-sourcefire && make && sudo make install&& \
    snort -v
    
