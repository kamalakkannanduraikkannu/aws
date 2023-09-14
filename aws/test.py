import boto3
from botocore import UNSIGNED
from botocore.client import Config
B_name="coderbytechallengesandbox"
F_prefix="__cb__"
s3 = boto3.client('s3',config=Config(signature_version=UNSIGNED))
res = s3.list_objects_v2(Bucket=B_name,Prefix=F_prefix)
file_respose = res.get("Contents")
file =[]
for fi in  file_respose:
  res = s3.get_object(Bucket=B_name,Key=fi["Key"])
  print(res.get("Body").read())