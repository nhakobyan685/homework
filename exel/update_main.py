import argparse


#-------------------------#
'''
    Description: checks if the library is not there, if it is not there, it imports the os 
            library into the program and with the os.system() method, it installs 
            xlsxwriter and rotates this text, after that the program continues to 
            work library not found, installing...
'''
#-------------------------#
try:
    import xlsxwriter
except ImportError:
    print("xlsxwriter library not found, installing...")
    import os
    os.system('pip3 install xlsxwriter')
    import xlsxwriter as xw


#-------------------------#
'''
    Description: this checks if it received an invalid argument or if it received 
        an invalid argument from the CLI (command line interface) prints this 
        Invalid argument received from the CLI and prints the error received 
        from argparse.ArgumentError exits the programthis function checks if it received an invalid argument or if it received an invalid argument 
        from the CLI (command line interface) prints this Invalid argument received from the CLI and prints the error received from argparse.ArgumentError exits the programthis function checks if it received an invalid argument or if it received an invalid argument from the CLI (command line interface) prints this Invalid argument received from the CLI and prints the error received from argparse.ArgumentError exits the programan invalid argument or if it received an invalid argument from the CLI (command line interface) prints this Invalid argument received from the CLI and prints the error received from argparse.ArgumentError exits the program
'''
#-------------------------#
try:
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                        help='an integer for the accumulator')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
    args = parser.parse_args()
except:
    print("Invalid argument received from the command line")
    exit(1)

print(args.accumulate(args.integers))


# Database
data = [
    {
        "name":"Keith",
        "surname":"Sheppard",
        "age":26,
        "phone":37498252241
    },
    {
        "name":"Micheal",
        "surname":"Washington",
        "age":18,
        "phone":37477404980
    },
    {
        "name":"Matthew",
        "surname":"Moreno",
        "age":76,
        "phone":37496485732
    },
    {
        "name":"Marcus",        
        "surname":"Hodges",
        "age":47,
        "phone":37495749139
    },
    {
        "name":"Patricia", 
        "surname":"Martin",
        "age":35,
        "phone":37494598282
    },    
    {
        "name":"Amanda",
        "surname":"Wolf",
        "age":35,
        "phone":37499342540
    },
    {
        "name":"Robin",
        "surname":"Rose",
        "age":35,
        "phone":37433441589
    },
    {
        "name":"Meghan",
        "surname":"Taylor",
        "age":35,
        "phone":37444578501
    }
]



parser = argparse.ArgumentParser(description='This program is designed to prepare a database and to add data. The background of people aged 25 years or older is green and the rest of the boxes are gray and the data will be added to the database when the data is transferred from outside.')
parser.add_argument('-N','--name', type=str, required=True, help='Add name argument like this -name Trump or -N Trump')
parser.add_argument('-S','--surname', type=str, required=True, help='Add surname argument like this -surname Smith  or -S Smith')
parser.add_argument('-A','--age', type=int, required=True, help='Add age argument like this -age 18 or -A 18 ')
parser.add_argument('-P','--phone', type=int, required=True, help='Add phone argument like this -phone 374000000 or -P 374000000 ')

args = parser.parse_args()

new_data = {
    "name": args.name,
    "surname": args.surname,
    "age": args.age,
    "phone": args.phone
}

data.append(new_data)


# make workbook
workbook = xw.Workbook('db.xlsx')
worksheet = workbook.add_worksheet('Data')


# paint header yellow
header_color = workbook.add_format(
    {
        "bg_color": "#fcbe03"
    }
)


# white backround color checnge gray
white_bg_color = workbook.add_format(
    {
        "bg_color":"gray"
    }
)


# write xlsx file
worksheet.write(0, 0, "id", header_color)
worksheet.write(0, 1, "Name", header_color)
worksheet.write(0, 2, "Age", header_color)
worksheet.write(0, 3, "Phone", header_color)


# worksheet column color
worksheet.set_column(0, 5, 20)


# make loop for header
for index, entry in enumerate(data):
    worksheet.write(index+1, 0, str(index), white_bg_color)
    worksheet.write(index+1, 1, entry["name"], white_bg_color)
    worksheet.write(index+1, 2, entry["age"], white_bg_color)
    worksheet.write(index+1, 3, entry["phone"], white_bg_color)

    # Apply conditional formatting for age >= 25
    if entry["age"] >= 25:
        format = workbook.add_format({"bg_color": "green"})
        worksheet.conditional_format(index+1, 2, index+1, 2, {"type": "cell", "criteria": ">=", "value": 25, "format": format})


# save file xlsx
workbook.close()
