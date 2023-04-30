from arpeggio import EOF
from arpeggio import OneOrMore
from arpeggio import Optional
from arpeggio import RegExMatch
from arpeggio import ZeroOrMore

""" Each rule is given in the form of Python function.
Python function returns data structure that maps to PEG expressions.
PEG expressions are defined in the arpeggio library.
PEG expressions are used to define parsing rules.
PEG stands for Parsing Expression Grammar.
PEG grammar is a set of PEG rules. PEG rules consists of parsing expressions and can reference (call) each other.


EOF
end of string/file is recognized by the EOF special rule. 

OneOrMore
will try to match parser expression specified one or more times.

Optional
will try to match parser expression specified and will not fail in case match is not successful.

RegExMatch
checks for a match only at the beginning of the string. 
So, if a match is found in the first line, it returns the match object. 
But if a match is found in some other line, the Python RegEx Match function returns null.

ZeroOrMore
will try to match parser expression specified zero or more times. It will never fail.


to use Python's raw string notation for regular expression patterns; backslashes are
not handled in any special way in a string literal prefixed with 'r'.
So r"\n" is a two-character string containing '\' and 'n', while "\n" is
a one-character string containing a newline. """

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
