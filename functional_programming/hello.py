import sys


def main():
    if len(sys.argv) < 2:
        print("Использование: hello.py <имя>")
        sys.exit(1)

    name = sys.argv[1]
    print(f"Привет, {name}!")


# if __name__ == "__main__":
#     main()