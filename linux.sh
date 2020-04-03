# Imagemagick for tesseract 
convert -density 300 plik.pdf -depth 8 -strip -background white -alpha off plikout.tiff

convert -density 300 -trim plik.pdf[50] -quality 100 50.jpg
	plik.pdf %02d.pdf #pojedyncze strony
	*.pdf plik.pdf #jeden plik
# Tesseract pdf to txt
tesseract plikout.tiff -l pol pliktext

mogrify -resize 400x300 plik.jpg
	-resize 50%

vnstat (-u)
vnstati -s -i wlp1s0 -o ~/Pulpit/plik.png
sudo vnstati -h -i wlp1s0 -o ~/Pulpit/sum.png

#change name files
a=1
for i in *.jpg; do
  new=$(printf "%04d.jpg" "$a") #04 pad to length of 4
  mv -i -- "$i" "$new"
  let a=a+1
done

pyinstaller --onefile --windowed nazwa.py

nmap -sP 192.168.0.1/24
ip a
ip r
ping www.sgsp.edu.pl
host 178.73.9.50
dig sonda.inf.sgsp.edu.pl
telnet 127.0.0.53 53
telnet mail.sgsp.edu.pl 25
dig k.szach.in
mtr -n k.szach.in
netstat -nat 
nmap z.szach.in
nmap -Pn k.szach.in
ping 85.187.140.122

xdotool search --onlyvisible --name "nuc"

adb start-server
adb devices 
adb connect 192.168.0.50:5555
adb shell screencap /sdcard/scren.png
adb kill-server
adb tcpip 5555

scrcpy
scrcpy -b 2m -m 1024--always-on-top

youtube-dl -x --audio-format mp3 https://www.youtube.com/
youtube-dl -F https://www.youtube.com/

whois 10.10.10.30

		ls /home/m/Muzyka/yt -l | wc -l 
		total_seconds=$(( $(mp3info -p '%S + ' /home/m/Muzyka/yt/*.mp3) 0 ))
		printf "%02d:%02d:%02d\n" $((total_seconds / 3600)) $((total_seconds/60 - (total_seconds/3600)*60)) $((total_seconds % 60))
cat input.txt | cut -d ' ' -f 2| sort -n| head -n 2| uniq -c

grep -rnw . -e "pattern"
python3 -m http.server 80
shred -uvzn 5 file
youtube-dl -x --audio-format mp3 --playlist-items 1-15,17 -o '/home/%(title)s.%(ext)s'\''' https://yt
curl -u name pass

