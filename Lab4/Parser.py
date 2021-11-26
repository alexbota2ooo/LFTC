

class Parser:
    def __init__(self, grammar):
        self.grammar = grammar

    def Success(self, config):
        config['s'] = 'f'
        return config

    def Expand(self, config):
        if config['alpha'] is None:
            config['alpha'] = [config['beta'][0]]
        else:
            config['alpha'].append(config['beta'][0])
        # config['beta'] se modifica da nu m-am mai uitat atent cu ce, cautam maine eventual
        return config

    def Advance(self, config):
        config['i'] = config['i'] + 1
        if config['alpha'] is None:
            config['alpha'] = [config['beta'][0]]
        else:
            config['alpha'].append(config['beta'][0])
        config['beta'] = config['beta'][1:]
        return config

    def MomentaryInsuccess(self, config):
        config['s'] = 'b'
        return config

    def Back(self, config):
        config['i'] = config['i'] - 1
        config['beta'] = config['beta'].insert(0, config['alpha'][-1])
        config['alpha'] = config['alpha'][:-1]
        return config

    def AnotherTry(self, config):
        config['s'] = 'q'
        prods = self.grammar.getProdForNonTerm(config['alpha'][-1])
        config['alpha'].append(prods[0])
        return config

    def recursive_descent(self, w):
        n = len(w)
        config = {'s': 'q', 'i': 0, 'alpha': None, 'beta': w}
        while config['s'] != 'f' and config['s'] != 'e':
            if config['s'] == 'q':
                if config['i'] == n and config['beta'] == '':
                    config = self.Success(config)
                else:
                    if config['beta'][0] in self.grammar.getNonTerms():  # ceva nonterminal, nu A
                        config = self.Expand(config)
                    else:
                        if config['beta'][0] in self.grammar.getAlphabet():  # ceva terminal, nu a
                            config = self.Advance(config)
                        else:
                            config = self.MomentaryInsuccess(config)
            else:
                if config['s'] == 'b':
                    alphaString = ''
                    for c in config['alpha']:
                        alphaString += c
                    if alphaString in self.grammar.getAlphabet():  # same
                        config = self.Back(config)
                    else:
                        config = self.AnotherTry(config)

        message = ""
        if config['s'] == 'e':
            print("Error")
        else:
            print("Sequence accepted")
            #BuildStringOfProd(config['alpha'])