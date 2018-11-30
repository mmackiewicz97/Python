#!/bin/bash
for i in {25..1};
do
	echo $i;
	sleep 1m;
done;
ffplay Correct-answer.mp3 -nodisp -volume 30 -autoexit
for i in {5..1}
do 
	echo $i
	sleep 1m
done
ffplay plum.mp3 -nodisp -volume 30 -autoexit
notify-send "Koniec przerwy"

date1=$((`date +%s`)); 
while true; do 
	echo -ne "$(date -u --date @$((`date +%s`-$date1)) +%M:%S)\r"
    sleep 0.5
	trap break SIGINT
done
#!/bin/bash
gnome-terminal -e "bash -c \"./.nauka.sh; exec bash\"" --geometry 42x2+1010
