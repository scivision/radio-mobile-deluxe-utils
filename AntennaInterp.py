#!/usr/bin/env python3
from rmwutils import csv2ant
from rmwutils.plots import plot_ant_pattern

from matplotlib.pyplot import show


from argparse import ArgumentParser

p = ArgumentParser()
p.add_argument(
    "csvfn",
    help=".csv file containing only rows of normalized antenna pattern vs. azimuth over 0-360 deg.",
)
p.add_argument("antfn", help=".ant filename to write", nargs="?")
p.add_argument("--titletext", default="")
p = p.parse_args()


dat = csv2ant(p.csvfn, p.antfn)

plot_ant_pattern(dat, p.titletext)

show()
