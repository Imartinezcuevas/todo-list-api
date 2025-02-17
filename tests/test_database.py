import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import Base
from src.models import User, Task

TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    """Creates a new database session for each test."""
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    try:
        yield session
    finally:
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

def test_user_task_relationship(db_session):
    # Create user
    user = User(email="testuser@example.com", password="hashedpassword")
    db_session.add(user)
    db_session.commit()

    # Create task
    task1 = Task(title="Task 1", description="First task", owner_id=user.id)
    task2 = Task(title="Task 2", description="Second task", owner_id=user.id)
    db_session.add_all([task1, task2])
    db_session.commit()

    # Verify relationship
    db_user = db_session.query(User).filter_by(email="testuser@example.com").first()
    assert len(db_user.tasks) == 2
    assert db_user.tasks[0].title in ["Task 1", "Task 2"]

def test_delete_user_cascades_to_tasks(db_session):
    # Create user and task
    user = User(email="testuser@example.com", password="hashedpassword")
    db_session.add(user)
    db_session.commit()

    task = Task(title="Test Task", description="Test", owner_id=user.id)
    db_session.add(task)
    db_session.commit()

    # Remove user
    db_session.delete(user)
    db_session.commit()

    # Check the task is also deleted 
    tasks = db_session.query(Task).all()
    assert len(tasks) == 0