import argparse
import sys

# parser = argparse.ArgumentParser()
# parser.parse_args()
# parser.add_argument("echo", help="echo the string you user here")
# args = parser.parse_args()
# print(args)

# parser.add_argument("square", help="display a square of a given number", type=int)
# args = parser.parse_args()
# print(args.square**2)

# parser.add_argument("--verbosity", help="increase output verbosity")
# args = parser.parse_args()
# if args.verbosity:
#     print("versbosity turned on")

# parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
# args = parser.parse_args()
# if args.verbose:
#     print("versbosity turned on")

parser = argparse.ArgumentParser(
    prog="Rasa",
    description="project name",
    epilog="Text at the bottom of help"
)
parser.add_argument('filename')
parser.add_argument('-c', '--count')
parser.add_argument('-v', '--verbose', action='store_true')

args = parser.parse_args()
print(args.filename, args.count, args.verbose)
print(args)
print(sys.argv[1])