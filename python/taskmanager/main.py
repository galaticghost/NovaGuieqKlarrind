import json
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    while True:
        try:
            with open("task.json", "r") as r:
                json_file = json.load(r)
                break
        except:
            with open("task.json","w") as json_file:
                
                default_data = {
                    "next_id":1,
                    "tasks":[]
                }
                
                json.dump(default_data,json_file)

    while True:
        clear_screen()
        print("1 - List tasks")
        print("2 - Add task")
        print("3 - Update task")
        print("4 - Delete task")
        print("5 - Exit")

        choice = input("Type your choice: ")

        match choice:
            case "1":
                list_tasks(json_file)
            case "2":
                add_task(json_file)
            case "3":
                update_task(json_file)
            case "4":
                delete_task(json_file)
            case "5":
                with open("task.json","w") as file:
                    json.dump(json_file,file)
                exit()
            case _:
                print("XJIGF")

def list_tasks(json_file):
    while True:
        clear_screen()
        print("1 - List all tasks")
        print("2 - List tasks that are done")
        print("3 - List tasks that are not done")
        print("4 - List tasks in progress")
        print("5 - Exit")

        choice = input("Type your choice: ")

        match choice:
            case "1":
                list_all(json_file)
            case "2":
                list_done(json_file)
            case "3":
                list_todo(json_file)
            case "4":
                list_in_progress(json_file)
            case "5":
                return None
            case _:
                continue

def list_all(json_file):
    for task in json_file["tasks"]:
        print(task)
    input("\nPress <<ENTER>> to continue")

def list_todo(json_file):
    check = 0
    for task in json_file["tasks"]:
        if task["status"] == "TODO":
            check = 1
            print(task)
    if check == 0:
        print("There are no task that are not done")
    input("\nPress <<ENTER>> to continue")

def list_in_progress(json_file):
    check = 0
    for task in json_file["tasks"]:
        if task["status"] == "in progress":
            check = 1
            print(task)
    if check == 0:
        print("There are no tasks that are in progress")
    input("\nPress <<ENTER>> to continue")

def list_done(json_file):
    check = 0
    for task in json_file["tasks"]:
        if task["status"] == "done":
            check = 1
            print(task)
    if check == 0:
        print("There are no tasks that are done")
    input("\nPress <<ENTER>> to continue")

def add_task(json_file):
    description = input("Type the description of your task: ")
    
    id = json_file["next_id"]
    
    task = {
        "id":id,
        "description":description,
        "status":'TODO',
        "createdAt":0,
        "updatedAt":0
    }
    
    json_file["next_id"] += 1

    json_file["tasks"].append(task)

    return None

def update_task(json_file): # TODO id not exists
    clear_screen()

    while True:
        print("1 - Update description")
        print("2 - Update status")

        choice = input("Type your choice: ")

        match choice:
            case "1":
                update_task_description(json_file)
                break
            case "2":
                update_task_status(json_file)
                break
            case _:
                continue

def update_task_description(json_file):
    while True:
        try:
            id = int(input("Type the ID of the task: "))
            break
        except:
            clear_screen()
            print("The typed ID is not valid")
            continue
    description = input("Type the new description: ")
    for task in json_file["tasks"]:
        if task["id"] == id:
            task["description"] = description 
            return None
    
    print("There is no task with this ID")
    input("Press <<ENTER>> to continue")
        
def update_task_status(json_file):
    while True:
        try:
            id = int(input("Type the ID of the task: "))
            break
        except:
            clear_screen()
            print("The typed ID is not valid")
            continue
    for task in json_file["tasks"]:
        if task["id"] == id:
            if task["status"] == "TODO":
                task["status"] = "in progress"
            elif task["status"] == "in progress":
                task["status"] = "done"
            else:
                print("The task is already done")
                input("Press <<ENTER>> to continue")
            return None
    
    print("There is no task with this ID")
    input("Press <<ENTER>> to continue")

def delete_task(json_file):
    clear_screen()

    while True:
        try:
            id = int(input("Type the ID of the task:"))
            break
        except:
            clear_screen()
            print("The typed ID is not valid")
            continue
    
    for task in json_file["tasks"]:
        if task["id"] == id:
            json_file["tasks"].pop(json_file["tasks"].index(task))
            return None
    
main()