import pika
from pika import channel

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

# To make messages durable. Following settings are needed.
#   1. durable = True ---> When creating queue.
#   2. delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE ---> When publishing message
# This will persist messages to disk.
# Even if RabbitMQ service is restarted messages are still available.
# When services restarted queue Hello and messages in Hello are lost.
# while Hello1 and its messages are retrieved back from disk. 
channel.queue_declare('hello1', durable=True)

channel.basic_publish(exchange='', routing_key='hello1', body='Hello RabbitMQ!',
properties=pika.BasicProperties(
    delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
))

connection.close()