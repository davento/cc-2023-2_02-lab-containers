from pyspark import SparkContext
import sys
import os
import time
import shutil
import re

# Verify that program is used correctly
if len(sys.argv) != 3:
    print("Usage: wordcount <input> <output>")
    exit(-1)

# Declare file routes
inputPath = sys.argv[1]
outputPath = sys.argv[2]

if os.path.exists(outputPath):
    os.remove(outputPath)

# Set up starting time for cAdvisor
testingTime = 10
for i in range(testingTime, 0, -1):
    print("Starting in " + str(i) + " s")
    time.sleep(1)
print("\nStarting process\n")

# Start app
sc = SparkContext(appName="PythonWordCount")

# Read data
text_file = sc.textFile(inputPath)
# Process data
counts = text_file.flatMap(lambda line: re.findall(r'\b\w+\b', line)) \
             .map(lambda word: (word, 1)) \
             .reduceByKey(lambda a, b: a + b) \
             .sortBy(lambda x : x[1], ascending=False)

# Merge result in a single file
outputPathTemp = outputPath + "_temp"
counts.coalesce(1).saveAsTextFile(outputPathTemp)
os.rename(os.path.join(outputPathTemp, "part-00000"), outputPath)
shutil.rmtree(outputPathTemp)

# Stop app
sc.stop()

# Set up ending time for cAdvisor
for i in range(testingTime, 0, -1):
    print("Finishing in " + str(i) + " s")
    time.sleep(1)
print("\nProcess finished\n")