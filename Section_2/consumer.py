import pika
from model import Contact

def send_email(contact):
    print(f'Sending email to {contact.email}...')

def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')
    print(f'[x] Received contact ID {contact_id}')

    contact = Contact.objects.get(id=contact_id).first()

    if contact:
        if send_email(contact):
            contact.message_sent = True
            contact.save()
            print(f' [x] Email sent contact to {contact.email}, status updated')

    else:
        print(f' [x] Contact with ID {contact.id} not found')

def start_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='email_queue', durable=True)
    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)
    print('[*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    start_consumer()