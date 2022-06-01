import yaml

with open('super_market.yaml') as file:
    try:
        database = yaml.safe_load(file)   
        print(database)
    except yaml.YAMLError as exception:
        print(exception)