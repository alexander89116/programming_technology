#!/bin/bash

cp ./config.ini ./PatternsCollection/Decorator/cpp-source/configs/
mkdir tmp
cd tmp

cmake ../PatternsCollection
make

cd ../bin
./Decorator
