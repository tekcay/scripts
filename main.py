import py.CasingGenerator
import py.NewItemGenerator
import py.JsonModelGenerator
import py.UserInteractions
import py.Globals

Globals.init()

while functionCall != 0:

    UserInteractions.getFunction()

    if functionCall == 1:
        CasingGenerator.init()
    elif functionCall == 2:
        NewItemGenerator.init()
    elif print('Typing error')