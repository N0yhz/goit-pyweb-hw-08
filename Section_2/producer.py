import pika
from faker import Faker
from model import Contact

def send_to_queue(contact_id):
    credentials = pika.PlainCredentials(username = 'n0yhz', password = 'module08')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port = 5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='email_queue', durable=True)

    channel.basic_publish(
        exchange='',
        routing_key='email_queue', 
        body=str(contact_id),
        )
    
    print(f'[x] Contact {contact_id} sent to queue')
    connection.close()

def generate_contacts(count):
    fake = Faker()
    for _ in range(count):
        full_name= fake.name()
        email = fake.email()
        additional_data = fake.text(max_nb_chars=150)

        contact = Contact(
            full_name=full_name,
            email=email,
            additional_data=additional_data
            )
        contact.save()

        send_to_queue('email_queue', contact.id)

if __name__ == '__main__':
    n=10
    generate_contacts(n)