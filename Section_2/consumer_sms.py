import pika
from model import Contact

def send_sms(contact):
    print(f'Sending SMS to {contact.phone_number}...')
    return True

def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')
    print(f'[x] Received contact ID {contact_id} for SMS')

    contact = Contact.objects(id=contact_id).first()

    if contact:
        if send_sms(contact):
            contact.message_sent = True
            contact.save()
            print(f' [x] SMS sent contact to {contact.phone_number}, status updated')

    else:
        print(f' [x] Contact with ID {contact.id} not found')

def start_consumer():
    credentials = pika.PlainCredentials(username = 'n0yhz', password = 'module08')
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', port = 5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='sms_queue', durable=True)
    channel.basic_consume(queue='sms_queue', on_message_callback=callback, auto_ack=True)
    print('[*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    start_consumer()