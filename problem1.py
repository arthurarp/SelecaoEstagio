dicts = [
  {'nome': 'Arthur', 'idade': 23},
  {'nome': 'Alberto', 'idade': 22},
  {'nome': 'Maria', 'idade': 25},
  {'nome': 'Luciana', 'idade': 70},
  {'nome': 'Alberto', 'idade': 37},
  {'nome': 'Luciana', 'idade': 50}
]

set_structure = set() 

for each_dict in dicts:
  if 'nome' in each_dict:
    set_structure.add(each_dict['nome'])

print(list(set_structure))