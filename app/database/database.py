from sqlmodel import SQLModel, create_engine

from .models import Post, User  # noqa: F401

engine = create_engine("sqlite:///base_de_datos.db")

if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)
    print("Tables created in database.db")
