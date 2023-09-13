import boto3
from botocore import UNSIGNED
from botocore.client import Config
B_name="coderbytechallengesandbox"
F_prefix="__cb__"
s3 = boto3.client('s3',config=Config(signature_version=UNSIGNED))
#get the file names object based on prefix 
res = s3.list_objects_v2(Bucket=B_name,Prefix=F_prefix)
file_respose = res.get("Contents")
file =[]
#file names adding to list from dictionary 
for fi in  file_respose:
  print(fi)
  print(str(fi["Key"]))
  #res = s3.get_object(Bucket=B_name,Key=str1)
 # print(res.get("Body").read().decode('utf-8'))
#read file condent from object "Body" 
'''for f in file:
  res = s3.get_object(Bucket=B_name,Key=str(f))
  print(res.get("Body").read().decode('utf-8'))

import boto3
from botocore import UNSIGNED
from botocore.client import Config
B_name="coderbytechallengesandbox"
F_prefix="__cb__"
s3 = boto3.client('s3',config=Config(signature_version=UNSIGNED))
res = s3.list_objects_v2(Bucket=B_name, Prefix=F_prefix)
file_respose = res.get("Contents")
if(file_respose):
  for fi in  file_respose:
    res = s3.get_object(Bucket=B_name,Key=str(fi["Key"]))
    print(res.get("Body").read().decode('utf-8'))
else:
  print("No object found") '''