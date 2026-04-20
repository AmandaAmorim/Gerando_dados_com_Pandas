import unicodedata

def remove_accents(text):
    nfkd_form = unicodedata.normalize('NFKD', text)

    return "".join([c for c in nfkd_form if not unicodedata.combining(c)]).strip().replace(" ", "")
