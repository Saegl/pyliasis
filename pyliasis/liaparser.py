from lark import Lark

with open("grammar.lark", "rt", encoding="utf8") as f:
    parser = Lark(f)
