import pytest
from src import TaskManager


@pytest.fixture
def task_manager():
    """Фикстура для создания экземпляра TaskManager с подключением к вашей базе данных."""
    # Укажите путь к вашей базе данных
    db_path = "F:/Projects/Company/database/bd.db"  # Замените на реальный путь к вашей базе данных
    manager = TaskManager(db_path=db_path)
    yield manager
    manager.close()


def test_add_task(task_manager):
    """Тест для добавления задачи."""
    task_manager.add_task("Test Task", "Test Description")
    tasks = task_manager.get_all_tasks()
    assert len(tasks) >= 1  # Проверяем, что задача добавлена
    assert tasks[-1][1] == "Test Task"  # Проверяем последнюю добавленную задачу
    assert tasks[-1][2] == "Test Description"
    assert tasks[-1][3] == "не выполнено"


def test_update_task_status(task_manager):
    """Тест для обновления статуса задачи."""
    # Добавляем задачу для теста
    task_manager.add_task("Test Task", "Test Description")
    tasks = task_manager.get_all_tasks()
    task_id = tasks[-1][0]  # Берем ID последней добавленной задачи

    # Обновляем статус
    task_manager.update_task_status(task_id, "в процессе")
    updated_task = task_manager.get_all_tasks()[-1]  # Проверяем последнюю задачу
    assert updated_task[3] == "в процессе"


def test_delete_task(task_manager):
    """Тест для удаления задачи."""
    # Добавляем задачу для теста
    task_manager.add_task("Test Task", "Test Description")
    tasks = task_manager.get_all_tasks()
    task_id = tasks[-1][0]  # Берем ID последней добавленной задачи

    # Удаляем задачу
    task_manager.delete_task(task_id)
    tasks = task_manager.get_all_tasks()
    assert task_id not in [task[0] for task in tasks]  # Проверяем, что задачи больше нет


def test_search_tasks(task_manager):
    """Тест для поиска задач."""
    # Добавляем задачу для теста
    task_manager.add_task("Test Task", "Test Description")
    tasks = task_manager.search_tasks("Test")
    assert len(tasks) >= 1  # Проверяем, что задача найдена
    assert tasks[-1][1] == "Test Task"  # Проверяем последнюю найденную задачу


def test_filter_tasks_by_status(task_manager):
    """Тест для фильтрации задач по статусу."""
    # Добавляем задачи для теста
    task_manager.add_task("Test Task 1", "Test Description 1", status="не выполнено")
    task_manager.add_task("Test Task 2", "Test Description 2", status="в процессе")

    # Фильтруем задачи по статусу
    tasks = task_manager.filter_tasks_by_status("в процессе")
    assert len(tasks) >= 1  # Проверяем, что задача найдена
    assert tasks[-1][1] == "Test Task 2"  # Проверяем последнюю найденную задачу