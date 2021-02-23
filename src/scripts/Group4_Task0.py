#Group4_Task0.py
#Data Filtering and Cleaning
#Goal is to isolate data related to the city Bradford.

def Bradford2019():
    #Accidents2019 file
    file = open("../../data/raw/Road Safety Data - Accidents 2019.csv", "r")
    file = file.read()
    #split file into a list of strings
    file_strings = file.split("\n")[:-1]
    #split each string in the list into another level of lists
    file_list = []
    for line in file_strings:
        file_list.append(line.split(","))
    #isolate lists of values relating to Bradford
    Bradford_Accidents = []
    for list in file_list:
        #"variable lookup.xls" file indicates that the "Local Authority (District)" variable has Bradford set as "200"
        if list[12] == "200":
            Bradford_Accidents.append(list)
    
    #create file for the new Accidents2019 list
    Bradford_A = open("../../data/processed/Bradford - Accidents2019.csv", "a")
    #remove contents of file in case it exists already
    Bradford_A.truncate(0)
    #add variable names line to the new file
    Bradford_A.write(file_strings[0] + "\n")
    #add the rest of the values
    for list in Bradford_Accidents:
        for value in list: 
            Bradford_A.write(value + ",")
        Bradford_A.write("\n")
    
    #create a list for the "Accident_Index" variables' values relating to Bradford
    Bradford_Index = []
    for accident in Bradford_Accidents:
        Bradford_Index.append(accident[0])
    
    #Casualties2019 file
    file = open("../../data/raw/Road Safety Data - Casualties 2019.csv", "r")
    file = file.read()
    #split file into a list of strings
    file_strings = file.split("\n")[:-1]
    #split each string in the list into another level of lists
    file_list = []
    for line in file_strings:
        file_list.append(line.split(","))
    #use "Accident_Index" variable to isolate lists of values in Vehicles2019 file
    Bradford_Casualties = []
    for list in file_list:
        if list[0] in Bradford_Index:
            Bradford_Casualties.append(list)
    
    #create file for the new Casualties2019 list
    Bradford_C = open("../../data/processed/Bradford - Casualties2019.csv", "a")
    #remove contents of file in case it exists already
    Bradford_C.truncate(0)
    #add variable names line to the new file
    Bradford_C.write(file_strings[0] + "\n")
    #add the rest of the values
    for list in Bradford_Casualties:
        for value in list: 
            Bradford_C.write(value + ",")
        Bradford_C.write("\n")
    
    #Vehicles2019 file
    file = open("../../data/raw/Road Safety Data- Vehicles 2019.csv", "r")
    file = file.read()
    #split file into a list of strings
    file_strings = file.split("\n")[:-1]
    #split each string in the list into another level of lists
    file_list = []
    for line in file_strings:
        file_list.append(line.split(","))
    #use "Accident_Index" variable to isolate lists of values in Vehicles2019 file
    Bradford_Vehicles = []
    for list in file_list:
        if list[0] in Bradford_Index:
            Bradford_Vehicles.append(list)
    
    #create file for the new Vehicles2019 list
    Bradford_V = open("../../data/processed/Bradford - Vehicles2019.csv", "a")
    #remove contents of file in case it exists already
    Bradford_V.truncate(0)
    #add variable names line to the new file
    Bradford_V.write(file_strings[0] + "\n")
    #add the rest of the values
    for list in Bradford_Vehicles:
        for value in list: 
            Bradford_V.write(value + ",")
        Bradford_V.write("\n")
    

def main():
    Bradford2019()


if __name__ == "__main__":
    main()