import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
import numpy as np


def plot_m_nalew_by_t():
    df = pd.read_csv('brzoskwiniowka_m_nalew_by_t.csv')
    plt.plot(df.t, df.m, '.-')
    plt.xlabel('czas t [h]')
    plt.ylabel('masa nalewu [g]')

    plt.savefig("brzoskwiniowka_m_nalew_by_t.png")
    plt.show()


def plot_dm_nalew_by_dt():
    df = pd.read_csv('brzoskwiniowka_m_nalew_by_t.csv')
    df.m = df.m.diff() / df.t.diff()
    df = df.dropna()
    df_to_approximate = df[2:]  # bez 1. i 2. punktu
    model = smf.ols('np.log(m) ~ t', data=df_to_approximate).fit()
    plt.plot(df.t, df.m, '.')
    plt.xlabel('czas t [h]')
    plt.ylabel('przepływ S [g/h]')
    xes = np.arange(0, 120, 1)
    plt.plot(xes, np.exp(model.params['Intercept'] + model.params['t'] * xes))

    print(model.summary())

    plt.savefig("brzoskwiniowka_dm_nalew_by_dt.png")
    plt.show()


if __name__ == "__main__":
    plot_m_nalew_by_t()
    plot_dm_nalew_by_dt()

