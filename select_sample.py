import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ModelProject.settings')
from django import setup
setup()

from ModelApp.models import Person

#get all
persons = Person.objects.all()
for person in persons:
    print (person.id, person, person.salary)

print('********************************')

# peron = Person.objects.get(first_name='Abe')
person = Person.objects.get(pk=1)

print(person.id, person)

print('****************************************************************')

# filter(絞り込み、エラーにならない、複数取得可)
persons= Person.objects.filter(first_name = 'John', id = 1).all()
print(persons)

for person in persons:
    print(person.id, person)
    print(persons[0].email)
