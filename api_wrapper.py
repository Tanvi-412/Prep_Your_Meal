import requests
import json
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('./config/firebase.json')
app = firebase_admin.initialize_app(cred)

db = firestore.client()

url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/random"

querystring = {"number":"10","limitLicense":"false","tags":"mexican"}

headers = {
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    'x-rapidapi-key': "026637f033msh5b5e3f97cabe4ccp1b213ejsn8a44f3ec1d8f"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)

recipe_ref = db.collection(u'test recipe')
user_ref = db.collection(u'test user')

docs = user_ref.where(u'name', u'==', u'Mrunal').stream()

for doc in docs:
    # print(doc.id, doc.to_dict())
    dicti = doc.to_dict()
    # print(dicti)
    refrigerator = dicti['refrigerator']

# print(refrigerator)

query = recipe_ref.where(u'ingredients', u'array_contains', refrigerator).stream()
for doc in query:
    dicti = doc.to_dict()
    print(dicti)



# for recipes in data['recipes']:
#     ingi = []
#     for ingredients in recipes['extendedIngredients']:
#         if ingredients['name']:
#             ingredient_data = {
#                 u'name': ingredients['name']
#             }
#             ingi.append(ingredients['name'])
#             db.collection(u'test ingredients').document(ingredients['name']).set(ingredient_data)

    
#         print(ingredients['id'], ingredients['name'])
#     doc_recipe = {
#         u'vegetarian': recipes['vegetarian'],
#         u'vegan': recipes['vegan'],
#         u'ingredients': ingi,
#         u'instructions': recipes['analyzedInstructions'],
#         u'title': recipes['title']
#     }
#     db.collection(u'test recipe').document(recipes['title']).set(doc_recipe)