from matplotlib.pyplot import figure
import numpy as np


def plot_ant_pattern(dat: np.ndarray, ttxt: str = ""):
    if figure is None:
        return

    ax = [figure().gca(polar=True)]

    ax[0].plot(np.radians(dat[:, 0]), dat[:, 1])
    # ax[1].plot(np.radians(dat[:,0]), dat[:,2])

    for a in ax:
        a.set_theta_zero_location("N")
        a.set_theta_direction(-1)

        a.set_rmax(1)

        a.set_xlabel("azimuth (deg.)")
        a.set_title(ttxt)

    ax[0].set_ylabel("relative amplitude")
    # ax[1]
