import pypeline

def sum(x):
    return x + 2

def square(x):
    return x * x

def main():
    data = 1
    p = pypeline.pypeline()
    p.add(sum).add(square)
    result = p.run(data)
    print(result)

main()