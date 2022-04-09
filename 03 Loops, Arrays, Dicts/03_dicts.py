empty_dict = {}

grades = {
    'John': 'A',
    'Emily': 'A+',
    'Betty': 'B',
    'Mike': 'C',
    'Ashley': 'A'
}

print(grades['Betty'])
print(grades.keys())
print(grades.values())

for key in grades:
  print(key)

for k,v in grades.items():
  print(k,v)