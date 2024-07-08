import pika
import json
import logging

# Callback function
def callback(ch, method, properties, body):
    message = json.loads(body)
    logging.info(f"Received message: {message}")

# Consumer function
def consume_messages():
    conn = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = conn.channel()
    channel.queue_declare(queue='test_upwork_queue')

    channel.basic_consume(queue='test_upwork_queue', on_message_callback=callback, auto_ack=True)

    logging.info('Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

# Running the main function
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    consume_messages()