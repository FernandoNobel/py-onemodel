from onemodel.parser_ import Parser
from onemodel.tokens import Token, TokenType
from onemodel.nodes import *

import pdb

def test_empty():
    tokens = [
            Token(TokenType.END_OF_FILE, pos_start = Position(0,0,0,"",""))
            ]

    parser = Parser(tokens)
    res = parser.parse()

    assert res.node == None

def test_individual_operations():
    tokens = [
            Token(TokenType.NUMBER,1, pos_start = Position(0,0,0,"","")),
            Token(TokenType.END_OF_FILE, pos_start = Position(0,0,1,"",""))
            ]

    res = Parser(tokens).parse()

    assert res.node.element_nodes == [
            NumberNode(Token(TokenType.NUMBER,1))
            ]


    tokens = [
            Token(TokenType.PLUS, pos_start = Position(0,0,0,"","")),
            Token(TokenType.NUMBER,1, pos_start = Position(0,0,1,"","")),
            Token(TokenType.END_OF_FILE, pos_start = Position(0,0,2,"",""))
            ]

    res = Parser(tokens).parse()

    assert res.node.element_nodes == [
             UnaryOperationNode(
                 Token(TokenType.PLUS),
                 NumberNode(Token(TokenType.NUMBER,1))
                 )
             ]

