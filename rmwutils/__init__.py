from pathlib import Path
from scipy.interpolate import interp1d
from pandas import read_csv
import numpy as np
from xarray import DataArray
from matplotlib.pyplot import figure

def csv2ant(csvfn,antfn):
    """
    assume first column is azimuth (deg.) and second column is normalized antenna pattern.
    """
    csvfn = Path(csvfn).expanduser()
    dat = read_csv(csvfn, header=None, names=['azimuth','amplitude'])

    antfn = Path(antfn).expanduser()
# %% interp
    fdat = interp1d(dat['azimuth'], dat['amplitude'])

    aznew = np.arange(360.)
    idat = fdat(aznew)
    idat = DataArray(idat, coords={'azimuth':aznew}, dims=['azimuth'])

    ndat = 10*np.log10(idat.values)

    assert ndat.shape==(360,)

    np.savetxt(antfn, ndat, fmt='%.2f')  # only write amplitude, azimuth is implied

    return idat

def plot_ant_pattern(dat, ttxt):
    ax = figure().gca(polar=True)

    ax.set_theta_zero_location('N')
    ax.set_theta_direction(-1)

    ax.plot(np.radians(dat.azimuth), dat)

    ax.set_title(ttxt)
    ax.set_xlabel('azimuth (deg.)')