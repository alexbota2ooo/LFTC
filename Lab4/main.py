from grammar import *
from Parser import *

if __name__ == '__main__':
    option=-1
    # grammar = Grammar("g1.in")
    grammar = Grammar("g3.in")
    parser = Parser(grammar)

    f = open("p2.txt", "r")

    string = f.read()

    # 'baabba'
    # print(parser.recursive_descent('++(+)'))
    parser.recursive_descent('abba')
    # print(parser.recursive_descent('abba'))
    print(grammar.checkCFG())

    print()
    print("0. Exit")
    print("1. Set of NonTerminals")
    print("2. The alphabet")
    print("3. Starting Symbol")
    print("4. Productions")
    print("5. Get productions for a given non-terminal")
    print("6. Get input sequence")

    while(option!=0):
        option=int(input("option: "))
        if option==1:
            print(grammar.getNonTerms())
        elif option==2:
            print(grammar.getAlphabet())
        elif option==3:
            print(grammar.getStartingSymb())
        elif option==4:
            print(grammar.getProductions())
        elif option==5:
            nonterm = input("non-terminal")
            print(grammar.getProdForNonTerm(nonterm))
