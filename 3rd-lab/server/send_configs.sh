#!/bin/bash
if [[ $# -lt 2 ]];
then
	echo "No Arguments supplied! launch as :"
	echo "$0 port timeout";
	exit;
fi

for interface in eth0, enp3s0, wlan0, ens2; do
	local_ip=$(ifconfig enp3s0 | grep inet | awk '{print $2}'| cut -f2 -d: | sed ':a;N;$!ba;s/\n/ /g')
	if [[ ! -z "$local_ip" ]]; then
		break
	fi 
done

echo $local_ip;
config="ip=$local_ip\nport=$1\ntimeout=$2\n";

echo -e $config;
for net in $(ip -o -f inet addr show | grep $local_ip | awk '/scope global/ {print $4}'); do
	nets=$(nmap -sL $net | awk '/Nmap scan report/{print $NF}' | sed 's/(//g' | sed 's/)//g');
	for ip in $nets; do
		$(echo -e $config | nc -q 0 -N $ip 5001 &);
		echo $ip;
	done;
done;
	

