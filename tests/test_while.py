from lark import Tree, Token
from pyliasis import parser


def test_while():
    source = """
    while x < 5 do
        stmt1
        stmt2
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "while_stmt",
                [
                    Tree(
                        "cim",
                        [
                            Token("CNAME", "x"),
                            Token("CIM_OP", "<"),
                            Token("NUMBER", "5"),
                        ],
                    ),
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


def test_while_nested():
    source = """
    while x < 5 do
        stmt0
        while y < 5 do
            stmt1
            stmt2
        end
        stmt3
    end
    """
    tree = parser.parse(source)
    assert tree == Tree(
        "stmts",
        [
            Tree(
                "while_stmt",
                [
                    Tree(
                        "cim",
                        [
                            Token("CNAME", "x"),
                            Token("CIM_OP", "<"),
                            Token("NUMBER", "5"),
                        ],
                    ),
                    Tree(
                        "stmts",
                        [
                            Token("CNAME", "stmt0"),
                            Tree(
                                "while_stmt",
                                [
                                    Tree(
                                        "cim",
                                        [
                                            Token("CNAME", "y"),
                                            Token("CIM_OP", "<"),
                                            Token("NUMBER", "5"),
                                        ],
                                    ),
                                    Tree(
                                        "stmts",
                                        [
                                            Token("CNAME", "stmt1"),
                                            Token("CNAME", "stmt2"),
                                        ],
                                    ),
                                ],
                            ),
                            Token("CNAME", "stmt3"),
                        ],
                    ),
                ],
            )
        ],
    )
