from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: int | None = Field(default=None, primary_key=True)
    given_name: str
    family_name: str
    email: str = Field(unique=True, index=True)
    phone_number: str = None
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(
        default_factory=datetime.now,
        sa_column_kwargs={"onupdate": datetime.now},
    )

    posts: Post = Relationship(back_populates="user")
    #comments: Comment = Relationship(back_populates="user")

class Post(SQLModel, table=True):
    __tablename__ = "posts"

    id: int = Field(default=None, primary_key=True)
    title: str
    content: str
    user_id: int = Field(foreign_key="users.id")
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(
        default_factory=datetime.now,
        sa_column_kwargs={"onupdate": datetime.now},
    )

    user: User = Relationship(back_populates="posts")

