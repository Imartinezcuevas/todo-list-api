from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.database import SessionLocal
from src.models import Task, User

router = APIRouter()

# Dependencia para obtener la sesión de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Ruta para crear una tarea de prueba y devolver todas las tareas
@router.get("/test-db")
def test_db(db: Session = Depends(get_db)):
    # Crear un usuario de prueba
    new_user = User(email="testuser@example.com", password="1234")
    db.add(new_user)
    db.commit()  # Guardar el usuario en la base de datos

    # Crear una tarea de prueba para el usuario recién creado
    new_task = Task(title="Tarea de prueba", description="Descripción de prueba", completed=False, owner_id=new_user.id)
    db.add(new_task)
    db.commit()  # Guardar la tarea en la base de datos

    # Obtener todas las tareas y devolverlas
    tasks = db.query(Task).all()

    return {"message": "Base de datos funcionando ✅", "tasks": tasks}
