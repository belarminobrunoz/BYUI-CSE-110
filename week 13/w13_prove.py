# OVERVIEW: https://byui-cse.github.io/cse110-course/lesson13/prove.html

from prettytable import PrettyTable
# I found this lib when trying to print the information in a more organized way. Through it, is possible to create a table with the contents of an array. I found information in this stackoverflow article: https://stackoverflow.com/questions/9535954/printing-lists-as-tabular-data

# START - Functions Section
def calculate_wind_chill(temperature):
    print(f"*"*26+" WIND CHILL AT "+str(temperature)+"°F "+"*"*26)
    print()
    
    # First, I create the table called 'table' and add the headers.

    table = PrettyTable([
        'Speed',
        'Temperature °F', 
        'Windchill °F', 
        'Temperature °C',
        'Windchill °C'
        ])

    # This 'for loop' allows me to loop from 5 to 61 adding 5 numbers instead of 1. So, with that, it is possible to show the speed incrementing 5 to the iterator until we get 60.
    for speed in range(5,61,5):    
        

        wind_chill = 35.74 + (0.6215*temperature) - 35.75*(speed**0.16) + (0.4275*temperature)*(speed**0.16)

        # Here I add the information of the line

        table.add_row([
            str(speed)+" mph",                    # The speed
            temperature,                          # The temperature in Fahrenheit
            round(wind_chill,2),                  # The Windchill in Fahrenheit
            convert_fahr_to_celsius(temperature), # The temperature in Celsius
            convert_fahr_to_celsius(wind_chill)   # The Windchill in Celsius
            ])

    print(table)    
    print()


def convert_celsius_to_fahr(temperature):
    fahr = (temperature *(9/5)) + 32
    return fahr

def convert_fahr_to_celsius(temperature):
    celsius = (temperature-32)*(5/9)
    return round(celsius,2)
# END - Functions Section


# START - Program
print(f"*"*26+" WINDCHILL CALCULATOR"+"*"*26)
temperature_raw = float(input("Please, type the temperature: "))
temp_type = input("What is the unit of measurement: Fahrenheit or Celsius (F/C)? ").upper()

if temp_type == "C":
    temperature = convert_celsius_to_fahr(temperature_raw)
    calculate_wind_chill(temperature)

elif temp_type == "F":
    temperature = temperature_raw
    calculate_wind_chill(temperature)

elif temp_type != "C" and temp_type != "F":
    print(f"{temp_type} is not acceptable. Choose F for Fahrenheit and C for Celsius to see the windchill in diferents speeds.")