import string

from django.utils.crypto import get_random_string

chars = string.ascii_letters + string.digits + string.punctuation + ' '

SECRET_KEY = get_random_string(53, chars)
# print(SECRET_KEY)


# DATABASE_URL = 'postgresql://postgres:postgres@localhost:5432/postgres'




