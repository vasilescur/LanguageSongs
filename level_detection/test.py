#pylint: disable=C0103,C0111,C0304,W0401,W0614

from readability_score.calculators.fleschkincaid import *
from readability_score.calculators.dalechall import *
import sqlite3
from get_lyrics import song_lyrics
# from ..app.get_lyrics import song_lyrics

# import mysql.connector

# mydb = mysql.connector.connect(
#     host="localhost",
#     database='lyriclehrer',
#     user="python_sha2",
#     passwd="musiclanguage"
#     # auth_plugin='mysql_native_password'
# )

conn = sqlite3.connect('lyriclehrer.db')


songs = [
    ('musik.txt', 'de_DE'),
    ('narben.txt', 'de_DE'),
    ('rapgod.txt', 'en_US'),
    ('twinkle.txt', 'en_US')
]

# for song in songs:
#     file_name, locale = song

#     fk = FleschKincaid(open(file_name).read(), locale=locale)

#     print('\nScore of ' + file_name + '(locale: ' + locale + '): ')
#     print('min_age = ' + str(fk.min_age) + ', ' + 'us_grade = ' + str(fk.us_grade))


def get_difficulty(lyrics, locale):
    fk = FleschKincaid(lyrics, locale=locale)
    wonderful = 0
    if score > 10:                
    return fk.us_grade / 5

if __name__ == '__main__':
    file = open("titles.txt","r")
    names = []
    info = []
    inx = 0
    song = None
    artist = None

    for line in file:
        if inx == 0:
            song = line.strip()
        if inx == 1:
            artist = line.strip()
        if inx == 2:
            names.append((song,artist))
        inx = (inx+1)%3
    for name in names:
        lyrics = song_lyrics(name[0],name[1])
        if lyrics:
            print (name, get_difficulty(lyrics,"de_DE"))

        # http://www.sqlitetutorial.net/sqlite-python/