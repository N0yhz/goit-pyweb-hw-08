from mongoengine import Document, StringField, BooleanField, connect

connect(host='mongodb+srv://n0yhz:module08@qouteset1.13lvt.mongodb.net/')

class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True, unique=True)
    phone_number = StringField(required=True)  # adding phone number field
    preferred_contact_method = StringField(required=True, choices=["email", "sms"])
    message_sent =BooleanField(default=False)
    additional_data = StringField()
    
    def __str__(self):
        return f'{self.full_name} <{self.email}>'