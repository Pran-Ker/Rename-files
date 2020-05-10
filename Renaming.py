import os, songdetails

location = r'/Users/Mo/Music'
os.chdir(location)

for root, dirs, files in os.walk(location):
    for mp3s in files:
        if mp3s.endswith('.mp3'):
            song = songdetails.scan(mp3s)
            song_name="{}.mp3".format(song.title)
            print ("{} will be renamed to {} ".format (mp3s,song.title))
            os.rename(mp3s, song_name)