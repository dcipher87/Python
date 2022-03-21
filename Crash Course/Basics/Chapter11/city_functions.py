def city_country(city, country, population=''):
    """Returns city, country and population neatly formatted."""
    city = city.title()
    country = country.title()

    # city_and_country = f"{city} {country}"

    if population:
        city_and_country = f"{city} {country} -{population}"
    else:
        city_and_country = f"{city} {country}"

    # return city_and_country.title()
    return city_and_country
  

# city_and_country = city_country("cairo", "egypt")
# print(city_and_country)