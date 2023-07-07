# Name: ALinda Kumar Mazumder
# NSID: ugj683
# Student no: 11342454
# CMPT-145
import sys
from Stack import Stack
from Queue import Queue


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in ['s', 'q']:
        print("Usage: python3 a3q1.py <container_type>")
        print("Container types: 's' for stack, 'q' for queue")
        return

