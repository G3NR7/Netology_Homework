import pprint


def get_cook_book():
    cook_book = {}
    with open ('recipes.txt', 'r', encoding='utf-8') as f:
        book = []
        count_lines = 1
        temp_key = None
        for line in f:
            if line.strip() == '':
                continue
            elif count_lines == 1:
                temp_key = line.strip()
                cook_book[temp_key] = []
                count_lines += 1
            elif count_lines == 2:
                count_lines = count_lines + int(line.strip()) 
            elif count_lines > 2:
                temp= line.strip().split(' | ')
                cook_book[temp_key] += [{'ingredient_name': line.strip().split(' | ')[0], 'quantity': int( line.strip().split(' | ')[1]), 'measure':  line.strip().split(' | ')[2]}]
                if count_lines > 3:
                    count_lines -= 1
                else:
                    count_lines = 1
    return cook_book

def get_shop_list_by_dishes(dishes: list =None, person_count: int =None):
    сook_book = get_cook_book() # Тут получаб книгу рецеатов!!
    required_ingredients = {}
    keys_list = [] #Общий список ключей(ингридингтов)
    for i in dishes:
        for j in range(len(сook_book[i])):
            keys_list += сook_book[i][j]['ingredient_name'].split('\n')
    print(f'Книга рецептов:')
    pprint.pp(сook_book, width=100)
    for d in dishes:
        for i in range(len(сook_book[d])):
            if  required_ingredients.get(сook_book[d][i]['ingredient_name']) == None: # Если Не существует
                required_ingredients[сook_book[d][i]['ingredient_name']] =  {'quantity': сook_book[d][i]['quantity'], 'measure': сook_book[d][i]['measure']} # Создает ключ:значение
            elif сook_book[d][i]['ingredient_name'] in set(keys_list):
                required_ingredients[сook_book[d][i]["ingredient_name"]]["quantity"] += сook_book[d][i]["quantity"] # Суммирует значение из сook_book с значением в required_ingredients
    print(f'Требуемые ингредиенты:')
    pprint.pp(required_ingredients)

def main():
    get_shop_list_by_dishes(['Омлет', 'Фахитос'])

if __name__ == "__main__":
    main()