from random import SystemRandom
import string
from django.utils.text import slugify # slugfy transforma string em string url

def random_letters(k=5):
    return ''.join(SystemRandom().choices(
        string.ascii_lowercase + string.digits,
        k=k
    ))
def slugify_new(text, k=5):
    return slugify(text) + '' + random_letters(k)

print(slugify_new('blá blá blá blá blá'))