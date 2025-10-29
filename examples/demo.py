#!/usr/bin/env python3
from jawm import Process

demo = Process(
    name="demo_proc",
    script="#!/bin/bash\necho Demo example executed > demo_output.txt\n",
    logs_directory="logs_demo"
)

demo.execute()