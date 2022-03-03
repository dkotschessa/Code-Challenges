"""
Given the provided cars dictionary:

Get all Jeeps
Get the first car of every manufacturer.
Get all vehicles containing the string Trail in their names 
(should work for other grep too)
Sort the models (values) alphabetically
See the docstrings and tests for more details. Have fun!

Update 18th of Sept 2018: as concluded in the forum it is better 
to pass the cars dict into each function to make its scope local.
"""

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    jeeps = cars['Jeep']
    jeepstring = ''
    l = len(jeeps)
    for x in range(l-1):  # I do not like this solution AT ALL
        jeep = jeeps[x]
        jeepstring += jeep + ', '
    jeepstring += jeeps[l-1]  # add the last (no comma)
    return jeepstring


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    models = [x[0] for x in cars.values()]
    return models


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    matching = []
    grep = grep.lower()
    for keys, values in cars.items():
        for model in values:
            if grep in model.lower():
                matching.append(model)
    return sorted(matching)


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    for k, v in cars.items():
        cars[k] = sorted(cars[k])
    return cars