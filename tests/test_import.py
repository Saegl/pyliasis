from lark import Token, Tree
from pyliasis import parser


def test_import():
    source = """
    import math
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "import_stmt",
                [
                    Tree(
                        "import_name",
                        [
                            Tree(
                                "dotted_names",
                                [Tree("dotted_name", [Token("CNAME", "math")])],
                            )
                        ],
                    )
                ],
            )
        ],
    )


def test_import_dotted():
    source = """
    import mylib.parser.ast
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "import_stmt",
                [
                    Tree(
                        "import_name",
                        [
                            Tree(
                                "dotted_names",
                                [
                                    Tree(
                                        "dotted_name",
                                        [
                                            Token("CNAME", "mylib"),
                                            Token("CNAME", "parser"),
                                            Token("CNAME", "ast"),
                                        ],
                                    )
                                ],
                            )
                        ],
                    )
                ],
            )
        ],
    )


def test_import_from():
    source = """
    from math import pi
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "import_stmt",
                [
                    Tree(
                        "import_from",
                        [
                            Tree("dotted_name", [Token("CNAME", "math")]),
                            Tree("name_list", [Token("CNAME", "pi")]),
                        ],
                    )
                ],
            )
        ],
    )


def test_import_from_dotted():
    source = """
    from mylib.parser import ast
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "import_stmt",
                [
                    Tree(
                        "import_from",
                        [
                            Tree(
                                "dotted_name",
                                [Token("CNAME", "mylib"), Token("CNAME", "parser")],
                            ),
                            Tree("name_list", [Token("CNAME", "ast")]),
                        ],
                    )
                ],
            )
        ],
    )
