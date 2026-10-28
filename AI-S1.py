import pandas as pd

df = pd.read_csv('test_data.csv') #connects the csv file, defined to the code as df
for index, row in df.iterrows():
    RiskScore = 100
    if row["Housing"] == "own":
        RiskScore = RiskScore*1.125984252
    elif row["Housing"] == "rent":
        RiskScore = RiskScore*0.7610619469
    elif row["Housing"] == "free":
        RiskScore = RiskScore*0.6818181818
    else:
        print("Error at Housing")
    
    if row["Job"] == 0:
        RiskScore = RiskScore*1.2
    elif row["Job"] == 1:
        RiskScore = RiskScore*1.042016807
    elif row["Job"] == 2:
        RiskScore = RiskScore*0.9912536443
    elif row["Job"] == 3:
        RiskScore = RiskScore*0.9545454545
    else:
        print("Error at Job")

    if row["Sex"] == "male":
        RiskScore = RiskScore*1.061497326
    elif row["Sex"] == "female":
        RiskScore = RiskScore*0.876344086
    else:
        print("Error at Gender")
    
    if row["Age"] <=20 :
        RiskScore = RiskScore*0.9411764706
    elif row["Age"] <=30:
        RiskScore = RiskScore*0.8533916849
    elif row["Age"] <=40:
        RiskScore = RiskScore*1.10787172
    elif row["Age"] <=50:
        RiskScore = RiskScore*1.147727273
    elif row["Age"] <=60:
        RiskScore = RiskScore*0.925
    elif row["Age"] <=70:
        RiskScore = RiskScore*1.2
    elif row["Age"] >70:
        RiskScore = RiskScore*1.428571429
    else:
        print("Error at age")
    
    if row["Purpose"] == "repairs" :
        RiskScore = RiskScore*0.9411764706
    elif row["Purpose"] == "education":
        RiskScore = RiskScore*0.8533916849
    elif row["Purpose"] == "car":
        RiskScore = RiskScore*1.10787172
    elif row["Purpose"] == "furniture/equipment":
        RiskScore = RiskScore*1.147727273
    elif row["Purpose"] == "radio/TV":
        RiskScore = RiskScore*0.925
    elif row["Purpose"] == "business":
        RiskScore = RiskScore*1.2
    elif row["Purpose"] == "vacation/others":
        RiskScore = RiskScore*1.428571429
    elif row["Purpose"] == "domestic appliances":
        RiskScore = RiskScore*1.428571429
    else:
        print("Error at purpose")

    if row["Saving accounts"] == "little" :
        RiskScore = RiskScore*0.8603351955
    elif row["Saving accounts"] == "moderate":
        RiskScore = RiskScore*1.00990099
    elif row["Saving accounts"] == "rich":
        RiskScore = RiskScore*1.222222222
    elif row["Saving accounts"] == "quite rich":
        RiskScore = RiskScore*1.5
    elif pd.isna(row["Saving accounts"]):
        RiskScore = RiskScore*1.301587302
    else:
        print("Error at Saving accounts")

    if row["Checking account"] == "little" :
            RiskScore = RiskScore*0.5941644562
    elif row["Checking account"] == "moderate":
        RiskScore = RiskScore*0.8417721519
    elif row["Checking account"] == "rich":
        RiskScore = RiskScore*1.147058824
    elif pd.isna(row["Checking account"]):
        RiskScore = RiskScore*1.537604457
    else:
        print("Error at Checking accounts")

    if row["Credit amount"] <=1369.25 :#lower quartile
        RiskScore = RiskScore*0.9411764706
    elif row["Credit amount"] >=4241: #upper quartile
        RiskScore = RiskScore*0.8533916849
    elif row["Credit amount"] <4241 and row["Credit amount"] >1369.25: #within quartile range
        RiskScore = RiskScore*1.10787172
    else:
        print("Error at Credit amount")

    if row["Duration"] <= 6 :
        RiskScore = RiskScore*1.525
    elif row["Duration"] <=12:
        RiskScore = RiskScore*1.231884058
    elif row["Duration"] <=24:
        RiskScore = RiskScore*0.9748953975
    elif row["Duration"] <=36:
        RiskScore = RiskScore*0.7558139535
    elif row["Duration"] >36:
        RiskScore = RiskScore*0.5438596491
    else:
        print("Error at Duration amount")

    if RiskScore >=101.875279:
        df.loc[index,"CalcRisk"] = "good"
    elif RiskScore < 101.875279:
        df.loc[index,"CalcRisk"] = "bad"
df.to_csv('data.csv', index=False)