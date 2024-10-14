import pika
from faker import Faker
from model import Contact
import random

def send_to_queue(queue_name, contact_id):
    credentials = pika.PlainCredentials(username = 'n0yhz', password = 'module08')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port = 5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name, durable=True)

    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=str(contact_id),
        properties=pika.BasicProperties(
            delivery_mode=2, 
        )
    )
    print(f" [x] Sent contact ID {contact_id} to queue {queue_name}")

    connection.close()

def generate_contacts(count):
    fake = Faker()
    for _ in range(count):
        full_name = fake.name()
        email = fake.email()
        phone_number = fake.phone_number()
        additional_data = fake.text(max_nb_chars=200)
        preferred_contact_method = random.choice(["email", "sms"])

        contact = Contact(
            full_name=full_name,
            email=email,
            phone_number=phone_number,
            preferred_contact_method=preferred_contact_method,
            additional_data=additional_data
        )
        contact.save()

        print(f"Sending contact {contact.id} via {preferred_contact_method}")

        if preferred_contact_method == "email":
            print(f"Sending to email_queue: {contact.id}")
            send_to_queue('email_queue', contact.id) 
        else:
            print(f"Sending to sms_queue: {contact.id}")
            send_to_queue('sms_queue', contact.id)    

if __name__ == "__main__":
    n = 10 
    generate_contacts(n)