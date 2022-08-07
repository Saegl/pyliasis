from pyliasis import parser

if __name__ == "__main__":
    code = ""
    while True:
        line = input()
        if line == "q":
            break
        code += line + "\n"

    tree = parser.parse(code)

    print(tree)
    print(tree.pretty())
