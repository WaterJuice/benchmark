#!/usr/bin/env python3

import sys
import time
import subprocess
import argparse

# Benchmark based on "Dell Optiplex 7060 (6 core i7)"
BENCHMARK_SECONDS = 74
VERSION = "1.0.0 (Dec 2021)"

parser = argparse.ArgumentParser(
    description="Performs a C project building tasks and times it to compare it benchmark figure. Benchmark based on Dell Optiplex 7060 (6 core i7)"
)
parser.add_argument("--version", action="version", version=VERSION)
args = parser.parse_args()

print(":::: Starting Benchmark job. This will take a while :::::")

startTime = time.time()
subprocess.run(["cmake", "--build", "build"])
endTime = time.time()

timeTaken = endTime - startTime

seconds = int(timeTaken)

benchmark = int(100 * BENCHMARK_SECONDS / seconds)

print("")
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print(":: Benchmark complete")
print(":: Time taken: %u seconds" % seconds)
print(":: Reference time for scale: %u" % BENCHMARK_SECONDS)
print("::")
print(":: Benchmark: %u" % benchmark)
print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
