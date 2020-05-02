#!/bin/bash
# Airport Wifi changer by Unknow

nr=16
while [ thrue ]; do
	end=`echo "obase=16; $nr"|bc`
	newmac=18:65:90:d2:1d::$end
	ifconfig en0 ether $newmac
	echo "Nowy adres: $newmac"
	nr=$[$nr+1];
	sleep 600
done

#wlp1s0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
#        inet 10.10.31.133  netmask 255.255.254.0  broadcast 10.10.31.255
#        inet6 fe80::88d6:a77a:8a35:3bd7  prefixlen 64  scopeid 0x20<link>
#        ether ac:72:89:64:67:9d  txqueuelen 1000  (Ethernet)
