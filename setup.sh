#!/bin/bash

zip -r function.zip ./lambda_src

aws --endpoint-url=http://localhost:4566 \
lambda create-function --function-name lambda-hello-world \
--zip-file fileb://function.zip \
--handler index.handler --runtime python3.9.x \
--role arn:aws:iam::000000000000:role/lambda-role 