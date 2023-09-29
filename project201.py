
# 1. Ask for user input -> ditto
# 2. Create a dynamic URL based on step 1
# 3. Fetch the data from the url in step 2
# 4. Convert JSON to a dictionary
# 5. Print out pokemon data

import requests
while True:
    user_input = input("enter the value: ")
    url = f"https://pokeapi.co/api/v2/pokemon/{user_input}"
    req= requests.get(url)
    if req.status_code == 200:
        character = req.json()
    
        print(character['weight'])
        print(character["name"])
        # print(character)
        for ability in character["abilities"]:
            
            print([ability],['name'])
    else:
        print('please put the valid input')


