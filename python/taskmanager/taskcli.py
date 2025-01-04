import json
import argparse
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

parser = argparse.ArgumentParser()
parser.add_argument("echo", help="Echo the think you typed", type=int)
parser.add_argument("-x", "--xinamen", help="XINAMEN!!!!!",action="store_true")

subs = parser.add_subparsers()

sus = subs.add_parser('a')
sus.add_argument("xs")


args = parser.parse_args()
print(args.echo ** 2)
print(args.xs)
if args.xinamen:
    print("XINAMEN ON!")