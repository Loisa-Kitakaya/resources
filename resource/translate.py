import json
from watson_developer_cloud import LanguageTranslatorV3

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    iam_apikey='-6-QG-NTBvcMI9RMbKPCHaFpXg4lKbQ9pQfq-BNSAprq',
    url='https://gateway-wdc.watsonplatform.net/language-translator/api'
)

text = input ("Enter text to be translated: ")

translation = language_translator.translate(text, model_id='en-fr').get_result()
print(json.dumps(translation, ensure_ascii=False))
print (translation)