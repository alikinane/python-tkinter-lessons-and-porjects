# writing files in python .txt

# info = {
# 	'name':'ali',
# 	'age' : 19,
# 	'jop': 'entrepreneur',
# 	'statu': 'single'
# }
# file_path = 'C:\\Users\\nonoa\\OneDrive\\Desktop\\info.txt'
# with open(file_path,'w') as file :
# 	x = []
# 	for key , value in info.items():
# 		x.append(str(value))
# 	file.write('\n'.join(x))
# writing files in python .json
import json
info = {
	'name':'ali',
	'age' : 19,
	'jop': 'entrepreneur',
	'ismaried': False
}
file_path = 'C:\\Users\\nonoa\\OneDrive\\Desktop\\info.json'
with open(file_path , 'w') as file:
	json.dump(info,file,indent = 4)