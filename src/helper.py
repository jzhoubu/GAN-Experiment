import numpy as np

def has_multiple_attr(O, attrs):
    flag = 1
    for attr in attrs:
        if not hasattr(O, attr):
            print("Don't has attribute named {}".format(attr))
            flag = 0
    return flag


def Summary(gan):
    assert has_multiple_attr(gan, ["generator", "discriminator","timer"])
    print("The training time is {}".format(gan.timer))
    print("The size of generator is {}".format(sum([array.nbytes for array in gan.generator.get_weights()])))
    print("The size of discriminator is {}".format(sum([array.nbytes for array in gan.discriminator.get_weights()])))