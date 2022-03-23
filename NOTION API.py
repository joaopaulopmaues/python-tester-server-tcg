# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import json
import requests
#import seaborn as sns
#from projects_vis import *
#from notion_api import *


DATABASE_ID = "6c654308bcbe4dc7845e3a3460ca35e0"
NOTION_URL = 'https://api.notion.com/v1/databases/'

class NotionSync:
    def __init__(self):
        pass    

    def query_databases(self,integration_token="secret_vn0ayz4FMRtpkYdhev94dZPBEAlgILFtDhMLmvSyXeS"):
        database_url = NOTION_URL + DATABASE_ID + "/query"
        response = requests.post(database_url, headers={"Authorization": f"{integration_token}","Notion-Version": "2021-05-13"})
        if response.status_code != 200:
            raise ApiError(f'Response Status: {response.status_code}')
        else:
            return response.json()
    
    def get_projects_titles(self,data_json):
        return list(data_json["results"][0]["properties"].keys())
    

    def get_projects_data(self,data_json,projects):
        projects_data = {}
        for p in projects:
            if p!="Name" and p !="Date":
                projects_data[p] = [data_json["results"][i]["properties"][p]["checkbox"]
                                    for i in range(len(data_json["results"]))]
            elif p=="Date":
                dates = [data_json["results"][i]["properties"]["Date"]["date"]["start"]
                                    for i in range(len(data_json["results"]))]

        
        return projects_data,dates
    
    def getName(self,):
        
    def getDesc():

nsync = NotionSync()
data = nsync.query_databases()
print(json.dumps(data,indent=4, sort_keys=True))

#projects = nsync.get_projects_titles(data)
#projects_data,dates = nsync.get_projects_data(data,projects)