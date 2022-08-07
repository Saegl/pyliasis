from lark import Token, Tree
from pyliasis import parser


def test_if():
    source = """
    if expr then
        stmt1
        stmt2
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "cond_stmt",
                [
                    Token("CNAME", "expr"),
                    Tree(
                        "stmts",
                        [
                            Token("CNAME", "stmt1"),
                            Token("CNAME", "stmt2"),
                        ],
                    ),
                ],
            )
        ],
    )


def test_if_else():
    source = """
    if expr then
        stmt1
    else
        stmt2
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "cond_stmt",
                [
                    Token("CNAME", "expr"),
                    Tree("stmts", [Token("CNAME", "stmt1")]),
                    Tree("stmts", [Token("CNAME", "stmt2")]),
                ],
            )
        ],
    )


def test_if_elif():
    source = """
    if expr then
        stmt1
    elif
        stmt2
    else
        stmt2
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "cond_stmt",
                [
                    Token("CNAME", "expr"),
                    Tree(
                        "stmts",
                        [
                            Token("CNAME", "stmt1"),
                            Token("CNAME", "elif"),
                            Token("CNAME", "stmt2"),
                        ],
                    ),
                    Tree("stmts", [Token("CNAME", "stmt2")]),
                ],
            )
        ],
    )


def test_if_nested():
    source = """
    if expr1 then
        if expr2 then
            stmt1
        end
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "cond_stmt",
                [
                    Token("CNAME", "expr1"),
                    Tree(
                        "stmts",
                        [
                            Tree(
                                "cond_stmt",
                                [
                                    Token("CNAME", "expr2"),
                                    Tree("stmts", [Token("CNAME", "stmt1")]),
                                ],
                            )
                        ],
                    ),
                ],
            )
        ],
    )


def test_big_tree():
    source = """
    a
    if e then
        a
        if e then
            a
        elif e then
            a
            if e then
                a
            end
        else
            if e then
                a
            elif e then
                a
            end
            a
        end
        elif e then
            a
        else
        a
    end
    a
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Token("CNAME", "a"),
            Tree(
                "cond_stmt",
                [
                    Token("CNAME", "e"),
                    Tree(
                        "stmts",
                        [
                            Token("CNAME", "a"),
                            Tree(
                                "cond_stmt",
                                [
                                    Token("CNAME", "e"),
                                    Tree("stmts", [Token("CNAME", "a")]),
                                    Token("CNAME", "e"),
                                    Tree(
                                        "stmts",
                                        [
                                            Token("CNAME", "a"),
                                            Tree(
                                                "cond_stmt",
                                                [
                                                    Token("CNAME", "e"),
                                                    Tree(
                                                        "stmts", [Token("CNAME", "a")]
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    Tree(
                                        "stmts",
                                        [
                                            Tree(
                                                "cond_stmt",
                                                [
                                                    Token("CNAME", "e"),
                                                    Tree(
                                                        "stmts", [Token("CNAME", "a")]
                                                    ),
                                                    Token("CNAME", "e"),
                                                    Tree(
                                                        "stmts", [Token("CNAME", "a")]
                                                    ),
                                                ],
                                            ),
                                            Token("CNAME", "a"),
                                        ],
                                    ),
                                ],
                            ),
                        ],
                    ),
                    Token("CNAME", "e"),
                    Tree("stmts", [Token("CNAME", "a")]),
                    Tree("stmts", [Token("CNAME", "a")]),
                ],
            ),
            Token("CNAME", "a"),
        ],
    )
