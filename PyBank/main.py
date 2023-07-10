# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 17:03:03 2023

@author: rontr
"""
# import the packages/modules you'll need
import os
import csv

# Where is your file stored on your computer? Note the double slash
path = "Resources"

# What is Your File Called?
file_name = "budget_data.csv"
print(file_name)
# using os package to generate a file path
file_path=os.path.join(path, file_name)

# open the file
with open(file_path) as file:
    csvreader=csv.reader(file,delimiter=',')

## Remove the Header from the count
    csvheader=next(csvreader)
## Create Variable for Insights
    

## Create List for Average Change
    myList = []

    firstRow=next(csvreader)
    total=int(firstRow[1])
    maxchangemonth=firstRow[0]
    minchangemonth=firstRow[0]
    maxchange=0
    minchange=0
    totalchange=0
    prevTotal=firstRow[1]
## Count number of months in first column   
    counter = 1
    for row in csvreader:
        counter = counter + 1
        total = total + int(row[1])
        change=int(row[1])-int(prevTotal)
        prevTotal=int(row[1])
        if maxchange < change:
            maxchange = change
            maxchangemonth = row[0]
        elif minchange > change:
            minchange = change
            minchangemonth=row[0]
        totalchange = totalchange + change
        print(row)
        
    print ("Total Months: " + str(counter))
    print("Total: " + str(total))
    print("Average Change: " + str(totalchange/counter))
    print("Greatest Increase in Profits: " + str(maxchangemonth) + "($" + str(maxchange)+")")
    print("Greatest Decrease in Profits: " + str(minchangemonth) + "($" + str(minchange)+")")
    
    with open("PyBank.txt", mode="wt") as f:
        f.write("Total Months: " + str(counter) + "\n")
        f.write("Total: " + str(total) + "\n")
        f.write("Average Change: " + str(totalchange/counter) + "\n")
        f.write("Greatest Increase in Profits: " + str(maxchangemonth) + " ($" + str(maxchange) + "\n")
        f.write("Greatest Decrease in Profits: " + str(minchangemonth) + " ($" + str(minchange) + "\n")
    
   
    
    
    
## Get the total of column 2
    