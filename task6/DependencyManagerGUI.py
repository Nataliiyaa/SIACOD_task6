import tkinter as tk


class DependencyManagerGUI:
    def __init__(self, root, app):

        self.root = root  # корневое окно приложения
        self.app = app  # ссылка на основное приложение для вызова методов

        # Поля ввода для добавления зависимости
        self.input_frame = tk.Frame(root)
        self.input_frame.pack(pady=5)

        self.parent_label = tk.Label(self.input_frame, text="Родитель:")
        self.parent_label.grid(row=0, column=0, padx=5)
        self.parent_entry = tk.Entry(self.input_frame, width=20)
        self.parent_entry.grid(row=0, column=1, padx=5)

        self.child_label = tk.Label(self.input_frame, text="Зависимые (через запятую):")
        self.child_label.grid(row=0, column=2, padx=5)
        self.child_entry = tk.Entry(self.input_frame, width=30)
        self.child_entry.grid(row=0, column=3, padx=5)

        self.add_button = tk.Button(
            self.input_frame, text="Добавить зависимость", command=self.add_dependency
        )
        self.add_button.grid(row=0, column=4, padx=5)

        # Поле для показа зависимостей
        self.label = tk.Label(root, text="Список зависимостей:")
        self.label.pack(pady=5)

        self.text_input = tk.Text(root, width=60, height=15)
        self.text_input.pack(pady=5)

        # Кнопки действий
        self.actions_frame = tk.Frame(root)
        self.actions_frame.pack(pady=10)

        self.sort_button = tk.Button(
            self.actions_frame, text="Выполнить сортировку", command=self.app.perform_sort
        )
        self.sort_button.grid(row=0, column=0, padx=5)

        self.clear_button = tk.Button(
            self.actions_frame, text="Очистить список", command=self.app.clear_dependencies
        )
        self.clear_button.grid(row=0, column=1, padx=5)

        self.example_button = tk.Button(
            self.actions_frame, text="Загрузить примеры", command=self.app.load_examples
        )
        self.example_button.grid(row=0, column=2, padx=5)

    def add_dependency(self):
        parent = self.parent_entry.get().strip()
        children = self.child_entry.get().strip()
        self.app.add_dependency(parent, children)

        self.parent_entry.delete(0, tk.END)
        self.child_entry.delete(0, tk.END)

    def update_dependency_list(self, entry):
        self.text_input.insert(tk.END, entry)

    def clear_list(self):
        self.text_input.delete("1.0", tk.END)

    def load_example(self, examples):
        self.clear_list()
        for parent, children in examples.items():
            entry = f"{parent} -> {', '.join(children)}\n"
            self.update_dependency_list(entry)
