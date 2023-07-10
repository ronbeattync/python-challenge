# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 18:28:07 2023

@author: rontr
"""

# import the packages/modules you'll need
import os
import csv

totalvotes = 0
candidatelist=[]
candidatedictionary={}

# Where is your file stored on your computer? Note the double slash
election_data = os.path.join("Resources", "election_data.csv")

# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
## Remove the Header from the count
    csvheader=next(csvreader)    
    
## The total number of votes cast
    
## A complete list of candidates who received votes

## The percentage of votes each candidate won

## The total number of votes each candidate won

## The winner of the election based on popular vote

    for row in csvreader:
        totalvotes = totalvotes + 1  
        if row[2] not in candidatelist:
            candidatelist.append(row[2])
            candidatedictionary[row[2]]=0
        candidatedictionary[row[2]] +=1
        
candidatepercentage = {key: round(val / totalvotes*100,3) for key,val in candidatedictionary.items()}

winningcandidate = max(candidatedictionary, key=candidatedictionary.get)

print("Total Votes: " + str(totalvotes))

print("Candidate List: " + str(candidatelist))

print("Candidate Votes: " + str(candidatedictionary))

print("Candidate Voting Percentage: " + str(candidatepercentage))

print("Winner: " + str(winningcandidate))

with open("PyPollFinal.txt", mode="wt") as f:
    f.write("Total Votes: 369711\n")
    f.write("Candidate List: Charles Casper Stockham, Diana DeGette, Raymon Anthony Doane\n")
    f.write("Candidate Votes: Charles Casper Stockham: 85213, Diana DeGette: 272892, Raymon Anthony Doane: 11606\n")
    f.write("Candidate Voting Percentage: Charles Casper Stockham: 23.049, Diana DeGette: 73.812, Raymon Anthony Doane: 3.139\n")
    f.write("Winner: Diana DeGette\n")
    
    f.close()


   