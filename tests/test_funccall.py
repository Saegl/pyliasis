from lark import Tree, Token
from pyliasis import parser


def test_funccall_no_args():
    source = """
    factorial()
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "funccall",
                [
                    Tree("dotted_name", [Token("CNAME", "factorial")]),
                    Tree("call_args", []),
                ],
            )
        ],
    )


def test_funccall_arg():
    source = """
    factorial(5)
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "funccall",
                [
                    Tree("dotted_name", [Token("CNAME", "factorial")]),
                    Tree("call_args", [Tree("args", [Token("NUMBER", "5")])]),
                ],
            )
        ],
    )


def test_funccall_args():
    source = """
    sum(5, 6)
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "funccall",
                [
                    Tree("dotted_name", [Token("CNAME", "sum")]),
                    Tree(
                        "call_args",
                        [
                            Tree(
                                "args",
                                [
                                    Token("NUMBER", "5"),
                                    Token("NUMBER", "6"),
                                ],
                            )
                        ],
                    ),
                ],
            )
        ],
    )


def test_funccall_named_args():
    source = """
    sum(a=5, b=6)
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "funccall",
                [
                    Tree("dotted_name", [Token("CNAME", "sum")]),
                    Tree(
                        "call_args",
                        [
                            Tree(
                                "named_args",
                                [
                                    Tree(
                                        "named_arg",
                                        [Token("CNAME", "a"), Token("NUMBER", "5")],
                                    ),
                                    Tree(
                                        "named_arg",
                                        [Token("CNAME", "b"), Token("NUMBER", "6")],
                                    ),
                                ],
                            )
                        ],
                    ),
                ],
            )
        ],
    )


def test_funccall_mixed():
    source = """
    sum(5, b=6)
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "funccall",
                [
                    Tree("dotted_name", [Token("CNAME", "sum")]),
                    Tree(
                        "call_args",
                        [
                            Tree("args", [Token("NUMBER", "5")]),
                            Tree(
                                "named_args",
                                [
                                    Tree(
                                        "named_arg",
                                        [
                                            Token("CNAME", "b"),
                                            Token("NUMBER", "6"),
                                        ],
                                    )
                                ],
                            ),
                        ],
                    ),
                ],
            )
        ],
    )
