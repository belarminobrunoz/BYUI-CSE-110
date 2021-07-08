# TASKS - https://byui-cse.github.io/cse110-course/lesson11/prove.html
# OK - Find the lowest value for life expectancy and the highest value for life expectancy in the dataset. 
# Identify the year and country that has the largest drop from one year to the next.
# Allow the user to type in a country, then show the minimum, maximum, and average life expectancy for that country.
# Look for interesting anomalies or patterns in the data.

year_of_interest = int(input("Enter the year of interest: "))

with open("week 12/life-expectancy.csv") as life_expec_file:

    max_life_expec = 0
    max_life_expec_country = ""
    max_life_expec_year = 0

    min_life_expec = 9999
    min_life_expec_country = ""
    min_life_expec_year = 0

    all_life_expec_specif_year = []

    max_life_expec_user_choice = 0
    max_life_expec_country_user_choice = ""
    max_life_expec_year_user_choice = 0

    min_life_expec_user_choice = 9999
    min_life_expec_country_user_choice = ""
    min_life_expec_year_user_choice = 0

    countries = []
    country = ''

    countries_80_life_expec = []
    countries_60_life_expec = []
    countries_40_life_expec = []
    countries_20_life_expec = []
    countries_smaller_20_life_expec = []




    for linha1 in life_expec_file:

        line = linha1.split(",")
        if line[0] != "Entity":
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


            if year_of_interest == year:
                all_life_expec_specif_year.append(life_expec_in_years)

                if life_expec_in_years > max_life_expec_user_choice:
                    max_life_expec_user_choice = life_expec_in_years
                    max_life_expec_country_user_choice  = country_name
                    max_life_expec_year_user_choice  = year
                
                if life_expec_in_years < min_life_expec_user_choice :
                    min_life_expec_user_choice  = life_expec_in_years
                    min_life_expec_country_user_choice  = country_name
                    min_life_expec_year_user_choice  = year
                
                if life_expec_in_years >= 80:
                    countries_80_life_expec.append(country_name)

                elif life_expec_in_years < 80 and life_expec_in_years >= 60:
                    countries_60_life_expec.append(country_name)

                elif life_expec_in_years < 60 and life_expec_in_years >= 40:
                    countries_40_life_expec.append(country_name)

                elif life_expec_in_years < 40 and life_expec_in_years >= 20:
                    countries_20_life_expec.append(country_name)
                elif life_expec_in_years < 20:
                    countries_smaller_20_life_expec.append(country_name)
            
            if country_name != country:
                countries.append(country_name)
                country = country_name




                    

    avg_expec = sum(all_life_expec_specif_year) / len(all_life_expec_specif_year)
    num_countries = len(countries)
    # Here I used a function to sum every item inside the list sum(). I found it in this article: https://medium.com/programminginpython-com/python-program-to-calculate-the-sum-of-elements-in-a-list-ed2b80db8268

    print()
    print("***** RESULTS FROM THE DATA ANALYSIS *****")
    print("--- GENERAL ---")
    print(f"    >>> The min life expectancy was {min_life_expec:.2f} at {min_life_expec_country} in {min_life_expec_year}")
    print(f"    >>> The max life expectancy was {max_life_expec:.2f} at {max_life_expec_country} in {max_life_expec_year}")
    print()
    print(f"--- YEAR {year_of_interest} ---")
    print(f"For the year {year_of_interest}, the year you chose:")
    print(f"    >>> The average life expectancy across all countries was {avg_expec:.2f}")
    print(f"    >>> The min life expectancy was {min_life_expec_user_choice:.2f} at {min_life_expec_country_user_choice} in {min_life_expec_year_user_choice}")
    print(f"    >>> The max life expectancy was {max_life_expec_user_choice:.2f} at {max_life_expec_country_user_choice} in {max_life_expec_year_user_choice}")
    print("===========================================")
    print(f"We have {num_countries} countries in total")
    print(f"    >>> {len(countries_80_life_expec)} of them, have/had life expectancy equal or greater than 80 years")
    if len(countries_80_life_expec) > 0:
        print("        Here are some of them: ")
        count = 0
        for c80 in countries_80_life_expec:
            print(f"        > {c80}")
            count = count +1
            if count == 3:
                print()
                break
            
    print(f"    >>> {len(countries_60_life_expec)} of them, have/had life expectancy between 60 and 79 years")
    if len(countries_60_life_expec) > 0:
        print("        Here are some of them: ")    
        count = 0
        for c60 in countries_60_life_expec:
            print(f"        > {c60}")
            count = count +1
            if count == 3:
                print()
                break
    print(f"    >>> {len(countries_40_life_expec)} of them, have/had life expectancy between 40 and 59 years")
    if len(countries_40_life_expec) > 0:
        print("        Here are some of them: ")  
        count = 0
        for c40 in countries_40_life_expec:
            print(f"        > {c40}")
            count = count +1
            if count == 3:
                print()
                break
    print(f"    >>> {len(countries_20_life_expec)} of them, have/had life expectancy between 20 and 39 years")
    if len(countries_20_life_expec) > 0:
        print("        Here are some of them: ")  
        count = 0
        for c20 in countries_20_life_expec:
            print(f"        > {c20}")
            count = count +1
            if count == 3:
                print()
                break
    print(f"    >>> {len(countries_smaller_20_life_expec)} of them, have/had life expectancy up to 20 years")
    if len(countries_smaller_20_life_expec) > 0:
        print("        Here are some of them: ")  
        count = 0
        for cs20 in countries_smaller_20_life_expec:
            print(f"        > {cs20}")
            count = count +1
            if count == 3:
                print()
                break  
