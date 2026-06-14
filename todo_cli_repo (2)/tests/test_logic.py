from app.logic import add_task

def test_add_task():
    tasks = []
    add_task(tasks, "test")
    assert len(tasks) == 1
