import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import Base, get_db
from src.models import User, Task

TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """Creates a new database session for each test."""
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_create_user(db_session):
    new_user = User(email="testuser@example.com", password="hashedpassword")
    db_session.add(new_user)
    db_session.commit()

    user = db_session.query(User).filter(User.email == "testuser@example.com").first()

    assert user is not None
    assert user.email == "testuser@example.com"
    assert user.password == "hashedpassword"

def test_create_task(db_session):
    new_user = User(email="testuser@example.com", password="hashedpassword")
    db_session.add(new_user)
    db_session.commit()

    task = Task(title="Test Task", description="This is a test task", completed=False, owner_id=new_user.id)
    db_session.add(task)
    db_session.commit()

    retrieved_task = db_session.query(Task).filter(Task.title=="Test Task").first()

    assert retrieved_task is not None
    assert retrieved_task.title == "Test Task"
    assert retrieved_task.description == "This is a test task"
    assert retrieved_task.completed == False
    assert retrieved_task.owner_id == new_user.id