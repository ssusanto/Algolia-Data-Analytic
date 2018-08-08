# -*- coding: utf-8 -*-
from datetime import date, timedelta
import requests, csv, http.client as client

def algolia_analytic():
    while True:
        request = input("Please enter either top-search, #search, no-result,details or STOP: ")
        
                        
        #API config from Algolia
        #Note: This is a private API key. Please keep it secret and use it ONLY from your backend
        api = {'X-Algolia-API-Key': 'Insert API Key here','X-Algolia-Application-Id': 'Insert App ID here'}
        

        now = date.today().strftime('%Y-%m-%d')
        
        #Condition to break the loop and end the program
        if request.lower() == "stop":
            break
        
    
        if request == "top-search":
            startDate = input("Please input the start date (yyyy-mm-dd): ")
            endDate = input("Please input the end date (yyyy-mm-dd): ")  
            
            #Handle invalid date
            if startDate > now or endDate > now:
                print("One of your date is invalid, please try again")
                print()
                algolia_analytic()
            
            
            url = "https://analytics.algolia.com/2/searches?index=dev_catalog&startDate={0}&endDate={1}"
            
            curl = url.format(startDate,endDate)
            
            res = requests.get(curl, params = api)
            
            dic = res.json()
            
            output_lst = []
            
            try:
                for item in dic.values():
                    for values in item:
                        output_lst.append(values)
                        print(values)
                
                #Create CSV
                with open('data.csv', 'w') as csvfile:
                    fieldnames = ['search', 'count', 'nbHits']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                     
                    writer.writeheader()
                    writer.writerows(output_lst)
                        
            except:
                print()
                print("Null")
                print("The Index were not build or has no data yet within that time frame")
                    
        elif request == "#search":
            startDate = input("Please input the start date (yyyy-mm-dd): ")
            endDate = input("Please input the end date (yyyy-mm-dd): ")  
            
            #Handle invalid date
            if startDate > now or endDate > now:
                print("One of your date is invalid, please try again")
                print()
                algolia_analytic()
                
            url = "https://analytics.algolia.com/2/searches/count?index=dev_catalog&startDate={0}&endDate={1}"
            
            curl = url.format(startDate,endDate)
            
            res = requests.get(curl, params = api)
            
            dic = res.json()
            
            #index[0] returns the total #search within the time period
            #index[1] returns a dictionary that has date as the key and count as value
            lst = []
            
            output_lst = []
            
            for item in dic.values():
                lst.append(item)
                
            try:
                for item in lst[1]:
                    print(item)
                    output_lst.append(item)
                    
            #Create CSV
                with open('data.csv', 'w') as csvfile:
                    fieldnames = ['date', 'count']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                     
                    writer.writeheader()
                    writer.writerows(output_lst)
                    
            except:
                print()
                print("Null")
                print("The Index were not build or has no data yet within that time frame")
    
        elif request == "no-result":
            startDate = input("Please input the start date (yyyy-mm-dd): ")
            endDate = input("Please input the end date (yyyy-mm-dd): ")  
            
            #Handle invalid date
            if startDate > now or endDate > now:
                print("One of your date is invalid, please try again")
                print()
                algolia_analytic()
                
            url = "https://analytics.algolia.com/2/searches/noResults?index=dev_catalog&startDate={0}&endDate={1}"
            
            curl = url.format(startDate,endDate)
            
            res = requests.get(curl, params = api)
            
            dic = res.json()
            
            output_lst = []
            
            try:
                for values in dic.values():
                    for item in values:
                        print(item)
                        output_lst.append(item)
            #Create CSV
                with open('data.csv', 'w') as csvfile:
                    fieldnames = ['search', 'count', 'withFilterCount']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                     
                    writer.writeheader()
                    writer.writerows(output_lst)
                
            except:
                print()
                print("Null")
                print("The Index were not build or has no data yet within that time frame")
            
        elif request == "details":
            print()
            print("Enter top-search to display the top searches from dev_catalog")
            print("Enter #search to count the number of searches within the time period")
            print("Enter no-result to display the number of searches for a specific item that displays no result")
            
        else:
            print("Your input does not match with any of the function. Please try again")
        
#main
algolia_analytic()
        
    
    

    

    

    

