import boto3
from botocore import UNSIGNED
from botocore.client import Config
B_name="coderbytechallengesandbox"
F_prefix="__cb__"
s3 = boto3.client('s3',config=Config(signature_version=UNSIGNED))
// get the file names object based on prefix 
res = s3.list_objects_v2(Bucket=B_name,Prefix=F_prefix)
file_respose = res.get("Contents")
file =[]
// file names adding to list from dictionary 
for fi in  file_respose:
  file.append(list(fi.values())[0])
// read file condent from object "Body" 
for f in file:
  res = s3.get_object(Bucket=B_name,Key=str(f))
  print(res.get("Body").read())