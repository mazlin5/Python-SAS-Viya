# Python program to explain os.environ object

#import os module 
import os 
import pprint 
import platform
import saspy
import sas_kernel

# get list of user's 
# environment variables 
env_var = os.environ 

#print the list of user's 
# environment vars
print("Users env vars:")
pprint.pprint(dict(env_var), width = 1)


# below script will display available modules within your CAS session
# helpful when you want to use SAS SDK APIs for GET/POST requests
print(platform.sys.version)
help('modules')