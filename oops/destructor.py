
class Test:

    def __init__(self):
        print("Constructor called")

    def __del__(self):
        print("Destructor Called")

import time
# t1 = Test()
# t2 = t1
# t3 = t1

# del t1
# print("t1 deleted")
# time.sleep(5)
# del t2 
# print("t2 deleted")
# time.sleep(5)
# del t3
# print("t3 deleted")
# time.sleep(5)


l = [Test(), Test(), Test(), Test(), Test(), Test(), Test()]
del l
print("Application ended")