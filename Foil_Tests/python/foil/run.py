from main import *
from learning import get_constants, get_closure, get_masks, foil
from models import Literal, Program

insieme =prepare_data()
bkg_data = il_back(insieme)
es = gli_es()

print("INSIEME::::::::::::::::::", len(insieme), ":::::::::::::::::::::::::")


# verifico se il file Python è stato eseguito direttamente dall'interprete Python oppure
# se è stato importato in un altro modulo Python.
# gli underscore sono usati per evitare conflitti con altri nomi.
if __name__ == '__main__':
    bkg = bkg_data

    print('Dati di BKG (background knowledge):')
    print()
    print(bkg)
    print()


target_name = 'l_110'
target = Literal.parse(target_name + '(X)')
examples = es

print("________________________________________________________________________")
print('\nEsempi: \n(gli esempi positivi e negativi con target name= l_110 e target= (X) equivalente alla matricola):')
print("Gli esempi positivi sono preceduti dal simbolo: (\"+\" e \":\" )")
print("Gli esempi negativi sono preceduti dal simbolo: (\"-\" e \":\" )")
print()


# Se l'etichetta è positiva, viene stampato un messaggio che indica che l'esempio
# appartiene alla classe di target positiva e il valore dell'attributo X
# dell'assegnazione dell'esempio.
# per debug (?)
for e in examples:
    if e.label is Label.POSITIVE:
        print('+ : ' + target_name + '(' + e.assignment.get('X') + ')')
    else:
        print('- : ' + target_name + '(' + e.assignment.get('X') + ')')

print(bkg)


# get_constants prende in input una lista di clausole e restituisce un insieme di costanti
constants = get_constants([target, *{l for c in bkg for l in c.literals}])
world = Program(bkg).ground()
# get_closure implementa l'algoritmo di chiusura nell'ambito dell'algoritmo FOIL
# L'obiettivo della chiusura è determinare quali esempi soddisfano il target fornito,
# tenendo conto delle costanti e del mondo degli esempi.
positives, negatives = get_closure(target, constants, world, examples)
# Genero le maschere booleane necessarie per l'esecuzione dell'algoritmo FOIL
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