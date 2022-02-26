
# list of variables
i = 0
lowest = 999
lowest_country = ''
lowest_year = ''
highest = 0
highest_country = ''
highest_year = ''
life_total = 0
avg_life = 0
num_interest_years = 0

# variables for choice year
choice_year = int(input('Enter the year of interest: '))
choice_lowest = 999
choice_highest = 0

# variables for choice country
choice_country = input('What country would you like to learn more about? ')
choice_country_min = 999
choice_country_max = 0
country_life_avg = 0
country_life_total = 0
country_num_interest_years = 0

with open('life-expectancy.csv') as life_expectancy:
    
    for line in life_expectancy:
        i += 1
        cleanline = line.strip()
        parts = cleanline.split(',')

        # This IF is used to get all the information exxpect the first line, which is headings
        if i > 1:
            country = parts[0]
            year = int(parts[2])
            life = float(parts[3]) 
            
            # to find the lowest life expectancy with the year and country
            if lowest > life:
                lowest = life
                lowest_year = year
                lowest_country = country

            # to find the highest life expectancy with the year and country
            if highest < life:
                highest = life
                highest_year = year
                highest_country = country

            # use to calculate the average life of interested year
            if choice_year == year:
                life_total += life
                num_interest_years += 1

                # to find the lowest life expectancy and country of interested year
                if choice_lowest > life:
                    choice_lowest = life
                    choice_lowest_year = year
                    choice_lowest_country = country

                # to find the highest life expectancy and country of interested year
                if choice_highest < life:
                    choice_highest = life
                    choice_highest_year = year
                    choice_highest_country = country

            # use to calculate the average life of the users choice of country
            if country.lower() == choice_country.lower():
                country_life_total += life
                country_num_interest_years += 1

                # to find the lowest life expectancy of choice of country
                if choice_country_min > life:
                    choice_country_min = life

                # to find the highest life expectancy of choice country
                if choice_country_max < life:
                    choice_country_max = life


avg_life = life_total / num_interest_years
choice_country_avg = country_life_total / country_num_interest_years

print(f'The overall max life expectancy is: {highest} from {highest_country} in {highest_year}')
print(f'The overall min life expectancy is: {lowest} from {lowest_country} in {lowest_year}')
print()
print(f'For the year {choice_year}:')
print(f'The average life expectancy across all reporting counties was {avg_life}')
print(f'The max life expectancy was in {choice_highest_country} with {choice_highest}')
print(f'The min life expectancy was in {choice_lowest_country} with {choice_lowest}')
print()
print(f'For {choice_country.capitalize()}, the min life expectancy is {choice_country_min}, the max is {choice_country_max}, and the average is {choice_country_avg}')