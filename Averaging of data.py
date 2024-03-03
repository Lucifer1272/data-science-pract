import pandas as pd
InputFileName='IP_DATA_CORE.csv'
OutputFileName='Retrieve_Router_Location.csv'
Base='D:/1_UPG_MSCIT_PART1/Data_Science_Practical/Practical_Files/'
print('========Farhaan Dodhia : 53004230003========')
print('Working Base:',Base,'using')
print('==================================')
sFileName = Base + InputFileName
print('Loading:',sFileName)
IP_DATA_ALL=pd.read_csv(sFileName,header=0,low_memory=False,usecols=['Country','Place Name','Latitude','Longitude'],encoding="latin-1")
IP_DATA_ALL.rename(columns={'Place Name':'Place_Name'},inplace=True)
AllData=IP_DATA_ALL[['Country','Place_Name','Latitude']]
print(AllData)
MeanData=AllData.groupby(['Country','Place_Name'])['Latitude'].mean()
print(MeanData)
