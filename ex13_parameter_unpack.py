#argument input method to pass variable to script
from sys import argv
script, first, second, third = argv # pass three command line arguments
print("The script is called:",script)
print("Your first variable is:",first)
print("Your second variable is:",second)
print("Your third variable is:",third)