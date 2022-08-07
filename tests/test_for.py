from lark import Token, Tree
from pyliasis import parser


def test_for():
    source = """
    for i in range do
        print
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "for_stmt",
                [
                    Tree("name_list", [Token("CNAME", "i")]),
                    Token("CNAME", "range"),
                    Tree("stmts", [Token("CNAME", "print")]),
                ],
            )
        ],
    )
