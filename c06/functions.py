def print_hello(name):
    print(f"Nice to meet you {name}")

def get_name():
    name = input('What''s your name? ')
    return name

def main():
    person = get_name()
    print_hello(person)

if __name__ == "__main__":
    main()