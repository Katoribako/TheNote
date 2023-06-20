from Notebook import Notebook


def print_instructions():
    print("Команды:")
    print("add - добавить новую заметку")
    print("edit - редактировать существующую заметку")
    print("delete - удалить существующую заметку")
    print("delete_all - удалить все заметки")
    print("list - вывести список всех заметок")
    print("view - просмотреть содержимое конкретной заметки")
    print("exit - выйти из программы")


def input_command(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in ["add", "edit", "delete", "delete_all", "list", "view",
                     "exit", "yes", "no"]:
            return value
        else:
            print("Ошибка: введите корректную команду.")


def input_id(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        else:
            print("Ошибка: введите целое положительное число.")


def main():
    notebook = Notebook("notes.json")
    notebook.load_notes()
    print("Добро пожаловать в приложение Заметки!")
    print_instructions()

    while True:
        command = input_command("Введите команду (add, edit, delete, "
                                "delete_all, list, view, exit): ")

        if command == "add":
            title = input("Введите заголовок заметки: ")
            content = input("Введите содержание заметки: ")
            notebook.add_note(title, content)
            notebook.save_notes()
            last_note_id = notebook.get_last_note_id()
            print(f"Заметка успешно добавлена. ID: {last_note_id}")

        elif command == "edit":
            id = input_id("Введите ID заметки: ")
            title = input("Введите новый заголовок заметки: ")
            content = input("Введите новое содержание заметки: ")
            notebook.edit_note(id, title, content)
            notebook.save_notes()

        elif command == "delete":
            id = input_id("Введите ID заметки: ")
            notebook.delete_note(id)
            notebook.save_notes()

        elif command == "delete_all":
            confirm = input_command(
                "Вы уверены, что хотите удалить все заметки? (yes/no): ")
            if confirm.lower() == "yes":
                notebook.delete_all_notes()
                notebook.save_notes()
                print("Все заметки успешно удалены.")
            else:
                print("Удаление заметок отменено.")


        elif command == "list":
            notebook.display_notes()

        elif command == "view":
            id = input_id("Введите ID заметки: ")
            note = notebook.get_note_by_id(id)
            if note:
                print(f"{note.title}\n{note.content}")
            else:
                print("Заметка не найдена")

        elif command == "exit":
            print("Программа закончила работу")
            break

        else:
            print(
                "Ошибка: неверная команда. Пожалуйста"
                ", введите корректную команду.")


if __name__ == "__main__":
    main()
