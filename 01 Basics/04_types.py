# Python is dynamically and strongly typed, 
# the types of the variables are figured out by the interpreter
# but you can't just mix up types when working with them

s = "GDSC KIIT" # string
a = 100 # int
b = 2.3 # float
d = 10e5 # float again, this is 10 * 10^5

# What happens when we try to add a string to an int ?

print(s + a) # ??


# You can transform the types of variables

string_a = str(a)
print(string_a, type(string_a))

int_b = int(b)
print(int_b, type(int_b))