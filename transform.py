def transform(data):
    transformed_data = [{
        "Weather": data["weather"][0]["main"],
        "Description": data["weather"][0]["description"],
        "Temperature": data["main"]["temp"],
        "Feels like": data["main"]["feels_like"],
        "Pressure": data["main"]["pressure"],
        "Wind speed": data["wind"]["speed"],
        "Wind direction": data["wind"]["deg"],
        "Clouds": data["clouds"]["all"],
        "City": data["name"]
    }]

    return transformed_data

    # NOTES
    # weather.main, weather.description, 
    # main.temp, main.feels_like, main.pressure,
    # wind.speed, wind.deg (Calculate in which direcion by myself), 
    # clouds.all, clouds.name