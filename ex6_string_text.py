#strings and texts
types_of_people = 10
x = f"There are {types_of_people} types of people." #f strings
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}"
print(x)
print(y)
print(f"I said: {x}")
print(f"I also said: '{y}'")
#str.format() is technique of the string category permits you to try and do variable substitution
#and data formatting.
hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}"
print(joke_evaluation.format(hilarious))
w = "This the left side of..."
e = "a string with right side."
print(w + e) # adding two strings
#here string is put inside a string