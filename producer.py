import pika
import json
import uuid
import logging
import time

from datetime import datetime


# Reading Delay
def read_delay():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config.get('DELAY', 5)

# Sending Message
def send_message():
    conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = conn.channel()
    channel.queue_declare(queue='test_upwork_queue')

    while True:
        delay = read_delay()
        message_id = str(uuid.uuid4())
        created_on = datetime.now().isoformat()
        message = {
            "message_id": message_id,
            "created_on": created_on
        }
        channel.basic_publish(exchange='',
                              routing_key='test_upwork_queue',
                              body=json.dumps(message)
        )
        logging.info(f"Sent message: {message}")
        time.sleep(delay)


# Running the main function
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    send_message()