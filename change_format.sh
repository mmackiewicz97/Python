for FILE in *; do
	ffmpeg -i "${FILE}" -vn -ab 128k -ar 44100 -y "${FILE%.webm}.mp3";
	echo FILE;
done;
