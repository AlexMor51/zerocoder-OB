class Task():
    def __init__(self):
        self.tasks=[]

    #добавление задач в список
    def add_tasks(self,deddline,description):
        self.tasks.append({"deddline":deddline,"description":description,"status":"Не выполнено"})

    #выполнение задачи из списка
    def complete_tasks(self,description):
        print()
        for task in self.tasks:
            if task["description"]==description:
                task["status"]="Выполнено"
                print(f"Задача {description} выполнена")

    def not_complete_tasks(self):
        print()
        print("Не выполненные задачи")
        for task in self.tasks:
            if task["status"] == "Не выполнено":
                print(f"{task['description']}-{task['deddline']}")
            else:
                pass


    def show_tasks(self):
        print("Текущие задачи")
        for task in self.tasks:
            print(f"{task['description']}-{task['deddline']}")


t=Task()
t.add_tasks("08:00","Поесть")
t.add_tasks("09:00","Поспать")
t.add_tasks("10:00","Сделать ДЗ")
t.show_tasks()
t.complete_tasks("Поесть")
t.not_complete_tasks()
