#pylint: disable=C0103,C0111,C0304


import requests
from bs4 import BeautifulSoup

client_access_token = 'iBz7r0TVf3TSGmozZvTm7W43RRckmj1ZnTPQpMwXrYLbfaQxzPbTsUhgGs5bXs5o'
base_url = "https://api.genius.com"
token = 'Bearer {}'.format(client_access_token)
headers = {'Authorization': token}
# song_title = "Vor Gericht"
# artist_name = "Alligatoah"


def get_song_api_path(song_title, artist_name):
    search_url = base_url + "/search"
    data = {'q': song_title}

    response = requests.get(search_url, data=data, headers=headers)
    json = response.json()

    print(json)

    song_info = None
    for hit in json["response"]["hits"]:
        if hit["result"]["primary_artist"]["name"] == artist_name:
            song_info = hit
            break

    if not song_info:
        return None

    if song_info:
        return song_info["result"]["api_path"]



def song_lyrics_and_art(song_title, artist_name):
    song_api_path = get_song_api_path(song_title, artist_name)

    song_url = base_url + song_api_path
    response = requests.get(song_url, headers=headers)

    json = response.json()

    # return json

    path = json["response"]["song"]["path"]
    page_url = "https://genius.com" + path
    page = requests.get(page_url)

    html = BeautifulSoup(page.text, "html.parser")
    [h.extract() for h in html('script')]

    lyrics = html.find("div", class_="lyrics").get_text()
    lyrics = lyrics.replace(u"\u2018", "'").replace(u"\u2019", "'")

    art = json['response']['song']['header_image_thumbnail_url']

    return (lyrics, art)





# def album_art(song_title, artist_name):
#     song_api_path = get_song_api_path(song_title, artist_name)

#     # return song_api_path

#     song_url = base_url + song_api_path
#     response = requests.get(song_url, headers=headers)

#     json = response.json()

#     path = json["response"]["song"]["path"]
#     page_url = "http://genius.com" + path
#     page = requests.get(page_url)

#     html = BeautifulSoup(page.text, "html.parser")
    
#     src = None
#     try:
#         src = html.find('img', {'class': 'cover_art-image'})['src']
#     except:
#         return ''
    
#     if src is None:
#         return ''






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


def get_language_songs():
    api_key = '307fc6401b9ae0479dc42ced50e35384'

if __name__ == "__main__":
    
    print(song_lyrics_and_art('Rap God', 'Eminem'))