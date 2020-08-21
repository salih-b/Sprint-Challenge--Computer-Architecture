
"""Main."""
from cpu import *


cpu = CPU()

#
# Execute commands
#

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: ls8.py <filename>", file=sys.stderr)
        sys.exit(1)

    cpu.load(sys.argv[1])
    cpu.run()