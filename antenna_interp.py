#!/usr/bin/env python
from rmwutils import csv2ant, plot_ant_pattern
from matplotlib.pyplot import show
import seaborn as sns
sns.set_context('talk')

def main(csvfn, antfn, ttxt):
    dat = csv2ant(csvfn, antfn)

    plot_ant_pattern(dat, ttxt)


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('csvfn',help='.csv file containing only rows of normalized antenna pattern vs. azimuth over 0-360 deg.')
    p.add_argument('antfn',help='.ant filename to write')
    p.add_argument('--titletext')
    p = p.parse_args()

    main(p.csvfn, p.antfn, p.titletext)

    show()