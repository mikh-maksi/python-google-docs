import googletrans
from googletrans import Translator

trans = googletrans.Translator()

# trans.translate("Привіт")

# print(googletrans.LANGUAGES)

intxt = "Привіт"

trans.text = "Привіт"

print(trans)

# print(trans.detect(intxt))

# print(translator.translate("привіт", src = 'uk', dest = 'pl'))
