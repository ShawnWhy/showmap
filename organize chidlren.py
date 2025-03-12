#read the csv file and create a nested list
import csv
import json
import copy
source = 'output.csv'
output = 'output.json'
data = []
level1 = []
level2 = []
level3 = []
level4 = []
level5 = [] 
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
        #give the line a rotation key and give it a degree value that is 360/15*index
        line['rotation'] = 360/15*data.index(line)
        line['children'] = []
        line['level']=1
        level1.append(copy.deepcopy(line))
        for row in reader:
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
            child['level']=2
            child['rotation'] = line['children'].index(child)*360/15*3
            level2.append(copy.deepcopy(child))

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
                grandchild['level']=3
                grandchild['rotation'] = child['children'].index(grandchild)*360/15*9
                level3.append(copy.deepcopy(grandchild))

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
                    greatgrandchild['level']=4
                    greatgrandchild['rotation'] = grandchild['children'].index(greatgrandchild)*360/15*27
                    print (greatgrandchild)
                    # push the temp state of greatgrandchild to level4
                    temp_state = copy.deepcopy(greatgrandchild)
                    level4.append(temp_state)
                    for row in reader:
                        if(row['parent'] == greatgrandchild['id']):
                            greatgrandchild['children'].append(row.copy())
                        else:
                            pass
     #level 5
    for line in data:
        for child in line['children']:
            for grandchild in child['children']:
                for greatgrandchild in grandchild['children']:
                    for greatgreatgrandchild in greatgrandchild['children']:
                        greatgreatgrandchild['children'] = []
                        greatgreatgrandchild['level']=5
                        greatgreatgrandchild['rotation'] = greatgrandchild['children'].index(greatgreatgrandchild)*360/15*81
                        print (greatgreatgrandchild)
                        # push the temp state of greatgrandchild to level4
                        temp_state = copy.deepcopy(greatgreatgrandchild)
                        level5.append(temp_state)
                        for row in reader:
                            if(row['parent'] == greatgreatgrandchild['id']):
                                greatgreatgrandchild['children'].append(row.copy())
                            else:
                                pass

    #then write the new list to a json file
    with open(output, 'w') as f:
        json.dump(data, f)
    with open('level1.json', 'w') as f:
        json.dump(level1, f)
    with open('level2.json', 'w') as f:
        json.dump(level2, f)
    with open('level3.json', 'w') as f:
        json.dump(level3, f)
    with open('level4.json', 'w') as f:
        json.dump(level4, f)
    with open('level5.json', 'w') as f:
        json.dump(level5, f)
    
#foreach of lines in file output.csv create a nested list
#if the parent list is 0, then create a new list, add the current line to the list
#then for each line after the first, check if the parent is the same as the current line
#if so, add the current line to the new children key of the current line

