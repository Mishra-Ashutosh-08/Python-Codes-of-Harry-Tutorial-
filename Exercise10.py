# pickle
# use requests module to download the iris dataset

import requests
import pickle
data = requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text
l1 = data.split("\n")
l2 = [item.split(",") for item in l1 if len(item)!=0]
with open("myiris.pkl", "wb") as f:
    pickle.dump(l2, f)