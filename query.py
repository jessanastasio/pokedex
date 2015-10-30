import requests
import json
 
BASE_URL = 'http://pokeapi.co'
 
def query_pokeapi(resource_url):
    url = '{0}{1}'.format(BASE_URL, resource_url)
    response = requests.get(url)
 
    if response.status_code == 200:
        return json.loads(response.text)
    return None

userInput = raw_input('Enter your pokemon: ')
 
pokemon = query_pokeapi('/api/v1/pokemon/'+userInput+'/')
 
sprite_uri = pokemon['sprites'][0]['resource_uri']
description_uri = pokemon['descriptions'][0]['resource_uri']
 
sprite = query_pokeapi(sprite_uri)
description = query_pokeapi(description_uri)
 
print pokemon['name']
print description['description']
print BASE_URL + sprite['image']
