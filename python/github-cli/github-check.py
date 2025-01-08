import requests
import argparse

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("username", help="The github username of the person you want to check their activity") # TODO
    args = parser.parse_args()

    activity = get_activity(args.username)

    print_activity(activity)

def get_activity(username: str) -> dict | None:
        response = requests.get(f"https://api.github.com/users/{username}/events")
        if response.status_code == 200:
              return response.json()
        else:
            print("error")
            exit()

def print_activity(activity):
      for action in activity:
            user = action["actor"]["display_login"]
            repo = action["repo"]["name"]
            match action["type"]:
                case "PushEvent":
                    print(f"{user} pushed {len(action["payload"]["commits"])} commits to {repo}")
                case "WatchEvent":
                    print(f"{user} started watching {repo}")
                case "CreateEvent":
                    print(f"{user} started {repo}")
                case _:
                    print(action)

main()