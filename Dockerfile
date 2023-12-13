FROM ubuntu:latest

# Dependency Install
RUN apt-get update && apt-get install -y vim build-essential libpcap-dev libpcre3-dev libdumbnet-dev zlib1g-dev \
    liblzma-dev openssl libssl-dev bison flex libhwloc-dev pip pkg-config openssh-server net-tools iputils-ping
RUN pip install pandas slack_sdk

# Install Snort
RUN DEBIAN_FRONTEND=noninteractive apt-get -q -y install snort

# Set Environment
RUN mkdir -p /snort/aegis_CVE_pcap /snort/tmp_pcap
RUN rm /etc/snort/rules/* && touch /etc/snort/rules/white_list.rules /etc/snort/rules/black_list.rules

COPY snort.conf /etc/snort/snort.conf
COPY rule/vulnerability.rules /etc/snort/rules
COPY snort_automation /snort
COPY pcap /snort/tmp_pcap

# Snort Automation
WORKDIR /snort
RUN python3 file_extract.py && python3 snort_automation.py && python3 snort_result_to_slack.py