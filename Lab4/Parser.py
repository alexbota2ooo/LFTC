

class Parser:
    def __init__(self, grammar):
        self.grammar = grammar

    def Expand(self, config):
        config['alpha'].append(config['beta'][0] + "_1")

        aux = self.grammar.getProdForNonTerm(config['beta'][0])[0]

        config['beta'] = config['beta'][1:]

        for i in range(len(aux)-1, -1, -1):
            config['beta'].insert(0, aux[i])

        return config

    def Advance(self, config, w):
        config['alpha'].append(config['beta'][0])
        config['beta'] = config['beta'][1:]
        config['i'] = config['i'] + 1
        return config

    def MomentaryInsuccess(self, config):
        config['s'] = 'b'
        return config

    def Back(self, config):
        config['i'] = config['i'] - 1
        config['beta'].insert(0, config['alpha'][-1])
        config['alpha'] = config['alpha'][:-1]
        return config

    def AnotherTry(self, config):
        x = config['alpha'][-1].split('_')
        nonterm = x[0]
        j = int(x[1])

        if len(self.grammar.getProdForNonTerm(nonterm)) > j:
            j = j + 1
            config['s'] = 'q'
            config['alpha'][-1] = nonterm + "_" + str(j)
            aux = self.grammar.getProdForNonTerm(nonterm)[j - 1]

            delete = self.grammar.getProdForNonTerm(nonterm)[j - 2]
            config['beta'] = config['beta'][len(delete):]

            for i in range(len(aux) - 1, -1, -1):
                config['beta'].insert(0, aux[i])
        elif config['i'] != 1 or nonterm != self.grammar.getStartingSymb():
            config['s'] = 'b'
            config['alpha'] = config['alpha'][:-1]
            config['beta'] = config['beta'][1:]
            config['beta'].insert(0, nonterm)
        else:
            config['s'] = 'e'

        return config

    def Success(self, config):
        config['s'] = 'f'
        return config

    def buildStringOfProd(self, workingStack):
        result = []
        for x in workingStack:
            for e in x:
                if e == '_':
                    aux = x.split('_')
                    nonterm = aux[0]
                    j = int(aux[1])

                    production = self.grammar.getProdForNonTerm(nonterm)[j - 1]

                    result.append(nonterm + ' -> ' + str(production))

        return result


    def recursive_descent(self, w):
        n = len(w)
        print(n)
        config = {'s': 'q', 'i': 1, 'alpha': [], 'beta': [self.grammar.getStartingSymb()]}
        while config['s'] != 'f' and config['s'] != 'e':
            print(config)
            if config['s'] == 'q':
                if config['i'] == n + 1 and config['beta'] == []:
                    config = self.Success(config)
                else:
                    if config['beta'] and config['beta'][0] in self.grammar.getNonTerms():
                        print("expand")
                        config = self.Expand(config)
                    else:
                        if config['beta'] and config['i'] - 1 < n and config['beta'][0] == w[config['i'] - 1]:
                            print("advance")
                            config = self.Advance(config, w)
                        else:
                            print("momentary insuccess")
                            config = self.MomentaryInsuccess(config)
            else:
                    if len(config['alpha']) > 0 and config['alpha'][-1] in self.grammar.getAlphabet():
                        print("back")
                        config = self.Back(config)
                    else:
                        print("another try")
                        config = self.AnotherTry(config)

        message = ""
        if config['s'] == 'e':
            print("Error")
        else:
            print()
            print("Sequence accepted")
            print()
            print("Production string:")
            print(self.buildStringOfProd(config['alpha']))

