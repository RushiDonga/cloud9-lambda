aws lambda create-function 
  --function-name testFunction 
  --runtime python3.9 
  --role arn:aws:iam::937726284102:role/lambda-basic-execution-role 
  --zip-file fileb:///home/ec2-user/environment/lambda/lambda.zip 
  --handler lambda_function.lambda_handler
