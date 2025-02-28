from typing import Optional
from src import TaskManager
import datetime


def display_menu():
    print("\n1. Добавить задачу")
    print("2. Показать все задачи")
    print("3. Изменить статус задачи")
    print("4. Удалить задачу")
    print("5. Поиск задач")
    print("6. Фильтрация по статусу")
    print("7. Выход")
# отображает меню для пользователя

def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")
#получает целое число от пользователя

def get_date_input(prompt: str) -> Optional[str]:
    while True:
        date_input = input(prompt)
        if not date_input:
            return None
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            return date_input
        except ValueError:
            print("Ошибка: введите дату в формате ГГГГ-ММ-ДД.")
# получает дату от пользователя в формате ГГГГ-ММ-ДД

def main():
    # основная функция для запуска приложения
    manager = TaskManager()

    while True:
        display_menu()
        choice = get_int_input("Выберите действие: ")

        if choice == 1:
            title = input("Введите название задачи: ")
            description = input("Введите описание задачи: ")
            due_date = get_date_input("Введите срок выполнения (ГГГГ-ММ-ДД, оставьте пустым, если нет): ")
            priority = input("Введите приоритет (низкий, средний, высокий, оставьте пустым, если нет): ")
            category = input("Введите категорию (работа, учеба, личное, оставьте пустым, если нет): ")
            if manager.add_task(title, description, due_date=due_date, priority=priority, category=category):
                print("Задача успешно добавлена!")

        elif choice == 2:
            tasks = manager.get_all_tasks()
            if tasks:
                print("\nСписок задач:")
                for task in tasks:
                    print(
                        f"ID: {task[0]}, Название: {task[1]}, Описание: {task[2]}, Статус: {task[3]}, "
                        f"Срок: {task[4]}, Приоритет: {task[5]}, Категория: {task[6]}"
                    )
            else:
                print("Задачи не найдены.")

        elif choice == 3:
            task_id = get_int_input("Введите ID задачи: ")
            new_status = input("Введите новый статус: ")
            if manager.update_task_status(task_id, new_status):
                print("Статус задачи успешно обновлен!")
            else:
                print("Не удалось обновить статус задачи.")

        elif choice == 4:
            task_id = get_int_input("Введите ID задачи для удаления: ")
            if manager.delete_task(task_id):
                print("Задача успешно удалена!")
            else:
                print("Не удалось удалить задачу.")

        elif choice == 5:
            keyword = input("Введите ключевое слово для поиска: ")
            tasks = manager.search_tasks(keyword)
            if tasks:
                print("\nРезультаты поиска:")
                for task in tasks:
                    print(
                        f"ID: {task[0]}, Название: {task[1]}, Описание: {task[2]}, Статус: {task[3]}, "
                        f"Срок: {task[4]}, Приоритет: {task[5]}, Категория: {task[6]}"
                    )
            else:
                print("Задачи не найдены.")

        elif choice == 6:
            status = input("Введите статус для фильтрации (не выполнено, в процессе, выполнено): ")
            tasks = manager.filter_tasks_by_status(status)
            if tasks:
                print(f"\nЗадачи со статусом '{status}':")
                for task in tasks:
                    print(
                        f"ID: {task[0]}, Название: {task[1]}, Описание: {task[2]}, Статус: {task[3]}, "
                        f"Срок: {task[4]}, Приоритет: {task[5]}, Категория: {task[6]}"
                    )
            else:
                print("Задачи не найдены.")

        elif choice == 7:
            manager.close()
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()