import asyncio
import json
import uuid
from aiokafka import AIOKafkaConsumer
from app.db.database import SessionLocal
from app.models.feed import Feed
import os

KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")

async def consume_media_uploaded():
    consumer = AIOKafkaConsumer(
        'media.uploaded',
        bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS,
        group_id='feed-group',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )
    await consumer.start()
    try:
        async for msg in consumer:
            payload = msg.value
            async with SessionLocal() as db:
                feed_item = Feed(
                    id=str(uuid.uuid4()),
                    user_id=payload['user_id'],
                    media_id=payload['media_id'],
                    file_url=payload['file_url']
                )
                db.add(feed_item)
                await db.commit()
    finally:
        await consumer.stop()