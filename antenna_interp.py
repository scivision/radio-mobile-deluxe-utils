#!/usr/bin/env python
from rmwutils import csv2ant

def main(csvfn, antfn):
    dat = csv2ant(csvfn,antfn)


if __name__ = '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('csvfn',help='.csv file containing only rows of normalized antenna pattern vs. azimuth over 0-360 deg.')
    p.add_argument('antfn',help-'.ant filename to write')
    p = p.parse_args()

    main(p.csvfn,p .antfn)