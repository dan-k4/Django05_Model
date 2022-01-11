import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person

p = Person(
    first_name = 'John', last_name = 'Sato',
    birthday = '2000-03-03', email='john@gmail.com',
    salary=2000000, memo='memo John', web_site='http://www.john.com'
)
p = Person(
    first_name = 'John', last_name = 'Sato',
    birthday = '2000-03-03', email='john@gmail.com',
    salary=None, memo='memo John', web_site='http://www.john.com'
)
p = Person(
    first_name = 'John', last_name = 'Sato',
    birthday = '2000-03-03', email='john@gmail.com',
    salary=None, memo='memo John', web_site=''
)

# p.save()

# classmethod create
# Person.objects.create(
#     first_name = 'Abe', last_name = 'Sinzo',
#     email='Abechan@gmail.com',
#     salary=123000000, memo='memo Abeabeabe', web_site='http://www.abe.com'
# )

#get_or_create (取得 or 作成)

obj, created = Person.objects.get_or_create(
    first_name = 'Hiroshi', last_name = 'Abe',
    email='Abechan@gmail.com',
    salary=300000, memo='memo Abeabeabe', web_site='http://www.abe.com'
)
print(obj)
print(created)
