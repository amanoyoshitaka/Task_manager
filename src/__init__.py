import sqlite3


class TaskManager:

    def __init__(self, db_path="database/bd.db"):
        self.db_path = db_path
        self._create_connection()

    def _create_connection(self):
        try:
            self.conn = sqlite3.connect(self.db_path)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print(f"Ошибка подключения к базе данных: {e}")
    # cоздает соединение с базой данных

    def add_task(self, title, description="", status="не выполнено", due_date=None, priority=None, category=None):
        try:
            self.cursor.execute
            ('''
                INSERT INTO tasks (title, description, status, due_date, priority, category)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (title, description, status, due_date, priority, category))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Ошибка при добавлении задачи: {e}")
            return False
        # добавляет задачу в базу данных

    def get_all_tasks(self):
        try:
            self.cursor.execute("SELECT * FROM tasks")
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Ошибка при получении задач: {e}")
            return []
    # возвращает список всех задач

    def update_task_status(self, task_id, new_status):
        try:
            self.cursor.execute('''
                UPDATE tasks
                SET status = ?
                WHERE id = ?
            ''', (new_status, task_id))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Ошибка при обновлении статуса задачи: {e}")
            return False
    # обновляет статус задачи по её ID

    def delete_task(self, task_id):
        try:
            self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Ошибка при удалении задачи: {e}")
            return False
    # удаляет задачу по её ID


    def search_tasks(self, keyword):
        try:
            self.cursor.execute('''
                SELECT * FROM tasks
                WHERE title LIKE ? OR description LIKE ?
            ''', (f"%{keyword}%", f"%{keyword}%"))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Ошибка при поиске задач: {e}")
            return []
    # ищет задачи по ключевым словам в названии и описании

    def filter_tasks_by_status(self, status):
        try:
            self.cursor.execute('''
                SELECT * FROM tasks
                WHERE status = ?
            ''', (status,))
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            print(f"Ошибка при фильтрации задач: {e}")
            return []
    # фильтрует задачи по статусу

    def close(self):
        self.conn.close()
    # закрывает соединение с базой данных