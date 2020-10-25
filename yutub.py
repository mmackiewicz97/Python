import youtube_dl
import os

from pip._vendor.distlib.compat import raw_input


def wybierz_folder():
    os.chdir('E:\\Muzyka')
    print("Wybierz folder:")
    foldery = []
    for x, i in enumerate(os.listdir('E:\\Muzyka')):
        print(f'{x}. {i}')
        foldery.append(i)
    print("Wciśnij x by utworzyć nowy katalog")
    file = input()
    if file == 'x':
        os.mkdir(input("Wprowadź nazwę folderu:"))
        wybierz_folder()
    else:
        os.chdir(foldery[int(file)])
        wybierz_format()

def wybierz_format():
    # print("Wklej URL")
    # url = str(input())
    print("Wklej URL /--playlist-start 1 --playlist-end 5")
    url = raw_input()
    os.system(f"youtube-dl -x --audio-format mp3 -o %(title)s.mp3 {url}")
    wybierz_folder()

wybierz_folder()
