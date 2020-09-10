import pandas as pd
import time
import os
import random
import DataConnection as DC;
import SearchCriteria as SC;
import JsonFileWriter as JFW;
import Credentials as CD;
 
def fileCloser(path_list):
	for path in path_list:
		file = open(path,"a") 
		file.write("\n]")
		
def main():
	data_df=pd.read_csv("companies_list.csv")
	cred=CD.Credentials()
	accessToken=cred.getAccessToken()
	counter=1
	row_count=0
	searchCriteria=SC.SearchCriteria(accessToken)
	dataConnection=DC.DataConnection(accessToken)
	folderName=str(time.strftime("%d%m%Y_%H%M%S"))
	os.makedirs(folderName)
	print("Data is being stored in the "+folderName+" folder")
	path_list=[]
	
	for index, row in data_df.iterrows():
		if counter+71<=1000:
			timer=random.randrange(5,60,1)
			duns_list=searchCriteria.getDunsNumber(row["searchTerm"],row["countryCode"])
			counter+=1
			#time.sleep(timer)
			
			for duns in duns_list:
			
				api_retrived_data = dataConnection.AASMCU(duns)
				counter+=1
				#time.sleep(timer)
				path=JFW.JsonFileWriter(folderName+"/AASMCU.txt").write(api_retrived_data, duns, "AASMCU")
				if path not in path_list:
					if path is not None:
						path_list.append(path)
				
				api_retrived_data = dataConnection.AASDHQ(duns)
				counter+=1
				#time.sleep(timer)
				path=JFW.JsonFileWriter(folderName+"/AASDHQ.txt").write(api_retrived_data, duns, "AASDHQ")
				if path not in path_list:
					if path is not None:
						path_list.append(path)
						
				api_retrived_data = dataConnection.LNKALT(duns)
				counter+=1
				#time.sleep(timer)
				path=JFW.JsonFileWriter(folderName+"/LNKALT.txt").write(api_retrived_data, duns, "LNKALT")
				if path not in path_list:
					if path is not None:
						path_list.append(path)
						
				api_retrived_data = dataConnection.LNKUPD(duns)
				counter+=1
				#time.sleep(timer)
				path=JFW.JsonFileWriter(folderName+"/LNKUPD.txt").write(api_retrived_data, duns, "LNKUPD")
				if path not in path_list:
					if path is not None:
						path_list.append(path)
						
				api_retrived_data = dataConnection.CMPELK(duns)
				counter+=1
				#time.sleep(timer)
				path=JFW.JsonFileWriter(folderName+"/CMPELK.txt").write(api_retrived_data, duns, "CMPELK")
				if path not in path_list:
					if path is not None:
						path_list.append(path)
					
				if row["countryCode"]=="US":
					api_retrived_data = dataConnection.AASBIG(duns)
					counter+=1
					#time.sleep(timer)
					path=JFW.JsonFileWriter(folderName+"/AASBIG.txt").write(api_retrived_data, duns, "AASBIG")
					if path not in path_list:
						if path is not None:
							path_list.append(path)
							
					api_retrived_data = dataConnection.LNKMIN(duns)
					counter+=1
					#time.sleep(timer)
					path=JFW.JsonFileWriter(folderName+"/LNKMIN.txt").write(api_retrived_data, duns, "LNKMIN")
					if path not in path_list:
						if path is not None:
							path_list.append(path)	

			row_count=row_count+1
			
			
	fileCloser(path_list)
	data_df[0:row_count].to_csv("completed_list.csv")
	data_df[row_count:].to_csv("companies_list.csv")

	
if __name__=="__main__":
    print("Start")
    main()
    print("END")