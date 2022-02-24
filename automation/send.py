import pika
from pika import channel

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

channel.queue_declare('hello1', durable=True)

channel.basic_publish(exchange='', routing_key='hello1', body='Hello RabbitMQ!',
properties=pika.BasicProperties(
    delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
))

connection.close()