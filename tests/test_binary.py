from lark import Token, Tree
from pyliasis import parser


def test_plus_minus():
    source = """
    2 + 3 - 4
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "sum",
                [
                    Tree(
                        "sum",
                        [
                            Token("NUMBER", "2"),
                            Token("SUM_OP", "+"),
                            Token("NUMBER", "3"),
                        ],
                    ),
                    Token("SUM_OP", "-"),
                    Token("NUMBER", "4"),
                ],
            )
        ],
    )


def test_arith():
    source = """
    2 + 2 * 2
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "sum",
                [
                    Token("NUMBER", "2"),
                    Token("SUM_OP", "+"),
                    Tree(
                        "product",
                        [
                            Token("NUMBER", "2"),
                            Token("PRODUCT_OP", "*"),
                            Token("NUMBER", "2"),
                        ],
                    ),
                ],
            )
        ],
    )


def test_compare():
    source = """
    2 + 2 == 4
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "cim",
                [
                    Tree(
                        "sum",
                        [
                            Token("NUMBER", "2"),
                            Token("SUM_OP", "+"),
                            Token("NUMBER", "2"),
                        ],
                    ),
                    Token("CIM_OP", "=="),
                    Token("NUMBER", "4"),
                ],
            )
        ],
    )
