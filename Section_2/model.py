from mongoengine import Document, StringField, BooleanField, connect

connect(host='mongodb+srv://n0yhz:module08@qouteset1.13lvt.mongodb.net/')

class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True, unique=True)
    message_sent =BooleanField(default=False)
    additional_data = StringField()
    
    def __str__(self):
        return f'{self.full_name} <{self.email}>'