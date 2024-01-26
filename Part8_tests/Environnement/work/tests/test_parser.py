from src.helpers.Parser import Parser

def test_parser_with_digits1():
    separator = ','
    sentence = '123, 45, 678, 9, not_a_number'
    parser = Parser(separator)
    
    assert parser.parse(sentence) == '123 45 678 9'

def test_parser_with_digits2():
    separator = ':'
    sentence = '8790: bonjour le monde:8987:7777:Hello World:    9007' 
    parser = Parser(separator)
    
    assert  parser.parse(sentence) == '8790 8987 7777 9007'