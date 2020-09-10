from pathlib import Path
import json


class JsonFileWriter:
	def __init__(self,file_name):
		self.__file_path_str=file_name
	
	
	def write(self,byte_data,duns,prod):
		json_data = byte_data.decode('utf8').replace("'", '"')
		dict_data=json.loads(byte_data)
		flag=True
		for key in dict_data:
			if key=="error":
				flag=False
				break;
		if(flag):
			print("DUNS: "+duns+"  Product: "+prod+"  Status: Success")
			file_path = Path(self.__file_path_str)
			if file_path.is_file():
				file = open(self.__file_path_str,"a") 
				file.write(",\n"+json_data)
			else:
				file = open(self.__file_path_str,"a+") 
				file.write("[ \n"+json_data) 
			file.close()
			filePath=self.__file_path_str
			return filePath
		else:
			print("DUNS: "+duns+"  Product: "+prod+"  Status: Fail  MSG: "+dict_data["error"]["errorMessage"])
			return None
			
			
