from typing import Callable
import argparse
import json
import os

def main() -> None:
    args = get_queries()

    DATABASE_LOCATION: str = os.path.expanduser("~/task.json")

    database: dict = load_database(DATABASE_LOCATION)

    match args.command:
        case "add":
            add_task(database,args.description)
        case "update":
            update_task(database,args.id,args.description)
        case "delete":
            delete_task(database,args.id)
        case "list":
            list_all(database)

    save_database(database,DATABASE_LOCATION)

def load_database(path: str) -> dict:
    try:
        with open(path,"r") as json_file:
            database = json.load(json_file)
    except:
        database = {
            "next_id":1,
            "tasks":[]
        }

    return database   

def save_database(database: dict, location: str) -> None:
    with open(location,"w") as path:
        json.dump(database,path)

def get_queries():
    parser = argparse.ArgumentParser()

    sub_parsers = parser.add_subparsers(dest="command",required="true")

    add = sub_parsers.add_parser('add', help="Add a task")
    add.add_argument("description", help="The description of the task")

    update = sub_parsers.add_parser('update',help="Update a task")
    update.add_argument("id",help="The id of the task")
    update.add_argument("description",help="The description of the task")

    delete = sub_parsers.add_parser("delete", help="Delete a task")
    delete.add_argument("id",help="The id of the task")

    list_task = sub_parsers.add_parser("list", help="List tasks")
    list_task.add_argument("-a","--all",help="List all tasks")
    list_task.add_argument("-t","--todo",help="List all tasks that are not done")
    list_task.add_argument("-i","--in-progress",help="List all tasks that are in progress")
    list_task.add_argument("-d","--done",help="List all tasks that are done")

    args = parser.parse_args()

    return args

def list_all(json_file):
    for task in json_file["tasks"]:
        print(task)

def list_todo(json_file):
    check = 0
    for task in json_file["tasks"]:
        if task["status"] == "TODO":
            check = 1
            print(task)
    if check == 0:
        print("There are no task that are not done")

def list_in_progress(json_file):
    check = 0
    for task in json_file["tasks"]:
        if task["status"] == "in progress":
            check = 1
            print(task)
    if check == 0:
        print("There are no tasks that are in progress")

def list_done(json_file):
    check = 0
    for task in json_file["tasks"]:
        if task["status"] == "done":
            check = 1
            print(task)
    if check == 0:
        print("There are no tasks that are done")

def add_task(json_file: dict, description: str) -> None:
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

def update_task(json_file: dict, id: int, description: str) -> None:
    for task in json_file["tasks"]:
        if task["id"] == id:
            task["description"] = description 
            return None
    print(f"No task with id {id} was found")
        
def update_task_status(json_file):
    while True:
        try:
            id = int(input("Type the ID of the task: "))
            break
        except:
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

def delete_task(json_file: dict,id:int) -> None:
    for task in json_file["tasks"]:
        if task["id"] == id:
            json_file["tasks"].pop(json_file["tasks"].index(task))
            return None
    print(f"No task with id {id} was found")
    
if __name__ == "__main__":
    main()