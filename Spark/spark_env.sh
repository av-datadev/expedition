#!/bin/bash

# Use your Anaconda Python path (confirm with `which python` if unsure)
export PYSPARK_PYTHON=/opt/anaconda3/bin/python
export PYSPARK_DRIVER_PYTHON=/opt/anaconda3/bin/python

# Java 17 path
export JAVA_HOME=/opt/homebrew/opt/openjdk@17

# Spark install path
export SPARK_HOME=/opt/homebrew/opt/apache-spark/libexec
export PATH=$SPARK_HOME/bin:$PATH

# Launch VS Code
code .
