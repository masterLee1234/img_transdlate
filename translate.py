from googletrans import Translator

def trl(text):
    translator = Translator()
    result = translator.translate(text, dest="ko")
    return result.text