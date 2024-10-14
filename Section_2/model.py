from mongoengine import Document, StringField, BooleanField, connect

connect('email_sender_db')

class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True, unique=True)
    message_sent = StringField(required=True)
    additional_data = StringField(required=True)

    def __str__(self):
        return f'{self.full_name} <{self.email}>'