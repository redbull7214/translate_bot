from uuid import uuid4
from sqlalchemy import TIMESTAMP, ForeignKey, create_engine, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (Mapped, declarative_base, mapped_column,
                            relationship, scoped_session, sessionmaker)


engine = create_engine(
    "postgresql+psycopg2://tg_bot_dev:OwOtBdfep9Frut@db_test/tg_bot_dev"
)
session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = session.query_property()


class User(Base):
    """User sqlalchemy model."""

    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        unique=True,
    )

    user_id: Mapped[int] = mapped_column(
        primary_key=True,
        unique=True,
    )

    name: Mapped[str]

    messages: Mapped[list["Message"]] = relationship(
        back_populates="user",
        cascade="all, delete-orphan",
        lazy="joined",
    )

    def __repr__(self):
        """Representation of a string object.

        Returns:
            object: string object
        """
        return "User id: {id}, name: {name}>".format(
            id=self.id,
            name=self.name,
        )


class Message(Base):
    """Message sqlalchemy model."""

    __tablename__ = "message"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
        unique=True,
    )

    text: Mapped[str]
    translated_text: Mapped[str]
    created_at = mapped_column(
        TIMESTAMP,
        server_default=func.current_timestamp(),
        nullable=False,
    )
    user: Mapped["User"] = relationship(
        back_populates="messages",
        lazy="joined",
    )
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    def __repr__(self):
        """Representation of a string object.

        Returns:
            object: string object
        """
        return "Message id: {id}, text: {text}>".format(
            id=self.id,
            text=self.text,
        )


Base.metadata.create_all(bind=engine)
