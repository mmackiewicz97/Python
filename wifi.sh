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
