import json
from country_codes import get_country_code
# Load the data into a list.
filename = 'Chpt_16/population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Print the 2010 population for each Country

pop_list = []

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + ": " + str(population))
        else:
            print('Error - ' + country_name)
