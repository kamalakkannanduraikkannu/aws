#!/bin/bash
docker build -t hacker:1.0  aws-s3/.
docker run hacker:1.0
