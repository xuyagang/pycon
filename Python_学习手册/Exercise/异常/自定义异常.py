class Bad(Exception):
    pass

def doomed():
    raise Bad

try:
    doomed()
except Bad:
    print('Got Bad')