from argparse import ArgumentParser


parser = ArgumentParser(description='Minimal program that adds 2 numbers')
parser.add_argument('first_number', help='First number to be added together with the second')
parser.add_argument('second_number', help='Second number to be added together with the first')
args = parser.parse_args()


def add(a, b):

    return float(a) + float(b)


print(add(args.first_number, args.second_number))