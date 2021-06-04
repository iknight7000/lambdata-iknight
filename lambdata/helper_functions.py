""" These helper functions will be used to count 
the total null values and turn lists into columns """

import pandas as pd
import numpy as np
from faker import Faker 

#Assign the method Faker to fake
fake = Faker()
#Import the df for testing purposes 
df = pd.read_csv(
    "https://raw.githubusercontent.com/iknight7000/lambdata-knight/main/Hospitals.csv")

#Create a blank list for the generated addresses
new_addresses = []
""" Create a foor loop that generates 10 
fake addreses and adds them to the new_addresses list """

for _ in range(10):
    new_addresses.append(fake.address())

#Create Null_count class that counts null values
class Null_Count:
    
    """A Null Count class with methods and attributes"""
    # Constructors are used to instantiate an object of the class.
    # The __init__ *keyword* is a method that defines the objects.
    # self arguments reference the instance of the class to interact with itself
    # df is the argument that has to be passed in to the object
    
    def __init__(self,df):
        """This is a constructor method"""
        self.df = df
        # attributes
        #This is the creation of the attribute
        #We are defining the attribute here
        
    """create a method that identifies 
    all null values"""
    def clean_data(self):
        return df.isnull().sum().sum()

# Create a class that turns list to columns
class Add_Series:
    def __init__(self,df):
        self.df = df 
    
    """Create a method that takes 
    list and df as arguments"""
    def list_to_series(list,df):
        df[""] = pd.Series(list)
