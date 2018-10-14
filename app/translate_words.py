import http.client, uuid, json

SUBSCRIPTION_KEY = '910f03d051814b3a87bc85990bad78b6'


def translate(word, original_language, target_language):
    """
    translates word from original language to target language
    """
    content = '[{"Text": "%s"}]' % word

    target_language = target_language[:2]
    original_language = original_language[:2]

    path_w_params = "/translate?api-version=3.0&to=%s&from=%s" % (target_language, original_language)

    headers = {
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
        }

    conn = http.client.HTTPSConnection('api.cognitive.microsofttranslator.com')
    conn.request("POST", path_w_params, content, headers)

    response = conn.getresponse()
    translated = response.read()
    return json.loads(translated)[0]['translations'][0]['text'].lower()


if __name__ == '__main__':
    print(translate('hello', 'en-US', 'de-DE'))
    