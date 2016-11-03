# if you couldn't tell by the name, this puts a long ass string into your system memory.
# don't run it unless you have an absolute minimum of 8GB of RAM on your computer.
# even with 8GB, the memory will bleed into the swap. would only run this if you have 16GB+
#
# [ but of course I ran it plenty of times on a university iMac with 8GB and an unnamed i5 :-) ]

import random
import sys

ourSuperCoolLongString = ""
for x in range(0, 100): ourSuperCoolLongString += chr(random.randint(0, 255))
for x in range(0, 26): ourSuperCoolLongString = ourSuperCoolLongString + ourSuperCoolLongString

print(str(len(ourSuperCoolLongString)) + " characters\n" + str(sys.getsizeof(ourSuperCoolLongString)) + " bytes")
input()