from tkinter import messagebox

from DependencyGraph import DependencyGraph
from DependencyManagerGUI import DependencyManagerGUI


class DependencyManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Менеджер зависимостей")

        self.graph = DependencyGraph()
        self.gui = DependencyManagerGUI(root, self)

    def add_dependency(self, parent, children):
        if not parent:
            messagebox.showerror("Ошибка", "Введите название родительской библиотеки.")
            return

        if not children:
            messagebox.showerror("Ошибка", "Введите названия зависимых библиотек.")
            return

        children_list = [child.strip() for child in children.split(",") if child.strip()]

        for child in children_list:
            if parent == child:
                messagebox.showerror("Ошибка", "Библиотека не может зависеть сама от себя.")
                return

        for child in children_list:
            if self.graph.has_dependency(parent, child):
                messagebox.showerror("Ошибка", f"Зависимость {parent} -> {child} уже существует.")
                return

        # Добавление зависимостей
        for child in children_list:
            self.graph.add_dependency(parent, [child])

        self.gui.update_dependency_list(f"{parent} -> {', '.join(children_list)}\n")

    def clear_dependencies(self):
        self.graph.clear()
        self.gui.clear_list()

    def perform_sort(self):
        try:
            order = self.graph.tarjan_algorithm()
            messagebox.showinfo("Результат", f"Порядок установки: {', '.join(order)}")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Произошла ошибка: {e}")

    def load_examples(self):
        examples1 = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["D", "E"],
            "D": ["F"],
            "E": ["F"],
        }
        examples2 = {
            "A":  ["B", "C", "D"],
            "B": ["E"],
            "E": ["F", "G"],
            "C": ["G", "H"]
        }
        self.graph = DependencyGraph()
        for parent, children in examples2.items():
            self.graph.add_dependency(parent, children)

        self.gui.load_example(examples2)