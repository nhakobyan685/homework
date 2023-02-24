#!/bin/bash/python3


import xlsxwriter as xw


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


# make workbook
workbook = xw.Workbook('db.xlsx')
worksheet = workbook.add_worksheet('Data')


# paint header yellow
header_color = workbook.add_format(
    {
        "bg_color":"#fcbe03",

    }
)


# write xlsx file
worksheet.write(
        0,
        0, 
        "id",
        header_color
)
worksheet.write(
        0, 
        1, 
        "Name",
        header_color
)
worksheet.write(
        0, 
        2, 
        "Age",
        header_color
)
worksheet.write(
        0, 
        3, 
        "Phone",
        header_color
)


# worksheet column color
worksheet.set_column(
        0,
        5,
        20
)


# make loop for header
for index, entry in enumerate(data):
    worksheet.write(index+1, 0, str(index))
    worksheet.write(index+1, 1, entry["name"])
    worksheet.write(index+1, 2, entry["age"])
    worksheet.write(index+1, 3, entry["phone"])


# save file xlsx
workbook.close()
