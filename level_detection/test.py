#pylint: disable=C0103,C0111,C0304,W0401,W0614


import sqlite3
from get_lyrics import song_lyrics
from readability_score.calculators.fleschkincaid import *
from readability_score.calculators.dalechall import *
# from ..app.get_lyrics import song_lyrics

# import mysql.connector

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
    score = fk.us_grade/5

    if score > 18:
        return '5'
    if score > 15:
        return '4+'
    if score > 10:
        return '4'
    if score > 8:
        return '3+'
    if score > 6:
        return '3'
    if score > 4:
        return '2+'
    if score > 3:
        return '2'
    if score > 1:
        return '1+'
    return '1'

if __name__ == '__main__':
    conn = sqlite3.connect('lyriclehrer.db')

    file = open("titles.txt", "r")

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
            names.append((song, artist))
        inx = (inx+1)%3

    for name in names:
        print('Working on ' + name[0] + '... ', end='')

        lyrics = song_lyrics(name[0], name[1])
        lang = 'de_DE'

        # try:
        diff = get_difficulty(lyrics, lang)
        print('--> ' + str(diff))

        conn.execute('''INSERT INTO Songs (title, artist, level, language) VALUES (?,?,?,?)''', [name[0], name[1], diff, lang])
        conn.commit()


        # conn.execute('''INSERT INTO Songs (id, title, artist, level, language) VALUES (?,?,?,?,?)''', [0, name[0], name[1], diff, lang])

    # conn.commit()
    conn.execute('''SELECT * FROM Songs''')
    curs = conn.cursor()
    # print (len(curs.fetchall()))
    for thing in curs:
        print (thing)

    conn.close()

        # http://www.sqlitetutorial.net/sqlite-python/