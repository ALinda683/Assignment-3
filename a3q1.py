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

    container_type = sys.argv[1]
    container = None

    if container_type == 's':
        container = Stack()
    elif container_type == 'q':
        container = Queue()


