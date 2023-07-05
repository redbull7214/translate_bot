from sqlalchemy import select
from db import Message, User, session


async def select_user(user_id: int) -> User | None:
    """Select user from DB.

    Args:
        user_id: int

    Returns:
        object: User or None
    """
    query = session.execute(
        select(User).where(User.user_id == int(user_id)),
    )
    return query.scalar()


async def get_messages(user_id: str) -> list[Message] or None:
    """Select 10 messages from DB.

    Args:
        user_id: int

    Returns:
        object: list[Message] or None
    """
    query = (
        session.query(Message)
        .where(Message.user_id == user_id)
        .order_by(Message.created_at.desc())
        .limit(10)
        .all()
    )
    return query


async def create_user(user_id: int, name: str) -> User | None:
    """Create new user to DB.

    Args:
        user_id: int
        name: str

    Returns:
        object: User or None
    """

    user = User(
        user_id=user_id,
        name=name,
    )
    session.add(user)
    session.commit()
    session.refresh(user)

    return user


async def save_message(text: str, translated_text: str, user_id: str) -> Message:
    """Create new message to DB.

    Args:
        text: str
        translated_text: str
        user_id: str
    Returns:
        object: User or None
    """
    message = Message(
        user_id=user_id,
        text=text,
        translated_text=translated_text
    )
    session.add(message)
    session.commit()
    session.refresh(message)
    return message
