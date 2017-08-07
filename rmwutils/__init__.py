from pathlib import Path
from scipy.interpolation import interp1d
from pandas import read_csv
from numpy import savetxt,arange

def csv2ant(csvfn,antfn):
    """
    assume first column is azimuth (deg.) and second column is normalized antenna pattern.
    """
    csvfn = Path(csvfn).expanduser()
    dat = read_csv(csvfn)

    antfn = Path(antfn).expanduser()
# %% interp
    fdat = interp1d(dat[:,0], dat[:,1])

    aznew = arange(360.)
    idat = fdat(aznew)

    savetxt(antfn, idat)

    return idat,aznew

def plot_ant_pattern(dat):
