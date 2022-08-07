from lark import Tree, Token
from pyliasis import parser


def test_list():
    source = """
    [1, 2, 3]
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "list_value",
                [
                    Tree("nl_expr", [Token("NUMBER", "1")]),
                    Tree("nl_expr", [Token("NUMBER", "2")]),
                    Tree("nl_expr", [Token("NUMBER", "3")]),
                ],
            )
        ],
    )


def test_list_expr():
    source = """
    [1 + 1, 2 * 2, call()]
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "list_value",
                [
                    Tree(
                        "nl_expr",
                        [
                            Tree(
                                "sum",
                                [
                                    Token("NUMBER", "1"),
                                    Token("SUM_OP", "+"),
                                    Token("NUMBER", "1"),
                                ],
                            )
                        ],
                    ),
                    Tree(
                        "nl_expr",
                        [
                            Tree(
                                "product",
                                [
                                    Token("NUMBER", "2"),
                                    Token("PRODUCT_OP", "*"),
                                    Token("NUMBER", "2"),
                                ],
                            )
                        ],
                    ),
                    Tree(
                        "nl_expr",
                        [
                            Tree(
                                "funccall",
                                [
                                    Tree("dotted_name", [Token("CNAME", "call")]),
                                    Tree("call_args", []),
                                ],
                            )
                        ],
                    ),
                ],
            )
        ],
    )


def test_list_multiline():
    source = """
    [
        1,
        2,
        3,
    ]
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "list_value",
                [
                    Tree("nl_expr", [Token("NUMBER", "1")]),
                    Tree("nl_expr", [Token("NUMBER", "2")]),
                    Tree("nl_expr", [Token("NUMBER", "3")]),
                ],
            )
        ],
    )
