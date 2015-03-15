#!/usr/bin/env bash

gfortran -o double-write.x double.F90
gfortran -o single-read.x single.F90

./double-write.x
python convert.py
./single-read.x
