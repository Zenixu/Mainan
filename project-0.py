import pytube

link = input('enter yt video link: ')
yt = pytube.YouTube(link)
yt.streams.first().download()
print('downloaded', link)