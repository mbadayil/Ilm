import requests
     ...: response = requests.get('http://api.bart.gov/api/etd.aspx?cmd=etd&orig=MONT&key=ZPBV-5PUE-9ZIT-DWE9&json=y') #Getting response from API
     ...: train_info=response.json() #storing response in json format 
     ...:  # Once the response of API stored in json format user can start filtering out based on the json format response. 
     ...:  # Since most of the informations have been stored under 'root' filter will start from  train_info['root']
     ...:  # A for loop will be running to iterate through destinations. Another variable will be checking with in for loop 
     ...:  # to make sure user doesnt print more than 10 train informations. 
     ...: 
     ...: train_count=1 #Variable to count number of trains
     ...: 
     ...: train_info['root']['station'][0]['etd'][0]['destination'] #after going through json response, based on the filtering this is the filter 
     ...: # which will list all destinations. [0] is the index hardcoded in this example, however this will be dynamically updated in the for loop.
     ...: # For loop will be iterating through the length of the destinations. 
     ...: 
     ...: train_info['root']['station'][0]['etd'][0]['estimate'][0]['minutes'] # #after going through json response, 
     ...:  # based on the filtering this is the filter  which will list minutes remaining for trains to leave.. [0] is the index hardcoded in this example, 
     ...:  # however this will be dynamically updated in the for loop.
     ...: 
     ...: for dest in range(len(train_info['root']['station'][0]['etd'])): #This is the for loop that is iterating through entire desinations
     ...:     if train_count<=10: #making sure user is not priting more than 10 train informations. 
     ...:         print("Train to {} will be leaving  in ***** {} minutes *****".format(train_info['root']['station'][0]['etd'][dest]['destination'], train_info['root']['station'][0]['etd'][dest]['estimate'][0]['minutes']))
     ...:         # Printing each train information 
     ...:     train_count+=1 #Incrementing and counting the number of printed trains information.