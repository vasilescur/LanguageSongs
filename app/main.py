
#pylint: disable=C0103,C0111,C0304
from flask import Flask, render_template, jsonify, request
# from get_lyrics import song_id
app = Flask(__name__)

class Song:
    def __init__(self, title, artist, level, spot_link, language):
        self.title = title
        self.artist = artist
        self.level = level
        self.spot_link = spot_link
        self.language = language


# A few song ID's for each level
known_music_by_level = {
    '0': [

    ],

    '0+': [

    ],

    '1': [

    ],

    '1+': [

    ],

    '2': [

    ],

    '2+':
    '3':
    '3+':
    '4':
    '4+':
    '5':
}

# TODO: Store known music in a database.
known_music = []

for level, id_list in known_music_by_level.items():
    for song_id in id_list:

        #TODO: Get info from API
        title = "title"
        artist = "artist"
        spot_link = ""
        language = "de_DE"

        known_music.append(Song(
            song_id,
            title,
            artist,
            level,
            spot_link,
            language
        ))

print(known_music[0].title)
print(known_music[0].level)

def find_songs(form):
    songsList = []

    nativeLanguage = form['nativeLanguage']
    songLanguage = form['songLanguage']
    level = form['level']

    print('Searching for level ' + str(level))

    for song in known_music:
        print(song.level)
        print(level.split(','))

        if song.language == songLanguage and song.level in level.split(','):
            songsList.append(song)
        else:
            pass

    return songsList



if __name__ == '__main__':
    print(translate_en_to_de('these words are translated'))


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/findsongs', methods = ['GET','POST'])
def findsongs():
    songList = find_songs(request.args)

    return render_template('song-results.html', songList=songList)


if __name__ == '__main__':
    app.run()
