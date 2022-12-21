def describe_city(city_name, country):
    """takes input of a city and country"""
    print(f"{city_name.title()} is in {country.title()}.")


describe_city('moscow', 'russia')
describe_city(city_name='st. petersburg', country='russia')
describe_city('tampa', 'florida')
