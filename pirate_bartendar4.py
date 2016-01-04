questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
 }

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
 }

drink_pref = {}

def fav_drink(): 
   """I find out your favorite drink"""  
   for key, value in questions.items():
    drink_type = input(value + " " + "-> Enter y or n  ")
    if drink_type == 'y' or 'yes':
       drink_pref[key] = (drink_type)
    print (drink_pref)  # i output a value by using the return statement

if __name__ == '__main__':
   fav_drink()