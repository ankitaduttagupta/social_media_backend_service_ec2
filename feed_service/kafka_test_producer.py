# kafka_test_producer.py
from aiokafka import AIOKafkaProducer
import asyncio

async def send():
    producer = AIOKafkaProducer(bootstrap_servers="kafka:9092")
    await producer.start()
    try:
        await producer.send_and_wait("media_uploaded", b"Test message")
        print("Message sent!")
    finally:
        await producer.stop()

asyncio.run(send())

