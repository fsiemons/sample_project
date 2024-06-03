from argparse import ArgumentParser


parser = ArgumentParser(description='Useless program that makes you answer your own questions')
parser.add_argument('question', help='a string that will be asked')
args = parser.parse_args()

answer = input(f"Your question today is:\n{args.question}?\n")

print(f"You answered with:\n{answer}")
