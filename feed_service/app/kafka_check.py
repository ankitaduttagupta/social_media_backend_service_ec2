# feed_service/app/kafka_check.py

import asyncio
from aiokafka import AIOKafkaConsumer
from aiokafka.errors import KafkaConnectionError

async def check_kafka():
    consumer = AIOKafkaConsumer(
        "health-check-topic",
        bootstrap_servers="kafka:9092",
        group_id="health-check",
        enable_auto_commit=False
    )
    try:
        await consumer.start()
        print("✅ Kafka is reachable and consumer connected successfully.")
    except KafkaConnectionError as e:
        print(f"❌ Kafka connection failed: {e}")
    finally:
        await consumer.stop()

if __name__ == "__main__":
    asyncio.run(check_kafka())

