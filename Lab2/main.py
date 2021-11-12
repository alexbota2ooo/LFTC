# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from finiteautomata import FiniteAutomata


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fa = FiniteAutomata("fa.in")
    fa.readFile()
    print(fa.getStates())
    print("Initial state: " + fa.getInitalState())
    print(fa.getAlphabet())
    print(fa.getTransitions())
    while(True):
        print("1. Initial state")
        print("2. Final states")
        print("3. All states")
        print("4. Alphabet")
        print("5. Transitions")
        print("6. Is DFA")                 #is deterministic?
        print("7. Is sequence accepted by the FA")
        print("8. Exit")
        command = input("Command : ")
        if command == '1':
            print(fa.getInitalState())
        elif command == '2':
            print(fa.getFinalStates())
        elif command == '3':
            print(fa.getStates())
        elif command == '4':
            print(fa.getAlphabet())
        elif command == '5':
            print(fa.getTransitions())
        elif command == '6':
            print(fa.is_DFA())
        elif command == '7':
            sequence = input("Sequence: ")
            sequence = sequence.split()
            #print(sequence)
            print(fa.is_seq_accepted(sequence))
        elif command == '8':
            break

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
