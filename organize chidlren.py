#read the csv file and create a nested list
import csv
import json
source = 'output.csv'
output = 'output.json'
data = []
with open(source, 'r') as f:
    reader = list(csv.DictReader(f))
    for row in reader:
        #if the parent is 0, create a new list, add the current line to the list
        if(row['parent'] == '0'):
            # print(row)
            data.append(row)
        else:
            pass
    for line in data:
        line['children'] = []
        for row in reader:
            print(row)
            if(row['parent'] == line['id']):
                line['children'].append(row)
            else:
                pass

    # Reset reader
    reader = list(csv.DictReader(open(source, 'r')))
    
    for line in data:
        # print(line)
        for child in line['children']:
            child['children'] = []
            for row in reader:
                if(row['parent'] == child['id']):
                    child['children'].append(row)
                else:
                    pass

    # Reset reader
    reader = list(csv.DictReader(open(source, 'r')))
    
    #then do the same for the children of the children
    for line in data:
        for child in line['children']:
            for grandchild in child['children']:
                grandchild['children'] = []
                for row in reader:
                    if(row['parent'] == grandchild['id']):
                        grandchild['children'].append(row)
                    else:
                        pass

    # Reset reader
    reader = list(csv.DictReader(open(source, 'r')))
    
    #then
    for line in data:
        for child in line['children']:
            for grandchild in child['children']:
                for greatgrandchild in grandchild['children']:
                    greatgrandchild['children'] = []
                    for row in reader:
                        if(row['parent'] == greatgrandchild['id']):
                            greatgrandchild['children'].append(row)
                        else:
                            pass

    #then write the new list to a json file
    with open(output, 'w') as f:
        json.dump(data, f)
                        
#foreach of lines in file output.csv create a nested list
#if the parent list is 0, then create a new list, add the current line to the list
#then for each line after the first, check if the parent is the same as the current line
#if so, add the current line to the new children key of the current line

