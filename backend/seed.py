from app.core.database import SessionLocal
from app.models.todo import Todo
from datetime import datetime, timedelta

def create_mock_todos():
    mock_todos = [
        Todo(
            title="買い物に行く",
            description="牛乳と卵を買う",
            start_date=datetime.now(),
            end_date=datetime.now() + timedelta(days=1),
            completed=False,
            created_at=datetime.now(),
            updated_at=datetime.now()
        ),
        Todo(
            title="レポート作成",
            description="月次報告書をまとめる",
            start_date=datetime.now() + timedelta(days=1),
            end_date=datetime.now() + timedelta(days=3),
            completed=False,
            created_at=datetime.now(),
            updated_at=datetime.now()
        ),
        Todo(
            title="ランニング",
            description="5km走る",
            start_date=datetime.now() + timedelta(hours=2),
            end_date=datetime.now() + timedelta(hours=3),
            completed=True,
            created_at=datetime.now(),
            updated_at=datetime.now()
        ),
    ]

    with SessionLocal() as db:
        for todo in mock_todos:
            db.add(todo)
        db.commit()
        print(f"Added {len(mock_todos)} mock todos.")

if __name__ == "__main__":
    create_mock_todos()
