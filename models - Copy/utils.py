

from distutils.command.config import config
import pandas as pd
import numpy as np
import pickle
import json

import config


class Medical():
    def __init__(self,age, sex, bmi, children, smoker, region):

       self.age = age
       self.sex = sex
       self.bmi = bmi
       self.children = children
       self.smoker = smoker
       self.region = "region_" + region

    def load_model(self):
        with open(config.MODEL_FILE_PATH,"rb")as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,"r")as f:
            self.data = json.load(f)

    def predicted_charges(self):

        self.load_model()

        region_index = self.data["column_name"].index(self.region)

        array = np.zeros(len(self.data["column_name"]))

        array[0] = self.age
        array[1] = self.data["sex_dict"][self.sex]
        array[2] = self.bmi
        array[3] = self.children
        array[4] = self.data["smoker_dict"][self.smoker]
        array[region_index] = 1

        predicted_charge = self.model.predict([array])[0]
        return np.around(predicted_charge,2)

if __name__ == "__main__":
    age = 19.0
    sex = "male"
    bmi = 27.9
    children = 0.0
    smoker = "no"

    region = "southwest"

    obj = Medical(age, sex, bmi, children, smoker, region)

    charge = obj.predicted_charges()
    print(f"Medical Charges Is {charge} /- Rs Only")






