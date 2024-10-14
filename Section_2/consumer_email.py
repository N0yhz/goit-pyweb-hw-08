import pika
from model import Contact

def send_email(contact):
    print(f'Sending email to {contact.email}...')
    return True

def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')
    print(f'[x] Received contact ID {contact_id} for Email')

    contact = Contact.objects(id=contact_id).first()

    if contact:
        if send_email(contact):
            contact.message_sent = True
            contact.save()
            print(f' [x] Email sent contact to {contact.email}, status updated')

    else:
        print(f' [x] Contact with ID {contact.id} not found')

def start_consumer():
    credentials = pika.PlainCredentials(username = 'n0yhz', password = 'module08')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port = 5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='email_queue', durable=True)
    channel.basic_consume(queue='email_queue', on_message_callback=callback, auto_ack=True)
    print('[*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    start_consumer()