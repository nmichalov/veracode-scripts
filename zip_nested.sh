#!/bin/bash

if [ -d "upload_zips_temp" ]; then
  rm -rf upload_zips_temp
fi

mkdir upload_zips_temp

for DIR in $(ls); do
  if [ -d "${DIR}/lambda" ]; then
    zip -r "upload_zips_temp/${DIR}" "${DIR}/lambda"
  fi
done

rm -rf upload_zips_temp