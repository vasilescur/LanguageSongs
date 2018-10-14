#pylint: disable=C0103,C0111,C0304

import requests
from bs4 import BeautifulSoup
client_access_token = 'iBz7r0TVf3TSGmozZvTm7W43RRckmj1ZnTPQpMwXrYLbfaQxzPbTsUhgGs5bXs5o'
base_url = "https://api.genius.com"
token = 'Bearer {}'.format(client_access_token)
headers = {'Authorization': token}
# song_title = "Vor Gericht"
# artist_name = "Alligatoah"


def lyrics_from_song_api_path(song_api_path):
    song_url = base_url + song_api_path
    response = requests.get(song_url, headers=headers)

    json = response.json()

    path = json["response"]["song"]["path"]
    page_url = "https://genius.com" + path
    page = requests.get(page_url)

    html = BeautifulSoup(page.text, "html.parser")
    [h.extract() for h in html('script')]

    lyrics = html.find("div", class_="lyrics").get_text()
    lyrics = lyrics.replace(u"\u2018", "'").replace(u"\u2019", "'")

    return lyrics


def song_lyrics(song_title, artist_name):
    search_url = base_url + "/search"
    data = {'q': song_title}

    response = requests.get(search_url, data=data, headers=headers)
    json = response.json()
    song_info = None
    for hit in json["response"]["hits"]:
        if hit["result"]["primary_artist"]["name"] == artist_name:
            song_info = hit
            break


    if song_info:
        song_api_path = song_info["result"]["api_path"]
        return(lyrics_from_song_api_path(song_api_path))

def get_language_songs():
    api_key = '307fc6401b9ae0479dc42ced50e35384'
    



def song_id(song_title, artist_name):
    search_url = base_url + "/search"
    data = {'q': song_title}

    response = requests.get(search_url, data=data, headers=headers)
    json = response.json()

    song_info = None
    for hit in json["response"]["hits"]:
        if hit["result"]["primary_artist"]["name"] == artist_name:
            song_info = hit
            break

    if not song_info:
        return None
        
    # print (song_info['result'])
    return (song_info['result']['id'])


if __name__ == "__main__":
    listy = [('Du Hast','Rammstein'),('Gewinner','Clueso'),('Komm, gib mir deine Hand','The Beatles'),('Vor Gericht','Alligatoah'),('Es ist noch Suppe Da','Alligatoah')]
    
    for (so, ar) in listy:
        print (song_id(so,ar))
        print(song_lyrics(so,ar))
