def printNumInstances():
    print('Number of instance created: ', Spam.numInstances)

class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1

if __name__ == '__main__':
    a = Spam()
    b = Spam()
    c = Spam()
    print(printNumInstances())
    print(printNumInstances())