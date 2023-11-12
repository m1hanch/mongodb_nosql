import json

from bson.objectid import ObjectId
from mongoengine import *

connect(db='hw8',
        host='mongodb+srv://mihanch:mihaJ0107@cluster0.xo49jrs.mongodb.net/')


class Authors(Document):
    fullname = StringField(max_length=120, required=True)
    born_date = DateField()
    born_location = StringField(max_length=120)
    description = StringField(max_length=5000)
    meta = {'collection': 'authors'}


class Quotes(Document):
    tags = ListField(StringField(max_length=30))
    author = ReferenceField('Authors')
    quote = StringField(max_length=200)
    meta = {'collection': 'quotes'}


if __name__ == '__main__':
    with open('authors.json', 'r') as f:
        data = json.load(f)
    authors = [Authors(**item) for item in data]
    Authors.objects.insert(authors)

    with open('quotes.json', 'r') as f:
        data = json.load(f)
    quotes = [Quotes(**item) for item in data]
    Quotes.objects.insert(quotes)
