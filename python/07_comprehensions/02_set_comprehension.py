# {expression f0o item in itterable if condition}

bucket =["Apple", "mango", "banana", "grapes", "mango", "banana"]

uniqueFruits = {ingredients for ingredients in bucket}
print(uniqueFruits)

recepies ={
    "panner":["panner", "onion", "tomato"],
    "dosha":["batter", "ghee"]
    }
getIngredients = {ingredient for recepie in recepies.values() for ingredient in recepie}
print(getIngredients)