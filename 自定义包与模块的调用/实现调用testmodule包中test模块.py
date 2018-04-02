'''
import testmodule.test
a1=testmodule.test.fun7()()
print(a1)
'''
from testmodule import test
a1=test.fun7()()
print(a1)