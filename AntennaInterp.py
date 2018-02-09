#!/usr/bin/env python
from rmwutils import csv2ant, plot_ant_pattern
try:
    from matplotlib.pyplot import show
    import seaborn as sns
    sns.set_context('talk')
except ImportError:
    show = None


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser()
    p.add_argument('csvfn',help='.csv file containing only rows of normalized antenna pattern vs. azimuth over 0-360 deg.')
    p.add_argument('antfn',help='.ant filename to write',nargs='?')
    p.add_argument('--titletext',default='')
    p = p.parse_args()


    dat = csv2ant(p.csvfn, p.antfn)


    if show is not None:
        plot_ant_pattern(dat, p.titletext)

        show()