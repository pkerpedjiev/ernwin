#!/usr/bin/python

from __future__ import absolute_import
from __future__ import print_function
import sys
from optparse import OptionParser

import tess.threedee.model.coarse_grain as ttmc
from six.moves import range

def main():
    parser = OptionParser()

    #parser.add_option('-o', '--options', dest='some_option', default='yo', help="Place holder for a real option", type='str')
    #parser.add_option('-u', '--useless', dest='uselesss', default=False, action='store_true', help='Another useless option')

    (options, args) = parser.parse_args()

    if len(args) < 1:
        print("Usage: ./stem_angles.py temp.comp", file=sys.stderr)
        print("Print the angles between the stems in temp.comp", file=sys.stderr)
        sys.exit(1)

    bg = ttmc.CoarseGrainRNA(args[0])

    stems = [d for d in bg.defines.keys() if d[0] == 's']

    for i in range(len(stems)):
        for j in range(i+1, len(stems)):
            #p1 = bg.get_point[stems[i]]
            #p2 = bg.get_point[stems[j]]

            if len(bg.edges[stems[i]].intersection(bg.edges[stems[j]])) > 0:
                print(bg.name, stems[i], stems[j], bg.get_stem_angle(stems[i], stems[j]))

if __name__ == '__main__':
    main()

