from nose.tools import *
from ex48 import parser

def test_peek():
    wl = [('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')]
    assert_equal(parser.peek(wl),'noun')
    wl2 = [('verb', 'run'), ('direction', 'north')]
    assert_equal(parser.peek(wl2),'verb')

def test_match():
    wl = [('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')]
    assert_equal(parser.match(wl,'noun'), ('noun','bear'))
    wl2 = [('verb', 'run'), ('direction', 'north')]
    assert_equal(parser.match(wl2,'verb'),('verb','run'))

def test_parse():
    wl = [('noun', 'bear'), ('verb', 'eat'), ('stop', 'the'), ('noun', 'honey')]
    assert_equal(parser.parse_subject(wl),('noun','bear'))
    assert_equal(parser.parse_verb(wl),('verb','eat'))
    assert_equal(parser.parse_object(wl), ('noun','honey'))

def test_parse_sentence():
    result = parser.parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal(result.subject,  'player')
    assert_equal(result.verb,'run')
    assert_equal(result.object, 'north')










