import pika
from pika import channel

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)

channel = connection.channel()

channel.queue_declare('hello')

channel.basic_publish(exchange='', routing_key='hello', body='Hello RabbitMQ!')

connection.close()