from lark import Tree, Token
from pyliasis import parser


def test_class():
    source = """
    class Foo end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "class_stmt",
                [
                    Token("CNAME", "Foo"),
                    Tree("fields", []),
                    Tree("methods", []),
                ],
            )
        ],
    )


def test_class_with_inheritance():
    source = """
    class Foo <- Bar end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "class_stmt",
                [
                    Token("CNAME", "Foo"),
                    Tree("name_list", [Token("CNAME", "Bar")]),
                    Tree("fields", []),
                    Tree("methods", []),
                ],
            )
        ],
    )


def test_class_with_fields():
    source = """
    class Foo
        a: int
        b: str
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "class_stmt",
                [
                    Token("CNAME", "Foo"),
                    Tree(
                        "fields",
                        [
                            Tree(
                                "typed_name",
                                [Token("CNAME", "a"), Token("CNAME", "int")],
                            ),
                            Tree(
                                "typed_name",
                                [Token("CNAME", "b"), Token("CNAME", "str")],
                            ),
                        ],
                    ),
                    Tree("methods", []),
                ],
            )
        ],
    )


def test_class_with_methods():
    source = """
    class Foo
        def foo(self)
            some_code
        end
        def bar(self, arg1, arg2)
            some_code
        end
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "class_stmt",
                [
                    Token("CNAME", "Foo"),
                    Tree("fields", []),
                    Tree(
                        "methods",
                        [
                            Tree(
                                "def_stmt",
                                [
                                    Token("CNAME", "foo"),
                                    Tree(
                                        "def_args",
                                        [
                                            Tree(
                                                "mb_typed_names",
                                                [
                                                    Tree(
                                                        "mb_typed_name",
                                                        [Token("CNAME", "self")],
                                                    )
                                                ],
                                            )
                                        ],
                                    ),
                                    Tree("stmts", [Token("CNAME", "some_code")]),
                                ],
                            ),
                            Tree(
                                "def_stmt",
                                [
                                    Token("CNAME", "bar"),
                                    Tree(
                                        "def_args",
                                        [
                                            Tree(
                                                "mb_typed_names",
                                                [
                                                    Tree(
                                                        "mb_typed_name",
                                                        [Token("CNAME", "self")],
                                                    ),
                                                    Tree(
                                                        "mb_typed_name",
                                                        [Token("CNAME", "arg1")],
                                                    ),
                                                    Tree(
                                                        "mb_typed_name",
                                                        [Token("CNAME", "arg2")],
                                                    ),
                                                ],
                                            )
                                        ],
                                    ),
                                    Tree("stmts", [Token("CNAME", "some_code")]),
                                ],
                            ),
                        ],
                    ),
                ],
            )
        ],
    )


def test_class_mixed():
    source = """
    class Foo <- Bar
        a: int
        def foo(self)
            some_code
        end
        def bar(self, arg1, arg2)
            some_code
        end
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "class_stmt",
                [
                    Token("CNAME", "Foo"),
                    Tree("name_list", [Token("CNAME", "Bar")]),
                    Tree(
                        "fields",
                        [
                            Tree(
                                "typed_name",
                                [Token("CNAME", "a"), Token("CNAME", "int")],
                            )
                        ],
                    ),
                    Tree(
                        "methods",
                        [
                            Tree(
                                "def_stmt",
                                [
                                    Token("CNAME", "foo"),
                                    Tree(
                                        "def_args",
                                        [
                                            Tree(
                                                "mb_typed_names",
                                                [
                                                    Tree(
                                                        "mb_typed_name",
                                                        [Token("CNAME", "self")],
                                                    )
                                                ],
                                            )
                                        ],
                                    ),
                                    Tree("stmts", [Token("CNAME", "some_code")]),
                                ],
                            ),
                            Tree(
                                "def_stmt",
                                [
                                    Token("CNAME", "bar"),
                                    Tree(
                                        "def_args",
                                        [
                                            Tree(
                                                "mb_typed_names",
                                                [
                                                    Tree(
                                                        "mb_typed_name",
                                                        [Token("CNAME", "self")],
                                                    ),
                                                    Tree(
                                                        "mb_typed_name",
                                                        [Token("CNAME", "arg1")],
                                                    ),
                                                    Tree(
                                                        "mb_typed_name",
                                                        [Token("CNAME", "arg2")],
                                                    ),
                                                ],
                                            )
                                        ],
                                    ),
                                    Tree("stmts", [Token("CNAME", "some_code")]),
                                ],
                            ),
                        ],
                    ),
                ],
            )
        ],
    )
