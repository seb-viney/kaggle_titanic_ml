import os
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


#  Folder and Files path locations
data_foder = r'G:\GitHub\work_development\kaggle\kaggle_titanic_ml\data'
train_csv = data_foder + r'\train.csv'
test_csv = data_foder + r'\test.csv'

#  Data Frames
train_df = pd.read_csv(train_csv)
test_df = pd.read_csv(test_csv, 
    usecols=['PassengerId', 
        'Pclass',
        'Name',
        'Sex',
        'Age',
        'SibSp',
        'Parch',
        'Ticket',
        'Fare',
        'Cabin',
        'Embarked'],
    dtype={'PassengerId': str,
        'Pclass': str,
        'Name': str,
        'Sex': str,
        'Age': str,
        'SibSp': str,
        'Parch': str,
        'Ticket': str,
        'Fare': str,
        'Cabin': str,
        'Embarked': str}
    )
                                            
print("testing")