from sqlalchemy.pool import StaticPool
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine,text
from database import Base
import pytest
from fastapi.testclient import TestClient
from main import app
from models import Todos,Users
from routers.auth import bcrypt_context




# ----- Create a separate in-memory SQLite database for testing -----
SQLALCHEMY_TEST_DATABASE_URL = "sqlite:///./test_db.db"

engine = create_engine(
    SQLALCHEMY_TEST_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool
)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Create all tables in the test database
Base.metadata.create_all(bind=engine)

# ----- Dependency overrides -----
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

def override_get_current_user():
    return {"username": "Moana", "id": 1, "user_role": "admin"}

# ----- TestClient -----
client = TestClient(app)

@pytest.fixture
def test_todo():
    todo = Todos(
        title = 'Learn Sqlalchemy',
        description = 'To complete fastapi',
        priority = 5,
        complete = False,
        owner_id = 1
    )

    db = TestingSessionLocal()
    db.add(todo)
    db.commit()
    yield todo
    with engine.connect() as connection:
        connection.execute(text('DELETE FROM todos;'))
        connection.commit()



@pytest.fixture
def test_user():
    user = Users(
        username = 'abc',
        email = 'abc@gmail.com',
        first_name = 'ABC',
        last_name = 'DEF',
        hashed_password = bcrypt_context.hash("abc"),
        role = 'admin',
        phone_number = '9874562310'
    )

    db = TestingSessionLocal()
    db.add(user)
    db.commit()
    yield user
    with engine.connect() as connection:
        connection.execute(text('DELETE FROM users;'))
        connection.commit()
