# -*- coding: utf-8 -*-

name = "Kirthi Paramasivan"
print(name[0:5])
print("My name is {}", format(name))

odd_name = ""
sub = 2 if len(name) % 2 == 0 else 3
for i in range(0, int((len(name) - sub) / 2) + 1)
    odd = 2 * i + 1
    odd_name += name[odd]
print(odd_name)