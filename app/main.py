
#pylint: disable=C0103,C0111,C0304
from flask import Flask, render_template, jsonify, request

import sqlite3

from get_lyrics import song_lyrics_and_art
from translate_words import get_translate_entry, translate
from fudge_lyrics import fudge

# from get_lyrics import song_id
app = Flask(__name__)

class Song:
    def __init__(self, title, artist, level, language, albumart):
        self.title = title
        self.artist = artist
        self.level = level
        self.language = language
        self.albumart = albumart


def find_songs(form):
    conn = None

    try:
        conn = sqlite3.connect('lyriclehrer.db')
    except:
        print('Failed to connect to database.')
        raise Exception('failed to connect to database')

    songsList = []

    nativeLanguage = form['nativeLanguage']
    songLanguage = form['songLanguage']
    level = form['level']

    print('Searching for level ' + str(level))

    levels_list_str = '('
    for lev in level.split(','):
        levels_list_str += '"' + lev + '", '
    # Remove the last comma
    levels_list_str = levels_list_str[:len(levels_list_str)-2] + ')'

    print(levels_list_str)

    #BUG This is vulnerable to SQL injection if someone manually sets the dropdown
    # value to something malicious. Sue me
    for row in conn.execute('''
            SELECT title, artist, level, language 
            FROM Songs 
            WHERE language = "''' + songLanguage + '''"
                AND level in ''' + levels_list_str + '''
            ;
        '''):
        
        songsList.append(Song(
            row[0], row[1], row[2], row[3], song_lyrics_and_art(row[0], row[1])[1]
        ))

    return songsList


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/findsongs', methods = ['GET','POST'])
def findsongs():
    songList = find_songs(request.args)

    return render_template('song-results.html', songList=songList)


@app.route('/listen', methods = ['GET'])
def listen():
    lyrics = fudge(song_lyrics_and_art(request.args['title'], request.args['artist'])[0])

    # Split lyrics into something like this:

    # <span class="translatable">This</span> <span class="translatable">is</span> ...
    # <br/>
    # ... more words, one word per span
    

    return render_template(
        'listen.html',
        lyrics=lyrics,
        title=request.args['title'],
        artist=request.args['artist']
    )

if __name__ == '__main__':
    app.run(port=80)
