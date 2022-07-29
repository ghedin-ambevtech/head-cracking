import re
import unicodedata
from ast import Str
from encodings import utf_8
from unicodedata import normalize

from unidecode import unidecode

SYMPTOM_REFRIGERATOR_OFFTRADE = {
    "nao_gela": 60,
    "problem_with_refrigerator_freeze_drinks": 51,
    "porta_nao_fecha": 66,
    "nao_liga": 61,
    # "l?mpada_queimada": 58,
    "lampada_queimada": 58,
    "ruido/barulho": 45,
    # 'geladeira_dando_choque': 46,
    # 'fio_com_mau_contato': 90,
    "problem_with_refrigerator_others": 172,
}


def slugify_text(s, lower=True):
    """
    Creates a slug (ascii) for a given unicode string.
    If the unidecode package is available, an ascii transliteration is done.
    """
    from unicodedata import category, normalize

    normalized = normalize("NFD", s)
    cleaned = "".join([c for c in normalized if category(c) != "Mn"])
    slugified_ascii = re.sub(r"[^A-Za-z0-9_-]", "_", cleaned)

    # if unidecode_available:
    slugified_ascii = re.sub(r"[^A-Za-z0-9_-]", "_", unidecode(cleaned))

    slugified_ascii = re.sub(r"_{2,}", "_", slugified_ascii)

    if lower:
        slugified_ascii = slugified_ascii.lower()

    ### If you prefer to work with a unicode slug, use instead the following:
    # slugified_unicode = u""
    # for c in cleaned:
    #   cat = unicodedata.category(c)
    #   if cat.startswith("L") or cat.startswith("N"):
    #       slugified_unicode += c
    #   else:
    #       slugified_unicode += "_"

    return slugified_ascii


print(slugify_text("n?o_gela"))


# def remover_acentos(txt):
#     return normalize("NFKD", txt).encode("ASCII", "ignore").decode("ASCII")


# def get_open_reason_code_by_symptom_offtrade(symptom: str, device_type: int):
#     if device_type == 6:
#         print(SYMPTOM_REFRIGERATOR_OFFTRADE.get(unidecode(symptom)))


# get_open_reason_code_by_symptom_offtrade(
#     symptom=ascii("l?mpada_queimada"), device_type=6
# )

# lista = ["n?o_gela", "porta_n?o_fecha", "n?o_liga", "l?mpada_queimada", "ru?do/barulho"]

# for item in lista:
#     print(unidecode(item))

# # import unidecode

# # palavra = "programação"
# # palavraSemAcentuacao = unidecode.unidecode(palavra)
# # print(palavraSemAcentuacao)
# # if(palavraSemAcentuacao.find('cao')):
# #   print("Encontrado!")

# # lista = ["n?o_gela", "porta_n?o_fecha", "n?o_liga", "l?mpada_queimada", "ru?do/barulho"]

# # for item in lista:
# #     print(re.sub(r"[^a-zA-Z0-9_ ]", "", item))
# def convert_to_id(s: str):
#     """convert a string to id-like: remove space, remove special accent"""
#     s = s.replace(" ", "")
#     s = s.lower()
#     s = unidecode(s)
#     return s
def remove_diacritics(s):
    """
    Removes diacritics using the `unidecode` package.

    :param: an str or unicode string
    :returns: if bytes: the same string. if str: the unidecoded string.

    >>> remove_diacritics('aéèï')
    'aeei'
    >>> remove_diacritics('aéè'.encode('utf-8'))
    b'a\\xc3\\xa9\\xc3\\xa8'
    """
    if isinstance(s, str):
        # for issue #305
        # because I have no idea what the general solution for this would be
        s = s.replace("’", "'")

        return unidecode(s)
    else:
        return s


print(remove_diacritics("n?o_gela"))


# txto = utf_8.txto
# print(txto)

lista = ["n?o_gela", "porta_n?o_fecha", "n?o_liga", "l?mpada_queimada", "ru?do/barulho"]

for item in lista:
    print(item.encode("utf8"))


def get_open_reason_code_by_symptom_offtrade(
    symptom: str, device_type: int, encoding="utf8"
):
    if device_type == 6:
        print(SYMPTOM_REFRIGERATOR_OFFTRADE.get(unidecode(symptom)))


txto = "não_gela"
get_open_reason_code_by_symptom_offtrade(txto, 6)


def remove_non_ascii_normalized(text: str) -> str:
    normalized = unicodedata.normalize("NFD", text)
    return normalized.encode("ascii", "ignore").decode("utf8").casefold()


print(remove_non_ascii_normalized(txto))
