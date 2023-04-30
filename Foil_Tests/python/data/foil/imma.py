from main_2 import *
from learning import get_constants, get_closure, get_masks, foil
from models import Literal, Program


bkg_data = il_back()
es = gli_es()


if __name__ == '__main__':

    bkg = bkg_data

    print('BKG:')
    print()
    print(bkg)
    print()

    """     # Get constants

    constants = get_constants(bkg_data)

    # Get closure
    closure = get_closure(bkg_data)

    # Get masks
    masks = get_masks(bkg_data)

    # Get foil
    foil = foil(es, constants, closure, masks)

    # Get program
    program = foil.get_program()

    # Print program
    print(program) """

target_name = 'l_110'
target = Literal.parse(target_name + '(X)')
examples = es

print('Esempi:')
print()

for e in examples:
    if e.label is Label.POSITIVE:
        print('+ : ' + target_name + '(' + e.assignment.get('X') + ')')
    else:
        print('- : ' + target_name + '(' + e.assignment.get('X') + ')')

print(bkg)

constants = get_constants([target, *{l for c in bkg for l in c.literals}])
world = Program(bkg).ground()
positives, negatives = get_closure(target, constants, world, examples)
masks = get_masks([*{l for c in bkg for l in c.literals}])

print(positives)
print(negatives)

for clause in foil(target, bkg, masks, constants, positives, negatives):
    print()
    print('Risultato:')
    print()
    print(clause)


print()
print('Fine.')
