import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost')
)
channel = connection.channel()

channel.queue_declare('hello')

have_msgs = True

while have_msgs:
    method, properties, body = channel.basic_get('hello')

    if method:
        print('*********************************')
        print(f'method: {method} -- properties: {properties} -- body: {body}')
        channel.basic_ack(method.delivery_tag)
    else:
        have_msgs = False


channel.close()
connection.close()


def get_limited_messages():
    for method, properties, body in channel.consume('hello'):
        print(f'method: {method} -- properties: {properties} -- body: {body}')
        channel.basic_ack(method.delivery_tag)

        if method.delivery_tag == 3:
            break

    requeued_messages = channel.cancel()