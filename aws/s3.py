import logging
import boto3
from datetime import datetime
from botocore.exceptions import ClientError
def timenow():
      date = datetime.now()
      return str(date.minute)+"-"+str(date.second)
s3 = boto3.client('s3')
res = s3.list_objects_v2(Bucket="kamalmin",Prefix="kamal")
file_respose = res.get("Contents")
file =[]
for fi in  file_respose:
  print("file name:",fi["Key"]," Size: ",fi["Size"])
  res = s3.get_object(Bucket="kamalmin",Key=str(fi["Key"]))
  print(res.get("Body").read().decode("utf-8"))
 # wr = s3.put_object(Bucket="kamalmin",Key=str(f),Body="python: "+str(f)+"-"+timenow()) 
