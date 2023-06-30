"""Hops flask middleware example"""

from flask import Flask
import ghhops_server as hs
import rhino3dm
import requests
import base64
import json
"""
import matplotlib.pyplot as plt
import seaborn as sns; sns.set() # for plot styling
from flask_ngrok import run_with_ngrok
"""
import numpy

import math
import random

"""
# register hops app as middleware
app = Flask(__name__)
hops: hs.HopsFlask = hs.Hops(app)
"""

# flask app can be used for other stuff drectly
@app.route("/help")
def help():
    return "Welcome to Grashopper Hops for CPython!"
"""
from sklearn.datasets import make_blobs
X, y_true = make_blobs(n_samples=50, centers=4, cluster_std=0.60, random_state=0)
plt.scatter(X[:, 0], X[:, 1], s=50);

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run
hops = hs.Hops(app)
"""

@hops.component(
    "/test",
    name="test",
    description="test",
    inputs=[
        hs.HopsString("name", "name", "name")
    ],
    outputs=[
        hs.HopsString("name", "name", "name")
    ]
)
def test(name):
    s = "Hello " + name
    return s


def convertNumpyToPoint(numpyArray):
    points = []
    for i in range(len(numpyArray)):
        points.append(rhino3dm.Point3d(numpyArray[i][0], numpyArray[i][1], 0))
    return points



#write into a @hops component
@hops.component(
    "/convertNumpyToPoint",
    name="convertNumpyToPoint",
    description="convertNumpyToPoint",
    inputs=[
        hs.HopsString("numpyArray", "numpyArray", "numpyArray")
    ],
    outputs=[
        hs.HopsPoint("points", "points", "points")
    ]
)
def convertNumpyToPoint(numpyArray):
    points = []
    for i in range(len(numpyArray)):
        points.append(rhino3dm.Point3d(numpyArray[i][0], numpyArray[i][1], 0))
    return points

@hops.component(a
    "/getPoints",
    name="getPoints",
    description="getPoints",
    inputs=[
        hs.HopsString("numpyArray", "numpyArray", "numpyArray")
    ],
    outputs=[
        hs.HopsPoint("points", "points", "points", access=hs.HopsParamAccess.LIST)
    ]
)
def getPoints(numpyArray):
    points = []
    for i in range(len(numpyArray)):
        points.append(rhino3dm.Point3d(numpyArray[i][0], numpyArray[i][1], 0))
    return points

if __name__ == "__main__":
    app.run(debug=True)

