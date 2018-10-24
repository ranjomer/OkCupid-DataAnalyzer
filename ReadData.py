import numpy as np
import pandas as pd
import re

fields = pd.DataFrame( data = [['age', 'age'],['diet','diet'],['drugs','drugs'],['essay0','about_me'],['sex','sex'],['speaks','languagues'],['status','status']], columns = ['csvfields', 'columns'])

def cleanupstring(string):
    rgxclean = re.compile('<[^>]*>')
    rgxclnstr = re.sub(rgxclean, ' ', string)
    return (rgxclnstr.replace('\n', ' ').replace(',', ' ').replace('.', ' ').replace(':', ' ').replace('<a', ' ').replace('nan', ''))

def readData():
    return pd.read_csv('profiles.csv',usecols = fields['csvfields']) #names = fields['fields'] can't be used together with usecols for some reason
    
def prepareData(profiles):
    profiles.drop_duplicates() 
    profiles.columns = fields['columns'] 
    profiles.about_me = profiles.about_me.astype(str)
    profiles['about_me'] = profiles['about_me'].map(cleanupstring)
    profiles['about_me_length'] = profiles['about_me'].map(lambda x: len(re.findall("[a-zA-Z_]+", x)))
def getData():
    profiles = readData()
    prepareData(profiles)
    return profiles