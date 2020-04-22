class ListInherited:
    def __str__(self):
        return '<instance of %s , address %s:\n%s>' %(
            self.__class__.__name__,
            id(self),
            self.__attrenames()
        )
    def __attrenames(self):
        results = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__':
                results += '\tname %s=<>\n' % attr
            else:
                results += '\tname %s=%s\n' %(attr, getattr(self, attr))
        return results

    