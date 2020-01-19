def get_location(city, country, population=''):
    if population == '':
        return f'{city.title()}, {country.title()}'
    else:
        return f'{city.title()}, {country.title()} - population {population}'


print(get_location('moscow', 'russia'))
