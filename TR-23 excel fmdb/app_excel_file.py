import pymongo
from pymongo import MongoClient
import pandas as pd
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["excel_db"]
mycol = mydb["excel_data"]


def InsertData(path=None):

    data = pd.read_excel(path)
    data_json = json.loads(data.to_json(orient='records'))
    abc = data_json
    mycol.insert_many(data_json)

    print("All the Data inserted in Mongo DB Server .... ")

if __name__ == "__main__":
    InsertData(path="task_S.xlsx")