#        tokens = [
#                Token(TokenType.MINUS),
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.END_OF_FILE)
#                ]
#        res = Parser(tokens).parse()
#        self.assertEqual(res.node, 
#                UnaryOperationNode(
#                    Token(TokenType.MINUS),
#                    NumberNode(Token(TokenType.NUMBER,1))
#                    )
#                )
#
#        tokens = [
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.PLUS),
#                Token(TokenType.NUMBER,2),
#                Token(TokenType.END_OF_FILE)
#                ]
#        res = Parser(tokens).parse()
#        self.assertEqual(res.node, 
#                BinaryOperationNode(
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    Token(TokenType.PLUS),
#                    NumberNode(Token(TokenType.NUMBER,2)),
#                    )
#                )
#
#        tokens = [
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.MINUS),
#                Token(TokenType.NUMBER,2),
#                Token(TokenType.END_OF_FILE)
#                ]
#        res = Parser(tokens).parse()
#        self.assertEqual(res.node, 
#                BinaryOperationNode(
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    Token(TokenType.MINUS),
#                    NumberNode(Token(TokenType.NUMBER,2)),
#                    )
#                )
#
#        tokens = [
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.MULTIPLICATION),
#                Token(TokenType.NUMBER,2),
#                Token(TokenType.END_OF_FILE)
#                ]
#        res = Parser(tokens).parse()
#        self.assertEqual(res.node, 
#                BinaryOperationNode(
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    Token(TokenType.MULTIPLICATION),
#                    NumberNode(Token(TokenType.NUMBER,2)),
#                    )
#                )
#
#
#        tokens = [
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.DIVISION),
#                Token(TokenType.NUMBER,2),
#                Token(TokenType.END_OF_FILE)
#                ]
#        res = Parser(tokens).parse()
#        self.assertEqual(res.node, 
#                BinaryOperationNode(
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    Token(TokenType.DIVISION),
#                    NumberNode(Token(TokenType.NUMBER,2)),
#                    )
#                )
#
#        tokens = [
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.POWER),
#                Token(TokenType.NUMBER,2),
#                Token(TokenType.END_OF_FILE)
#                ]
#        res = Parser(tokens).parse()
#        self.assertEqual(res.node, 
#                BinaryOperationNode(
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    Token(TokenType.POWER),
#                    NumberNode(Token(TokenType.NUMBER,2)),
#                    )
#                )
#
#        # 1 == 1
#        tokens = [
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.IS_EQUAL),
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.END_OF_FILE)
#                ]
#        res = Parser(tokens).parse()
#        self.assertEqual(res.node, 
#                BinaryOperationNode(
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    Token(TokenType.IS_EQUAL),
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    )
#                )
#
#        # 1 != 1
#        tokens = [
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.NOT_EQUAL),
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.END_OF_FILE)
#                ]
#        res = Parser(tokens).parse()
#        self.assertEqual(res.node, 
#                BinaryOperationNode(
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    Token(TokenType.NOT_EQUAL),
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    )
#                )
#
#        # 1 < 1
#        tokens = [
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.LESS_THAN),
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.END_OF_FILE)
#                ]
#        res = Parser(tokens).parse()
#        self.assertEqual(res.node, 
#                BinaryOperationNode(
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    Token(TokenType.LESS_THAN),
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    )
#                )
#
#        # 1 > 1
#        tokens = [
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.GREATER_THAN),
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.END_OF_FILE)
#                ]
#        res = Parser(tokens).parse()
#        self.assertEqual(res.node, 
#                BinaryOperationNode(
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    Token(TokenType.GREATER_THAN),
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    )
#                )
#
#        # 1 <= 1
#        tokens = [
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.LESS_EQUAL_THAN),
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.END_OF_FILE)
#                ]
#        res = Parser(tokens).parse()
#        self.assertEqual(res.node, 
#                BinaryOperationNode(
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    Token(TokenType.LESS_EQUAL_THAN),
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    )
#                )
#
#        # 1 >= 1
#        tokens = [
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.GREATER_EQUAL_THAN),
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.END_OF_FILE)
#                ]
#        res = Parser(tokens).parse()
#        self.assertEqual(res.node, 
#                BinaryOperationNode(
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    Token(TokenType.GREATER_EQUAL_THAN),
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    )
#                )
#
#        # 1 AND 1
#        tokens = [
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.KEYWORD, "AND"),
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.END_OF_FILE)
#                ]
#        res = Parser(tokens).parse()
#        self.assertEqual(res.node, 
#                BinaryOperationNode(
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    Token(TokenType.KEYWORD, "AND"),
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    )
#                )
#
#        # 1 OR 1
#        tokens = [
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.KEYWORD, "OR"),
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.END_OF_FILE)
#                ]
#        res = Parser(tokens).parse()
#        self.assertEqual(res.node, 
#                BinaryOperationNode(
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    Token(TokenType.KEYWORD, "OR"),
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    )
#                )
#
#        # NOT 1
#        tokens = [
#                Token(TokenType.KEYWORD, "NOT"),
#                Token(TokenType.NUMBER,1),
#                Token(TokenType.END_OF_FILE)
#                ]
#        res = Parser(tokens).parse()
#        self.assertEqual(res.node, 
#                UnaryOperationNode(
#                    Token(TokenType.KEYWORD, "NOT"),
#                    NumberNode(Token(TokenType.NUMBER,1)),
#                    )
#                )
#
#    def test_full_expr(self):
#        # 27^2 + (43 / 36 - 48) * 51
#        tokens = [
#                Token(TokenType.NUMBER, 27),
#                Token(TokenType.POWER),
#                Token(TokenType.NUMBER, 2),
#                Token(TokenType.PLUS),
#                Token(TokenType.LEFT_PAREN),
#                Token(TokenType.NUMBER, 43),
#                Token(TokenType.DIVISION),
#                Token(TokenType.NUMBER, 36),
#                Token(TokenType.MINUS),
#                Token(TokenType.NUMBER, 48),
#                Token(TokenType.RIGHT_PAREN),
#                Token(TokenType.MULTIPLICATION),
#                Token(TokenType.NUMBER, 51),
#                Token(TokenType.END_OF_FILE),
#                ]
#        res = Parser(tokens).parse()
#
#        result = BinaryOperationNode(
#                    NumberNode(Token(TokenType.NUMBER,43)),
#                    Token(TokenType.DIVISION),
#                    NumberNode(Token(TokenType.NUMBER,36))
#                    )
#
#        result = BinaryOperationNode(
#                    result,
#                    Token(TokenType.MINUS),
#                    NumberNode(Token(TokenType.NUMBER,48))
#                    )
#
#        result = BinaryOperationNode(
#                    result,
#                    Token(TokenType.MULTIPLICATION),
#                    NumberNode(Token(TokenType.NUMBER,51))
#                    )
#
#        result = BinaryOperationNode(
#                    BinaryOperationNode(
#                        NumberNode(Token(TokenType.NUMBER,27)),
#                        Token(TokenType.POWER),
#                        NumberNode(Token(TokenType.NUMBER,2)),
#                        ),
#                    Token(TokenType.PLUS),
#                    result,
#                    )
#
#        self.assertEqual(res.node, result)
