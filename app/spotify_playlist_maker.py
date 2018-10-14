from bottle import request
import spotipy
from spotipy import oauth2

SPOTIPY_CLIENT_ID = 'f3472fcb45e74d0a84d01dfd201770f0'
SPOTIPY_CLIENT_SECRET = '782f1ed3d2d344f782f7072bf8b07364'
SPOTIPY_REDIRECT_URI = 'http://localhost:5000'
SCOPE = 'playlist-modify-private,playlist-modify-public'
CACHE = '.spotipyoauthcache'
SP = None


def authenticateCheck():
    global SP
    if SP is not None:
        return None

    access_token = ""
    sp_oauth = oauth2.SpotifyOAuth(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, SPOTIPY_REDIRECT_URI, scope=SCOPE,
                                   cache_path=CACHE)
    token_info = sp_oauth.get_cached_token()

    if token_info:
        access_token = token_info['access_token']
    else:
        url = request.url
        code = sp_oauth.parse_response_code(url)
        if code:
            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']
            
    SP = spotipy.Spotify(access_token)


def get_id(title, artist_name):
    authenticateCheck()

    # iterate through hits of track match
    for hit in SP.search(title, type='track')['tracks']['items']:

        # check if this track is the right track by checking the artist name
        for artist in hit['artists']:
            if artist['name'] == artist_name:
                return get_id_from_uri(hit['uri'])


def get_id_from_uri(uri):
    split_uri = uri.split(":")
    return split_uri[-1]


def make_new_playlist_with_tracks(playlist_name, tracks):
    authenticateCheck()

    # get username of current user
    results = SP.current_user()
    username = get_id_from_uri(results["uri"])

    # create playlist
    SP.user_playlist_create(user=username, name=playlist_name)

    # find new playlist id
    created_playlist_id = ''
    for playlist in SP.user_playlists(user=username)['items']:
        if playlist['name'] == playlist_name:
            created_playlist_id = get_id_from_uri(playlist['uri'])
            break

    # add tracks to new playlist
    track_ids = [get_id(track_name, artist) for track_name, artist in tracks]
    SP.user_playlist_add_tracks(username, created_playlist_id, track_ids)

if __name__ == '__main__':
    song_list = [('I Like It', 'Cardi B'), ('Ring', 'Cardi B'), ('Better Now', 'Post Malone')]
    make_new_playlist_with_tracks('name', song_list)