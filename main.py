with open('recept.txt', encoding='utf-8') as file:
    # res = file.readlines()
    # print(res)
    cook_book = {}
    for line in file:
        file.seek(0)
        dish = file.readline().strip()
        quantity_ingredients = int(file.readline())
        # print(dish)
        ingredients = []
        for i in range(quantity_ingredients):
            ingredient = file.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        cook_book[dish] = ingredients

    print(cook_book)


