from pathlib import Path
from scipy.interpolate import interp1d
import numpy as np


def csv2ant(csvfn: Path, antfn: Path = None):
    """
    assume first column is azimuth (deg.) and second column is normalized antenna pattern.
    http://radiomobile.pe1mew.nl/?The_program:File_formats:Antenna_.ant_format_%28V1%29

    Units are dB relative to boresite gain, NOT dBd, dBi etc. just relative gain from maximum.

    angles must be from 0 to 359 degrees, 1 degree step.
    """
    csvfn = Path(csvfn).expanduser()
    dat = np.loadtxt(csvfn, delimiter=",")

    if antfn:
        antfn = Path(antfn).expanduser()
    else:
        antfn = csvfn.with_suffix(".ant")

    assert dat.ndim == 2 and dat.shape[1] == 2

    # wraparound FCC 0-350 degree data
    if (dat[0, 0] == 0) and (dat[-1, 0] == 350):
        dat = np.append(dat, np.array([360, dat[0, 1]])[None, :], axis=0)
    # %% interp
    fdat = interp1d(dat[:, 0], dat[:, 1])

    aznew = np.arange(0, 360.0, 1)
    idat = fdat(aznew)

    idat = np.column_stack((aznew, idat, 20 * np.log10(idat)))

    print("writing", antfn)
    """
    only write amplitude, azimuth is implied
    \r\n is required, even under WINE
    """
    np.savetxt(antfn, idat[:, 2], fmt="%.2f", newline="\r\n")

    return idat
