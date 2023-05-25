from arpeggio import EOF
from arpeggio import OneOrMore
from arpeggio import Optional
from arpeggio import RegExMatch
from arpeggio import ZeroOrMore



def comment():
    return RegExMatch(r"%.*")


def program():
    return ZeroOrMore(statement), EOF


def statement():
    return [clause, example]


def example():
    return label, ground_literal, '.'


def label():
    return ['+', '-']


def ground_literal():
    return Optional(negation), ground_atom


def ground_atom():
    return functor, Optional('(', Optional(ground_terms), ')')


def ground_terms():
    return ground_term, ZeroOrMore(',', ground_term)


def ground_term():
    return [boolean, number, string, identifier]


def clause():
    return literal, Optional(':-', Optional(literals)), '.'


def literals():
    return literal, ZeroOrMore(',', literal)


def literal():
    return Optional(negation), atom


def negation():
    return OneOrMore('~')


def atom():
    return functor, Optional('(', Optional(terms), ')')


def functor():
    return [double_quote, single_quote, identifier]


def terms():
    return term, ZeroOrMore(',', term)


def term():
    return [boolean, number, string, identifier, variable]


def boolean():
    return [false, true]


def false():
    return RegExMatch(r"FALSE", ignore_case=True)


def true():
    return RegExMatch(r"TRUE", ignore_case=True)


def number():
    return [real, integer]


def real():
    return RegExMatch(r"-?\d*\.\d+(E-?\d+)?")


def integer():
    return RegExMatch(r"-?\d+")


def string():
    return [double_quote, single_quote]


def double_quote():
    return '"', RegExMatch(r'[^"]*'), '"'


def single_quote():
    return "'", RegExMatch(r"[^']*"), "'"


def identifier():
    return RegExMatch(r'[a-z][a-zA-Z_0-9]*')


def variable():
    return RegExMatch(r'[_A-Z][a-zA-Z_0-9]*')
