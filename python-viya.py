import os
import swat
import pandas as pd
from matplotlib import pyplot as plt
%matplotlib inline

# optional* setup a requirments.txt with sas-deployment hostname and user credentials
# read txt file 
with open('requirements.txt', 'r') as f:
    user = f.readline().strip()
    host = f.readline().strip()

# use your sas userid 
os.environ['CAS_CLIENT_SSL_SA_LIST'] ='/C:/Users/user'
# authinfo contains ssl configuration and certs  
conn = swat.CAS('hostname',5570, authinfo ='C:/Users/mazlin/Anaconda3/authinfo.txt')

out = conn.serverstatus()
print(out)