import argparse

parser = argparse.ArgumentParser(description='Calculating simple math ')
parser.add_argument("x", type=float, help="firs number")
parser.add_argument("operation", type=str, help="operation")
parser.add_argument("y", type=float, help="second number")
args = parser.parse_args()


print(args.x)
print(args.operation)
print(args.y)


if args.operation == "+":
    result = x + y

elif args.operation == "-":
    result =  x - y

elif args.operation == "*":
    result = x * y

elif args.operation == "/":
    result = x / y

else:
    print("Error")

print("result is = ", result)