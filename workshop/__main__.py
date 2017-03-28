import workshop
import sys


if len(sys.argv) < 1:
    print("Yo dawg you need to give one argument of a file that needs fitting")
else:
    workshop.fit(sys.argv[1])
