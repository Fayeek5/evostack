from app.database.database import (
    engine
)

from app.database.models import Base


def initialize_database():

    Base.metadata.create_all(
        bind=engine
    )


if __name__ == "__main__":

    initialize_database()

    print("Database initialized")
