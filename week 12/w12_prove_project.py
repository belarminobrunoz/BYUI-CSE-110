# year_of_interest = int(input("Enter the year of interest: "))

with open("week 12/life-expectancy.csv") as life_expec_file:

    max_life_expec = 0
    max_life_expec_country = ''
    max_life_expec_year = 0

    min_life_expec = 9999
    min_life_expec_country = ''
    min_life_expec_year = 0

    drop_from_previous_year = 0



    for linha in life_expec_file:

        line = linha.split(',')
        # print(line)
        if line[0] != 'Entity':
            country_name = line[0]
            country_code = line[1]
            year = int(line[2])
            life_expec_in_years = float(line[3])


            if life_expec_in_years > max_life_expec:
                max_life_expec = life_expec_in_years
                max_life_expec_country = country_name
                max_life_expec_year = year
            
            if life_expec_in_years < min_life_expec:
                min_life_expec = life_expec_in_years
                min_life_expec_country = country_name
                min_life_expec_year = year
                    

    print(f"The min_life_expec was {min_life_expec:.2f} at {min_life_expec_country} in {max_life_expec_year}")
    print(f"The and the max_life_expec was {max_life_expec:.2f} at {max_life_expec_country} in {max_life_expec_year}")
        
# TASKS
# OK - Find the lowest value for life expectancy and the highest value for life expectancy in the dataset. 
# Identify the year and country that has the largest drop from one year to the next.
# Allow the user to type in a country, then show the minimum, maximum, and average life expectancy for that country.
# Look for interesting anomalies or patterns in the data.