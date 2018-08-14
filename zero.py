# step 0
zero_0 = lambda f: lambda x: x
toInt_0 = lambda n: n(lambda x: x + 1)(0)

print("Step 0: {}".format(toInt_0(zero_0)))
print("=======================================\n")

# step 1


def zero_1(f):
    print('step 1: zero_1 - {} is getting ignored'.format(f))
    # note that f parameter is ignored
    return lambda x: x


def toInt_1(f):
    print('step 1: toInt_1 - {}'.format(f))
    # calling f with parameter lambda x: x + 1
    # in this case f == zero_1
    # zero_1 returns lambda x: x (zero_1 ignores the f parameter)
    # the returning lambda is executed with 0 as parameter
    # which results in 0
    return f(lambda x: x + 1)(0)


print("Step 1: {}".format(toInt_1(zero_1)))
print("=======================================\n")

# step 2


def zero_2(f):
    print('step 2: zero_2 - {} is getting ignored'.format(f))
    return lambda x: x


def plus_one_2():
    print('step 2: plus_one_2')
    return lambda x: x + 1


def toInt_2(f):
    print('step 2: toInt_2 - {}'.format(f))
    # calling f with parameter plus_one_2
    # in this case f == zero_2
    # zero_2 returns lambda x: x (zero_2 ignores the f parameter)
    # the returning lambda is executed with 0 as parameter
    # which results in 0
    return f(plus_one_2)(0)


print("Step 2: {}".format(toInt_2(zero_2)))
print("=======================================\n")

# step 3


def zero_3(f):
    print('step 3: zero_3 - {} is getting ignored'.format(f))
    return lambda x: x


def plus_one_3():
    print('step 3: plus_one_3')
    return lambda x: x + 1


def toInt_3(f):
    print('step 3: toInt_3 - {}'.format(f))
    # calling f with parameter plus_one_3
    # in this case f == zero_3
    # zero_3 returns lambda x: x (zero_3 ignores the f parameter)
    # the returning lambda is executed with 0 as parameter
    # which results in 0
    result = f(plus_one_3)
    print('step 3: result - {}'.format(result))

    return result(0)


print("Step 3: {}".format(toInt_3(zero_3)))
print("=======================================\n")
