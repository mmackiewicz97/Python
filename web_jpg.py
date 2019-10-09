import urllib.request
link = "http://komarowkapodlaska.pl/wp-content/uploads/2019/08/IMG_4834.jpg"
filename = link.split('/')[-1]
urllib.request.urlretrieve(link, filename)
