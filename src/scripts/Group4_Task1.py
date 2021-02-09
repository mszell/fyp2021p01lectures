#Group4_Task1.py
#Single Variable Analysis
#Goal is to make an analysis of accidents in Bradford relative to age groups, time, and ???

#Interesting variables
    #Road Type
    #Pedestrian Crossing-Human Control
    #Pedestrian Crossing-Physical Facilities
    #Light Conditions

import collections

def age_analysis():
    #Bradford Casualties2019 file
    file = open("data/Bradford/Bradford - Casualties2019.csv", "r")
    file = file.read()
    #split file into a list of strings
    file_strings = file.split("\n")[:-1]
    #split each string in the list into another level of lists
    file_list = []
    for line in file_strings[1:]:
        file_list.append(line.split(","))
    
    #create list of the age band for each accident
    age_groups = [line[6] for line in file_list]
    #create frequency dictionary for each age band in the list
    frequency = collections.Counter(age_groups)
    print(frequency)


def time_analysis():
    #Bradford Accidents2019 file
    file = open("data/Bradford/Bradford - Accidents2019.csv", "r")
    file = file.read()
    #split file into a list of strings
    file_strings = file.split("\n")[:-1]
    #split each string in the list into another level of lists
    file_list = []
    for line in file_strings[1:]:
        file_list.append(line.split(","))
    
    #create list of the day of the week for each accident
    day_of_week = [line[10] for line in file_list]
    #create frequency dictionary for each day of the week in the list
    frequency = collections.Counter(day_of_week)
    print(frequency)


def main():
    age_analysis()
    time_analysis()


if __name__ == "__main__":
    main()