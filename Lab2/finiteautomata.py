class FiniteAutomata:
    def __init__(self, file):
        self.__Q = []
        self.__S = {}
        self.__E = []
        self.__F = []
        self._q0 = ""
        self.__file = file
        self.readFile()

    def getLine(self, line):
        line = line.split('=')
        substring = line[1]
        substring = substring.split()
        return substring


    def readFile(self):
        with open(self.__file) as file:
            self.__Q = self.getLine(file.readline())
            self.__E = self.getLine(file.readline())
            self.__q0 = file.readline().split('=')[1].strip()
            self.__F = self.getLine(file.readline())

            file.readline()

            self.__S = {}
            for line in file:
                state1 = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[0]
                route = line.strip().split('->')[0].strip().replace('(', '').replace(')', '').split(',')[1]
                state2 = line.strip().split('->')[1].strip()
                print(state1 + ' ' + route + ' ' + state2)
                if (state1, route) in self.__S.keys():
                    self.__S[(state1, route)].append(state2)
                else:
                    self.__S[(state1, route)] = [state2]
            for elem in self.__S.keys():
                if len(self.__S[elem]) == 2:
                    if self.__S[elem][0] == self.__S[elem][1]:
                        self.__S[elem] = [self.__S[elem][0]]

    def getStates(self):
        return self.__Q

    def getAlphabet(self):
        return self.__E

    def getTransitions(self):
        return self.__S

    def getInitalState(self):
        return self.__q0

    def getFinalStates(self):
        return self.__F

    def is_DFA(self):
        for elem in self.__S.keys():
            if len(self.__S[elem]) > 1:
                return False
        return True

    def is_seq_accepted(self, sequence):
        if self.is_DFA():
            state = self.__q0
            for symbol in sequence:
                if (state, symbol) in self.__S.keys():
                    state = self.__S[(state, symbol)][0]
                else:
                    return False
            if state in self.__F:
                return True
            return False
        return False

