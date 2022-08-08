


materials = ['.steel', '.galvanized_steel', '.stainless_steel']
items = ['bubble_cap', 'distillation_tray']
tray_prefix = ['', 'advanced_', 'dense_']
cap_prefix = ['', 'micro_', 'nano_']


def toJson():
    name = prefix + item + material
   
    #Write .json model file
    json = '{"parent": "item/generated","textures": {"layer0": "tkcya:items/metaitems/' + name + '"}}'
    with open('output/metaitems/' + name + '.json', 'w') as model:
        model.write(json)


for item in items:
    for material in materials:
        if item == 'bubble_cap':
            for prefix in cap_prefix:
                toJson()
        elif item == 'distillation_tray':
            for prefix in tray_prefix:
                toJson()
