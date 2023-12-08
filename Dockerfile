FROM ubuntu:latest

RUN apt-get update
RUN apt-get -y installgcc libpcre3-dev zlib1g-dev libluajit-5.1-dev \
    libpcap-dev openssl libssl-dev libnghttp2-dev libdumbnet-dev \
    bison flex libdnet autoconf libtool

# Fetch source
RUN cd /usr/local/src && \
    wget https://www.snort.org/downloads/snort/daq-2.0.7.tar.gz && \
    tar xzf daq-2.0.7.tar.gz && \
    cd /usr/local/src && \
    wget https://www.snort.org/downloads/snort/snort-2.9.20.tar.gz && \
    tar -xvzf snort-2.9.20.tar.gz && \
    cd /usr/local/src && \

# Build DAQ
RUN cd /usr/local/src/daq-* && \
    autoreconf -f -i && \
    ./configure && make && sudo make install

# Build snort
RUN cd /usr/local/src/snort-* && \
    ./configure --enable-sourcefire && make && sudo make install&& \
    snort -v
    
