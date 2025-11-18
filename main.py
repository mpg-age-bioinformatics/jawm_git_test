#!/usr/bin/env python3
from jawm import Process

# Minimal dummy process
p = Process(
    name="echo_test",
    script="#!/bin/bash\necho Hello jawm! > output.txt\n",
    logs_directory="logs"
)

p.execute()
