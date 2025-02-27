import pika


def my_callback(ch, method, properties, body):
    print(body)
    print(type(body))


connection_parameters = pika.ConnectionParameters(
    host="localhost",
    port=5672,
    credentials=pika.PlainCredentials(
        username="*********",
        password="*********"
    )
)

channel = pika.BlockingConnection(connection_parameters).channel()
channel.queue_declare(
    queue="data_queue",
    durable=True
)

channel.basic_consume(
    queue="data_queue",
    auto_ack=True,
    on_message_callback=my_callback
)

print(f'Listen RabbitMQ on Port 5672')
channel.start_consuming()
