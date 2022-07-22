from recipe_scrapers import scrape_me

recipe = scrape_me('https://www.allrecipes.com/recipe/281089/state-fair-lemonade/')
print(recipe)

title = recipe.title()
ingredients = recipe.ingredients()


print('recipe:', title)
print('total time:', recipe.total_time())
print('ingredients:', ingredients)
print('instructions:', recipe.instructions())
print('image url:', recipe.image())
print('source:', recipe.host())
print('url:', recipe.canonical_url())
