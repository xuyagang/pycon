class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
    def printNumInstances(self):
        print(f'{Spam.numInstances}')

a, b, c = Spam(), Spam(), Spam()
a.printNumInstances()
print(Spam.numInstances)
print(Spam().printNumInstances())
