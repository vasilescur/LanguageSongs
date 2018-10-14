import http.client, uuid, json
import requests

MICROSOFT_TRANSLATE_SUBSCRIPTION_KEY = '910f03d051814b3a87bc85990bad78b6'


def sanitize_german(original):
    new = ""
    for char in original:
        if char == "Ä":
            new = new + "Ae"
        elif char == "ä":
            new = new + "ae"
        elif char == "Ü":
            new = new + "Ue"
        elif char == "ü":
            new = new + "ue"
        elif char == "Ö":
            new = new + "Oe"
        elif char == "ö":
            new = new + "oe"
        elif char == "ß":
            new = new + "ss"
        else:
            new = new + char
    return new

def get_translate_entry(word, original_language, target_language):
    """
    returns link to a translation entry
    at Harper Collins Dictionary if it is there
    otherwise returns None
    """
    lookup = {
        "cs": "czech",
        "da": "danish",
        "de": "german",
        "el": "greek",
        "es": "spanish",
        "et": "estonian",
        "en": "english",
        "fr": "french",
        "it": "italian",
        "nb": "norwegian",
        "nl": "dutch",
        "po": "polish",
        "pt": "portuguese",
        "sl": "slovene",
        "sv": "swedish"
    }
    
    original_language = lookup[original_language[:2]]
    target_language = lookup[target_language[:2]]
    if original_language == 'german':
        word = sanitize_german(word)

    url = 'https://www.collinsdictionary.com/us/dictionary/%s-%s/%s' % (original_language, target_language, word)

    request = requests.get(url)
    if request.status_code == 200:
        return url
    return None


def translate(phrase, original_language, target_language):
    """
    translates phrase (or word) from 
    original language to target language
    """
    phrase = sanitize_german(phrase)
    content = '[{"Text": "%s"}]' % phrase

    target_language = target_language[:2]
    original_language = original_language[:2]

    path_w_params = "/translate?api-version=3.0&to=%s&from=%s" % (target_language, original_language)

    headers = {
        'Ocp-Apim-Subscription-Key': MICROSOFT_TRANSLATE_SUBSCRIPTION_KEY,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
        }

    conn = http.client.HTTPSConnection('api.cognitive.microsofttranslator.com')
    conn.request("POST", path_w_params, content, headers)

    response = conn.getresponse()
    translated = response.read()
    return json.loads(translated)[0]['translations'][0]['text'].lower()


if __name__ == '__main__':
    print(translate('was würde ich noch sagen?', 'de', 'en'))
    print(get_translate_entry('straße', 'de', 'en'))
    