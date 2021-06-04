""" This file is to be used to test 
helper functions via assertations statements """

import pandas as pd
import numpy as np
from faker import Faker 
from lambdata.helper_functions import Null_Count, Add_Series

#Must import pytest or the test can not be ran
import pytest 

#For pytest to work, the methods must start with test
def test_null_count():
    
    #The df must be included in the function or pytest can't read it
    df = pd.read_csv(
        "https://raw.githubusercontent.com/iknight7000/lambdata-knight/main/Hospitals.csv")
    
    #instantiate the class
    test_null = Null_Count(df)
    assert test_null.clean_data() == 7567

