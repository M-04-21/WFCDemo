options = ['DeepWater', 'Water', 'Coast', 'Grass', 'Forest']

rules = {
    'DeepWater': ['DeepWater', 'Water'],
    'Water': ['DeepWater', 'Water', 'Coast'],
    'Coast': ['Water', 'Coast', 'Grass'],
    'Grass': ['Coast', 'Grass', 'Forest'] ,
    'Forest': ['Grass', 'Forest']
}

chances = {
    'DeepWater' : {'DeepWater' : 1,'Water' : 1},
    'Water': {'DeepWater': 0.5, 'Water': 0.5, 'Coast': 1},
    'Coast': {'Water': 1, 'Coast': 1, 'Grass': 1},
    'Grass': {'Coast': 1, 'Grass': 2, 'Forest': 0.5} ,
    'Forest': {'Grass': 2, 'Forest': 0.5}
}

defaultChances = {'DeepWater' : 1, 'Water': 1, 'Coast': 1, 'Grass': 1, 'Forest': 1}
