from sqlalchemy.future import select
from app.models.feed import Feed

async def get_feed(user_id: str, db):
    result = await db.execute(select(Feed).where(Feed.user_id == user_id))
    return result.scalars().all()
'''
async def create_feed(feed_data: FeedCreate, db):
    new_feed = Feed(
        user_id=feed_data.user_id,
        media_id=feed_data.media_id,
        file_url=feed_data.file_url
    )
    db.add(new_feed)
    await db.commit()
    await db.refresh(new_feed)
    return new_feed
'''
