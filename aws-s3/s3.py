import logging
import boto3
from botocore.exceptions import ClientError
s3 = boto3.client('s3')
res = s3.list_objects_v2(Bucket="kamalmin",Prefix="kamal")
file_respose = res.get("Contents")
file =[]
for fi in  file_respose:
  file.append(list(fi.values())[0])
for f in file:
  res = s3.get_object(Bucket="kamalmin",Key=str(f))
  print(res.get("Body").read())

