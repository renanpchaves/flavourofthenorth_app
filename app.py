import os 

#premade list
restaurants = [
    {'Name': 'Velen', 'Category':'Barons', 'Active': False},
    {'Name': 'Novigrad', 'Category': 'Bards', 'Active': True},
    {'Name': 'Skellige', 'Category': 'Isle', 'Active': False}
]

#root functions
def header(text):
    os.system('cls')
    lines = '*' * (len(text))
    print (lines)
    print(text)
    print (lines)
    print()

def to_menu():
    input ('\nPress any key to go back to the menu.')

def app_name():
    print ('【﻿Ｆｌａｖｏｕｒ　ｏｆ　ｔｈｅ　Ｎｏｒｔｈ】\n')

def terminate_app():
    header ('Closing the application\n')

def invalid_option():
    print ('Invalid option')
    to_menu()

#main menu view
def show_options():
    print ('1. Submit new restaurant')
    print ('2. Restaurant Catalog')
    print ('3. Switch restaurant status')
    print ('4. Exit\n')

#main functions
def new_restaurant():
    '''This function is responsible for creating new restaurants
    
    Inputs:
    -Restaurant name
    -Category

    Outputs:
    Adds a new restaurant to the catalog
    '''

    header ('Register new restaurants: \n')

    opcao = input ('To register a new restaurant, type 1. To go back to the main menu, type in any key.\n\n')

    if opcao == ('1'):
        restaurant_name = input ('Type in the restaurant name: \n')
        category = input(f'Type in the category of {restaurant_name}: \n')
        restaurant_data = {'Name': restaurant_name, 'Category': category, 'Active':False}
        restaurants.append(restaurant_data)
        print (f'The restaurant {restaurant_name} has been registered in the app.')
    
    to_menu()

def restaurant_catalog():
    '''This function is responsible for listing restaurants
    
    Output: Show restaurants catalog list.
    '''

    header ('Restaurant listing: ')

    print (f'{'Restaurant Name'.ljust(22)} | {'Category'.ljust(20)} | Status')
    for restaurant in restaurants:
        restaurant_name = restaurant['Name']
        category = restaurant['Category']
        active = 'Activated' if restaurant['Active'] else 'Deactivated'
        print (f'- {restaurant_name.ljust(20)} | {category.ljust(20)} | {active}')
    to_menu()

def switch_status():
    '''This function is responsible for switching restaurants status
    
    Inputs: Restaurant's name

    Output: Switches restaurants status and shows the user a message on doing so.
    '''
    
    header ('Switching restaurant status...')

    restaurant_name = input('Type in the restaurant\'s name: \n\n')
    restaurant_found = False

    for restaurant in restaurants:
        if restaurant_name == restaurant['Name']:
            restaurant_found = True
            restaurant['Active'] = not restaurant['Active']
            message = f'The restaurant {restaurant_name} has been successfully activated' if restaurant['Active'] else f'The restaurant {restaurant_name} has been successfully deactivated.'
            print(message)
    if not restaurant_found:
        print('Restaurant not found.')
    to_menu()

#merging all functions with options
def selection_menu():
    try:
        chosen_option = int(input ('Escolha uma opção: '))
        if chosen_option == 1:
            new_restaurant()
        elif chosen_option == 2:
            restaurant_catalog()
        elif chosen_option == 3:
            switch_status()
        elif chosen_option == 4:
            terminate_app()
            return False
        else:
            invalid_option()
    except:
        invalid_option()
    return True

#main
def main():
    while True:
        os.system('cls')
        app_name()
        show_options()

        recommence = selection_menu()
        if not recommence:
            break

if __name__ == '__main__':
    main()