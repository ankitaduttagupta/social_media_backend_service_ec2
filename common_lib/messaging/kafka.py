# Define file paths

# Kafka utility code

from aiokafka import AIOKafkaProducer
import asyncio
import json
import os

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")

producer = None

async def get_kafka_producer():
    global producer
    if not producer:
        producer = AIOKafkaProducer(
            bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        await producer.start()
    return producer

async def send_event(topic: str, message: dict):
    producer = await get_kafka_producer()
    await producer.send_and_wait(topic, message)

async def close_kafka_producer():
    global producer
    if producer:
        await producer.stop()
        producer = None