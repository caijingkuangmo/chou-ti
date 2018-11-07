from django.test import TestCase

# Create your tests here.

# class Foo(object):
#
#     def get(self, name):
#         print(name)
#
#     def list(self):
#         return [Foo.get]
#
#
# obj = Foo()
# for i in obj.list():
#     i(obj,'123')


# class Foo:
#
#     def __str__(self):
#         return 'foo'
#
# f = Foo()
# print(getattr(f, '__str__'))


class Foo(object):
    pass

foo = Foo()
for i in foo:
    print(i)