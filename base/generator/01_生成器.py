def gen(x):
    for i in range(x):
        yield i**2

gene = gen(5)
print(next(gene))