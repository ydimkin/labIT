#!/bin/bash

mkdir ./LabWork

cd  LabWork

pwd

echo "Hello, World!" > example.txt

ls -alh

cat example.txt

cp example.txt copy_example.txt

ls -alh

mv copy_example.txt renamed_example.txt

ls -alh

rm -rf renamed_example.txt

ls -alh

rm -rf ../LabWork
