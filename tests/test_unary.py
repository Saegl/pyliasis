from lark import Lark, Tree, Token
from pyliasis import parser


def test_unary():
    source = """
    -2
    """
    tree = parser.parse(source)
    Tree(
        "stmts",
        [
            Tree("unary", [Token("UNARY_OP", "-"), Token("NUMBER", "2")]),
            Tree("unary", [Token("UNARY_OP", "+"), Token("NUMBER", "2")]),
        ],
    )
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "unary",
                [Token("UNARY_OP", "-"), Token("NUMBER", "2")],
            ),
        ],
    )


def test_unary_arith():
    source = """
    -2 + 2
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "sum",
                [
                    Tree(
                        "unary",
                        [
                            Token("UNARY_OP", "-"),
                            Token("NUMBER", "2"),
                        ],
                    ),
                    Token("SUM_OP", "+"),
                    Token("NUMBER", "2"),
                ],
            )
        ],
    )
