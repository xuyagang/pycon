# https://www.colabug.com/2018/0721/3655465/


# # In the earlier versions of python ,you'd do:
# def divide(divisor, dividend):
#     import pdb; pdb.set_trace()
#     return dividend / divisor

# if __name__ == '__main__':
#     print(divide(0, 2))


# with python3.7 you'd do:
def divide(divisor, dividend):
    breakpoint()
    return dividend / divisor

if __name__ == '__main__':
    print(divide(0, 99))