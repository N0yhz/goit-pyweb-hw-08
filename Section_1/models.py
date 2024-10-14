from mongoengine import connect, Document, StringField, ReferenceField, ListField

connect(host='mongodb+srv://n0yhz:module08@qouteset1.13lvt.mongodb.net/')

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, reverse_delete_rule='CASCADE')
    quote = StringField(required=True )