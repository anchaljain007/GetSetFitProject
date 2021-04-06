import matplotlib.pyplot as plt
import numpy as np
import random


class ModelPredictor:
    def ml_search(image_path):
        model = " I am model"
        labels = ["bread", "chai", "egg_boiled", "egg_omlet", "rice", "roti", "yellow_dal"]

        return labels[random.randint(0, 7)]


# try:
#     mk =ModelPredictor.ml_search(image_path="/home/vaibhav/Documents/hack_the_mountains/data/test/rice/45.jpg")
#     print("++", mk, "++")

# except:
#     print(Exception)
