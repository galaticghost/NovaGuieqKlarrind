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
            print("ERROR: the user has not been found")
            exit()

def print_activity(activity) -> None:
      for action in activity:
            user = action["actor"]["display_login"]
            repo = action["repo"]["name"]
            match action["type"]:
                case "PushEvent":
                    print(f"- {user} pushed {len(action["payload"]["commits"])} commits to {repo}")
                case "WatchEvent":
                    print(f"- {user} started watching {repo}")
                case "CreateEvent":
                    print(f"- {user} started {repo}")
                case "DeleteEvent":
                    print(f"- {user} has delete {repo}")
                case "ForkEvent":
                    print(f"- {user} has forked {repo}")
                case "GollumEvent":
                    print(f"- {user} has updated a wiki on {repo}")
                case "IssueCommentEvent":
                    print(f"- {user} has comment on {repo}")
                case "IssuesEvent":
                    print(f"- {user} has issue on {repo}")
                case "MemberEvent":
                    print(f"- {user} has accepted {action["payload"]["member"]} at {repo}")
                case "PublicEvent":
                    print(f"- {user} has made {repo} public")
                case "PullRequestEvent":
                    print(f"- {user} has made a pull request at {repo}")
                case "PullRequestReviewEvent":
                    print(f"- {user} has review a pull request at {repo}")
                case "PullRequestReviewCommentEvent":
                    print(f"- {user} has made a comment at {repo} ")
                case "PullRequestReviewThreadEvent":
                    print(f"- {user} has marked {action["payload"]["thread"]} as {action["payload"]["action"]}")
                case "ReleaseEvent":
                    print(f"- {user} released at {repo}")
                case "SponsorshipEvent":
                    print(f"- {user} has started sponsoring {repo}")
main()