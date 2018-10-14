#import google.cloud
from google.cloud import translate
# $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\Chily\Downloads\word scanner-164ec7ebaab9.json"
# $env:GOOGLE_APPLICATION_CREDENTIALS="C:\Users\Chily\Downloads\word scanner-164ec7ebaab9.json"
# set GOOGLE_APPLICATION_CREDENTIALS= C:\Users\Chily\Downloads\word scanner-164ec7ebaab9.json
#set (GOOGLE_APPLICATION_CREDENTIALS=[PATH])
client = translate.Client(target_language='en')
result = client.translate("ich", source_language = 'de')
print(result)
