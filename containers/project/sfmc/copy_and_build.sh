#!/bin/sh

cd ..
cp -r arch/* sfmc
cd sfmc
docker build -t copy_demo:v1 .
docker run copy_demo:v1
