#!/usr/bin/python3

class A:

    a = 10

    def __call__(self, x):
        return x + self.a

Aclb = A()

print(Aclb(3))