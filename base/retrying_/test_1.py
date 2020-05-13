import random
from retrying import retry 

count = 0

@retry
def have_a_try():
    global count
    count += 1
    if random.randint(1,10) != 5:
        print('trying')
        count +=1
        raise Exception("It's not 5!")
    print("Try %d times" %count)

if __name__ == '__main__':
    have_a_try()