import pandas as pd

df = pd.read_csv('./data/compas-scores-raw.csv')

df = df.drop('Person_ID', axis=1)
df = df.drop('AssessmentID', axis=1)
df = df.drop('Case_ID', axis=1)
df = df.drop('Agency_Text', axis=1)
df = df.drop('LastName', axis=1)
df = df.drop('FirstName', axis=1)
df = df.drop('MiddleName', axis=1)
df = df.drop('ScaleSet_ID', axis=1)
df = df.drop('ScaleSet', axis=1)
df = df.drop('AssessmentReason', axis=1)
df = df.drop('Screening_Date', axis=1)
df = df.drop('AssessmentType', axis=1)
df = df.drop('RecSupervisionLevel', axis=1)
df = df.drop('RecSupervisionLevelText', axis=1)
df = df.drop('Scale_ID', axis=1)
df = df.drop('DisplayText', axis=1)
df = df.drop('RawScore', axis=1)
df = df.drop('IsCompleted', axis=1)
df = df.drop('IsDeleted', axis=1)
df = df.drop('ScoreText', axis=1)

sex = pd.get_dummies(df['Sex_Code_Text'])
df = pd.concat([df, sex], axis=1)
df = df.drop('Sex_Code_Text', axis=1)
df = df.drop('Female', axis=1)

sex = pd.get_dummies(df['Ethnic_Code_Text'])
df = pd.concat([df, sex], axis=1)
df = df.drop('Ethnic_Code_Text', axis=1)

lang = pd.get_dummies(df['Language'])
df = pd.concat([df,lang], axis=1)
df = df.drop('Language', axis=1)

legal = pd.get_dummies(df['LegalStatus'])
df = pd.concat([df,legal], axis=1)
df = df.drop('LegalStatus', axis=1)

custody = pd.get_dummies(df['CustodyStatus'])
df = pd.concat([df,custody], axis=1)
df = df.drop('CustodyStatus', axis=1)

marital = pd.get_dummies(df['MaritalStatus'])
df = pd.concat([df,marital], axis=1)
df = df.drop('MaritalStatus', axis=1)

df['age'] = 122 - df['DateOfBirth'].str[-2:].astype(int)
df = df.drop('DateOfBirth', axis=1)

df.to_csv('data/clean_data.csv', encoding='utf-8', index=False)