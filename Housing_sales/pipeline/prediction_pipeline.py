import os
import sys

import numpy as np
import pandas as pd
from Housing_sales.entity.config_entity import loanPredictorConfig
from Housing_sales.entity.s3_estimator import bankEstimator
from Housing_sales.exception import bankexception
from Housing_sales.logger import logging
from Housing_sales.utils.main_utils import read_yaml_file
from pandas import DataFrame


class bank_loan:
    def __init__(self,
                age,
                balance,
                contact,
                duration,
                housing,
                job,
                month,
                pdays,
                poutcome,
                previous
                ):
        """
        bank Data constructor
        Input: all features of the trained model for prediction
        """
        try:
            
            self.age = age
            self.balance = balance
            self.contact = contact
            self.duration = duration
            self.housing = housing
            self.job = job
            self.month = month
            self.pdays = pdays
            self.poutcome = poutcome
            self.previous = previous


        except Exception as e:
            raise bankexception(e, sys) from e

    def get_usvisa_input_data_frame(self)-> DataFrame:
        """
        This function returns a DataFrame from USvisaData class input
        """
        try:
            
            bank_input_dict = self.get_usvisa_data_as_dict()
            return DataFrame(bank_input_dict)
        
        except Exception as e:
            raise bankexception(e, sys) from e


    def get_usvisa_data_as_dict(self):
        """
        This function returns a dictionary from USvisaData class input 
        """
        logging.info("Entered get_usvisa_data_as_dict method as USvisaData class")

        try:
            input_data = {
               "age": [self.age],
               "balance": [self.balance],
               "contact": [self.contact],
               "duration": [self.duration],
               "housing": [self.housing],
               "job": [self.job],
               "month": [self.month],
               "pdays": [self.pdays],
               "poutcome": [self.poutcome],
               "previous": [self.previous],
            }

            logging.info("Created bank data dict")

            logging.info("Exited get_bank_data_as_dict method as bankData class")

            return input_data

        except Exception as e:
            raise bankexception(e, sys) from e

class bankClassifier:
    def __init__(self,prediction_pipeline_config: loanPredictorConfig = loanPredictorConfig(),) -> None:
        """
        :param prediction_pipeline_config: Configuration for prediction the value
        """
        try:
            # self.schema_config = read_yaml_file(SCHEMA_FILE_PATH)
            self.prediction_pipeline_config = prediction_pipeline_config
        except Exception as e:
            raise bankexception(e, sys)

    def predict(self, dataframe) -> str:
        """
        This is the method of USvisaClassifier
        Returns: Prediction in string format
        """
        try:
            logging.info("Entered predict method of USvisaClassifier class")
            model = bankEstimator(
                bucket_name=self.prediction_pipeline_config.model_bucket_name,
                model_path=self.prediction_pipeline_config.model_file_path,
            )
            result =  model.predict(dataframe)
            
            return result
        
        except Exception as e:
            raise bankexception(e, sys)