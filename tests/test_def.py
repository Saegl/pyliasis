from lark import Tree, Token
from pyliasis import parser


def test_def():
    source = """
    def render()
        some_code
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "def_stmt",
                [
                    Token("CNAME", "render"),
                    Tree("def_args", []),
                    Tree("stmts", [Token("CNAME", "some_code")]),
                ],
            )
        ],
    )


def test_def_with_return_type():
    source = """
    def render() -> int
        some_code
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "def_stmt",
                [
                    Token("CNAME", "render"),
                    Tree("def_args", []),
                    Token("CNAME", "int"),
                    Tree("stmts", [Token("CNAME", "some_code")]),
                ],
            )
        ],
    )


def test_def_with_arg():
    source = """
    def render(arg)
        some_code
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "def_stmt",
                [
                    Token("CNAME", "render"),
                    Tree(
                        "def_args",
                        [
                            Tree(
                                "mb_typed_names",
                                [Tree("mb_typed_name", [Token("CNAME", "arg")])],
                            )
                        ],
                    ),
                    Tree("stmts", [Token("CNAME", "some_code")]),
                ],
            )
        ],
    )


def test_def_with_args():
    source = """
    def render(arg1, arg2)
        some_code
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "def_stmt",
                [
                    Token("CNAME", "render"),
                    Tree(
                        "def_args",
                        [
                            Tree(
                                "mb_typed_names",
                                [
                                    Tree("mb_typed_name", [Token("CNAME", "arg1")]),
                                    Tree("mb_typed_name", [Token("CNAME", "arg2")]),
                                ],
                            )
                        ],
                    ),
                    Tree("stmts", [Token("CNAME", "some_code")]),
                ],
            )
        ],
    )


def test_def_with_args_and_defaults():
    source = """
    def render(arg1, arg2 = 5)
        some_code
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "def_stmt",
                [
                    Token("CNAME", "render"),
                    Tree(
                        "def_args",
                        [
                            Tree(
                                "mb_typed_names",
                                [Tree("mb_typed_name", [Token("CNAME", "arg1")])],
                            ),
                            Tree(
                                "with_default_names",
                                [
                                    Tree(
                                        "with_default_name",
                                        [
                                            Tree(
                                                "mb_typed_name",
                                                [Token("CNAME", "arg2")],
                                            ),
                                            Token("NUMBER", "5"),
                                        ],
                                    )
                                ],
                            ),
                        ],
                    ),
                    Tree("stmts", [Token("CNAME", "some_code")]),
                ],
            )
        ],
    )


def test_def_with_typed_args():
    source = """
    def render(arg1 : int, arg2 : str)
        some_code
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "def_stmt",
                [
                    Token("CNAME", "render"),
                    Tree(
                        "def_args",
                        [
                            Tree(
                                "mb_typed_names",
                                [
                                    Tree(
                                        "mb_typed_name",
                                        [Token("CNAME", "arg1"), Token("CNAME", "int")],
                                    ),
                                    Tree(
                                        "mb_typed_name",
                                        [Token("CNAME", "arg2"), Token("CNAME", "str")],
                                    ),
                                ],
                            )
                        ],
                    ),
                    Tree("stmts", [Token("CNAME", "some_code")]),
                ],
            )
        ],
    )


def test_def_with_typed_defaults():
    source = """
    def render(arg1 : int = 5, arg2 : str = "hello")
        some_code
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "def_stmt",
                [
                    Token("CNAME", "render"),
                    Tree(
                        "def_args",
                        [
                            Tree(
                                "with_default_names",
                                [
                                    Tree(
                                        "with_default_name",
                                        [
                                            Tree(
                                                "mb_typed_name",
                                                [
                                                    Token("CNAME", "arg1"),
                                                    Token("CNAME", "int"),
                                                ],
                                            ),
                                            Token("NUMBER", "5"),
                                        ],
                                    ),
                                    Tree(
                                        "with_default_name",
                                        [
                                            Tree(
                                                "mb_typed_name",
                                                [
                                                    Token("CNAME", "arg2"),
                                                    Token("CNAME", "str"),
                                                ],
                                            ),
                                            Token("STRING", '"hello"'),
                                        ],
                                    ),
                                ],
                            )
                        ],
                    ),
                    Tree("stmts", [Token("CNAME", "some_code")]),
                ],
            )
        ],
    )


def test_def_mixed():
    source = """
    def render(arg1, arg2: int, arg3: str = "hello")
        some_code
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "def_stmt",
                [
                    Token("CNAME", "render"),
                    Tree(
                        "def_args",
                        [
                            Tree(
                                "mb_typed_names",
                                [
                                    Tree("mb_typed_name", [Token("CNAME", "arg1")]),
                                    Tree(
                                        "mb_typed_name",
                                        [Token("CNAME", "arg2"), Token("CNAME", "int")],
                                    ),
                                ],
                            ),
                            Tree(
                                "with_default_names",
                                [
                                    Tree(
                                        "with_default_name",
                                        [
                                            Tree(
                                                "mb_typed_name",
                                                [
                                                    Token("CNAME", "arg3"),
                                                    Token("CNAME", "str"),
                                                ],
                                            ),
                                            Token("STRING", '"hello"'),
                                        ],
                                    )
                                ],
                            ),
                        ],
                    ),
                    Tree("stmts", [Token("CNAME", "some_code")]),
                ],
            )
        ],
    )


def test_factorial():
    source = """
    def factorial(n: int) -> int
        if n == 0 then
            return 1
        else
            return n * factorial(n - 1)
        end
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "def_stmt",
                [
                    Token("CNAME", "factorial"),
                    Tree(
                        "def_args",
                        [
                            Tree(
                                "mb_typed_names",
                                [
                                    Tree(
                                        "mb_typed_name",
                                        [Token("CNAME", "n"), Token("CNAME", "int")],
                                    )
                                ],
                            )
                        ],
                    ),
                    Token("CNAME", "int"),
                    Tree(
                        "stmts",
                        [
                            Tree(
                                "cond_stmt",
                                [
                                    Tree(
                                        "cim",
                                        [
                                            Token("CNAME", "n"),
                                            Token("CIM_OP", "=="),
                                            Token("NUMBER", "0"),
                                        ],
                                    ),
                                    Tree(
                                        "stmts",
                                        [Tree("return_stmt", [Token("NUMBER", "1")])],
                                    ),
                                    Tree(
                                        "stmts",
                                        [
                                            Tree(
                                                "return_stmt",
                                                [
                                                    Tree(
                                                        "product",
                                                        [
                                                            Token("CNAME", "n"),
                                                            Token("PRODUCT_OP", "*"),
                                                            Tree(
                                                                "funccall",
                                                                [
                                                                    Tree(
                                                                        "dotted_name",
                                                                        [
                                                                            Token(
                                                                                "CNAME",
                                                                                "factorial",
                                                                            )
                                                                        ],
                                                                    ),
                                                                    Tree(
                                                                        "call_args",
                                                                        [
                                                                            Tree(
                                                                                "args",
                                                                                [
                                                                                    Tree(
                                                                                        "sum",
                                                                                        [
                                                                                            Token(
                                                                                                "CNAME",
                                                                                                "n",
                                                                                            ),
                                                                                            Token(
                                                                                                "SUM_OP",
                                                                                                "-",
                                                                                            ),
                                                                                            Token(
                                                                                                "NUMBER",
                                                                                                "1",
                                                                                            ),
                                                                                        ],
                                                                                    )
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
                                        ],
                                    ),
                                ],
                            )
                        ],
                    ),
                ],
            )
        ],
    )
