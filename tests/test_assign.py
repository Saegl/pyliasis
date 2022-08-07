from lark import Tree, Token
from pyliasis import parser


def test_assign():
    source = """
    x = 2
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "assign_stmt",
                [
                    Token("CNAME", "x"),
                    Token("NUMBER", "2"),
                ],
            ),
        ],
    )


def test_assign_arith():
    source = """
    x = 2 + 2
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "assign_stmt",
                [
                    Token("CNAME", "x"),
                    Tree(
                        "sum",
                        [
                            Token("NUMBER", "2"),
                            Token("SUM_OP", "+"),
                            Token("NUMBER", "2"),
                        ],
                    ),
                ],
            )
        ],
    )


def test_assign_compare():
    source = """
    x = 2 == 2
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "assign_stmt",
                [
                    Token("CNAME", "x"),
                    Tree(
                        "cim",
                        [
                            Token("NUMBER", "2"),
                            Token("CIM_OP", "=="),
                            Token("NUMBER", "2"),
                        ],
                    ),
                ],
            )
        ],
    )
