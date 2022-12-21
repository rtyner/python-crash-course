def city_country(city_name, country):
    formatted_text = f"{city_name}, {country}"
    return formatted_text.title()


place = city_country('belgrade', 'serbia')
print(place)
place = city_country('st. petersburg', 'russia')
print(place)
place = city_country('moscow', 'russia')
print(place)
