# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 09:57:37 2022

@author: Ife.Olawore
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
import csv
import itertools

# This 
fPath = "C:\\Users\\bethany.kilpatrick\\Downloads\\"
fileExt = r".csv"
fName = 'data_management_BOA Technology_2022-07-29 15_33_54.csv'


dat = pd.read_csv(fPath + fName, delimiter =',', header = 0)
df = pd.DataFrame(dat)

# dat2 = pd.read_csv('C:\\Users\\ife.olawore\\Downloads\\MasterAetrex.csv',  delimiter =',', header = 0)
# main = pd.DataFrame(dat2)

# Function to normalize some of the given  metrics
def divide_ten(number):
    return number / 10

df[["Left Dorsal Height","Right Dorsal Height", "Left Arch Height",
"Right Arch Height",  "Left Girth", "Right Girth"]]= df[["Left Dorsal Height","Right Dorsal Height", "Left Arch Height",
"Right Arch Height", "Left Girth", "Right Girth"]] .apply(divide_ten)

                                                         
# Replacing values under some columns with the required 
df['Gender'] = df['Gender'].replace(['Male','Female'], ['M', 'F'])
df['Right Arch Type'] = df['Right Arch Type'].replace(['H','L','M','F'], ['High','Low','Medium', 'Flat'])
df['Left Arch Type'] = df['Left Arch Type'].replace(['H','L','M','F'], ['High','Low','Medium', 'Flat'])

# extracting the date from date-time and duplicating
date = df['Date'].str.split("T",1,expand = True)[:][0]
date = pd.DataFrame([date[value//2] for value in range(len(date)*2)])
date.columns = ['Date']

#duplicating some coulumn values
sex = df['Gender'].iloc[df.index.repeat(2)].reset_index()
size = df['Size'].iloc[df.index.repeat(2)].reset_index(drop=True)

# inserting replications of the side
df.insert(4, 'Left', 'L')
df.insert(5, 'Right', 'R')
side = df[['Left','Right']].stack().reset_index(drop=True).to_frame('Side')

# extracting the name from email and duplicating
subject = (df['Email'].str.split("@",1,expand = True)[:][0])
subject = pd.DataFrame([subject[values//2] for values in range(len(subject)*2)])

subject = subject.replace('dan.feeney', 'Dan Feeney') # Change individual names from username to real name

subject.columns = ['Subject']

# separating internal from external
placement = (df['Email'].str.split("@",1,expand = True)[:][1])
placement = pd.DataFrame([placement[values//2] for values in range(len(placement)*2)])
placement = placement.replace('boatechnology.com', 'Internal')
placement.columns = ['Internal or External']
placement[placement != 'Internal'] = 'External'


# Transposing left and right values for each subject
archtype = df[['Left Arch Type','Right Arch Type']].stack().reset_index(drop=True).to_frame('ArchType')
length = df[['Left Length','Right Length']].stack().reset_index(drop=True).to_frame('Length (cm)')
width = df[["Left Width","Right Width"]].stack().reset_index(drop=True).to_frame('Width (cm)')
instep = df[["Left Dorsal Height","Right Dorsal Height"]].stack().reset_index(drop=True).to_frame('Instep (cm)')
archht = df[["Left Arch Height", "Right Arch Height"]].stack().reset_index(drop=True).to_frame('ArchHt (cm)')
girth = df[["Left Girth", "Right Girth"]].stack().reset_index(drop=True).to_frame('Girth (cm)')
totalarea = df[["Left Total Area", "Right Total Area"]].stack().reset_index(drop=True).to_frame('TotalArea (cm**2)')
archdepth = df[["Left Arch Depth", "Right Arch Depth"]].stack().reset_index(drop=True).to_frame('ArchDepth (.5cm)')

# compute width_length
width_length = []
for val1 in range(0, len(length.index)):
    for val2 in range(0, len(length.columns)):
       width_length.append(width.values[val1,val2]/length.values[val1, val2])
width_length = pd.DataFrame(width_length)
width_length.columns = ['Width_Length (cm)']

# merging the columns to produce final output
merge  = [date,placement,subject,sex,side,archtype,length,width,instep,archht,girth,totalarea,archdepth,size,width_length]
data = pd.concat(merge,axis = 1)
data.set_index('index',inplace = True)

##########################################################

# Function under processing
#  Function should replace names of the subject on the new sheet with the names on the master file

# master_old =  pd.DataFrame(main['Length (cm)'].astype(str) + '_' + main['Width (cm)'].astype(str) + '_' + main['Instep (cm)'].astype(str) + '_' + main['ArchHt (cm)'].astype(str)  + '_' + main['Girth(cm)'].astype(str) + '_' + main['ArchDepth (.5cm)( Proximal POV)'].astype(str) + '_' + main['Shoe Sizes (Aetrex)'].astype(str))
# master_old.columns = ['master_old']                 
# master_new =  pd.DataFrame(data['Length (cm)'].astype(str) + '_' + data['Width (cm)'].astype(str) + '_' + data['Instep (cm)'].astype(str) + '_' + data['ArchHt (cm)'].astype(str)  + '_' + data['Girth (cm)'].astype(str) + '_' + data['ArchDepth (.5cm)'].astype(str) + '_' + data['Size'].astype(str))
# master_new.columns = ['master_new']
# aa = pd.concat([data['Subject'], master_new], axis = 1)
# bb = pd.concat([main['Subject'], master_old], axis = 1)
# aa = aa.reset_index(drop = True)


# aa['check']  = np.where(aa['master_new'] == bb['master_old'], True , False)
# for datas in aa['Subject']:
#     for mains in bb['Subject']:
#         for xx in aa['master_new']:
#             for yy in bb['master_old']:
#                 if xx == yy:
#                     datas.replace(datas, mains)
                # else: 
                #     aa['Subject']
# for values in data:
#     if data['Size'] <= 5: 
#         values.delete()

############################################################

data = data[data['Size'] > 5] # Drops subjects with sizes less than 5 i.e children


# data = data.groupby('Subject').head(2).reset_index(drop = True) 
#function to drop duplicate values: Please note that this will also filter out the 'index' row hence skipping that number 

data.to_csv('C:\\Users\\bethany.kilpatrick\\Downloads\\NewMasterwalk_aetrex.csv', index=True)
# Open file
file = open('C:\\Users\\bethany.kilpatrick\\Downloads\\NewMasterwalk_aetrex.csv')
csvreader = csv.reader(file)

