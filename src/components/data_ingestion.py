import os
import sys
import pandas as pd
import numpy as np 
from src.logger import logging
from src.exception import CustomException
from sklearn.model_selection import train_test_split




class DataIngestionConfig:
    train_path=os.path.join("artifact","train.csv")
    test_path=os.path.join("artifact","test.csv")
    raw_path=os.path.join("artifact","raw.csv")

class DataIngestion:
    def __init__(self) -> None:
        self.config=DataIngestionConfig()

    def start_ingestion(self):

        try:

            logging.info("ingestion started")
            data=pd.read_csv("https://raw.githubusercontent.com/iamRahulB/small-dataset-for-testing-/main/Mental%20Health.csv")

            os.makedirs(os.path.dirname(self.config.raw_path),exist_ok=True)

            data.to_csv(self.config.raw_path, index=False, header=True)

            train, test= train_test_split(data, test_size=0.2,random_state=42)


            os.makedirs(os.path.dirname(self.config.train_path),exist_ok=True)
            train.to_csv(self.config.train_path)

            os.makedirs(os.path.dirname(self.config.test_path),exist_ok=True)
            test.to_csv(self.config.test_path)
            logging.info("ingestion done")

            1/0






        except Exception as e:
            raise CustomException(e,sys)

    

if __name__=="__main__":
    obj=DataIngestion()
    obj.start_ingestion()