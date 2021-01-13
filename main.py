import numpy as np
import pandas as pd
from tqdm import tqdm
from dotmap import DotMap as DotDict
from importlib import reload

from MADpy import fileloader
from MADpy import fit
from MADpy import plot
from MADpy import utils

import numpyro
numpyro.enable_x64()

#%%


def main(filenames, cfg):

    all_fit_results = {}

    for filename in filenames:
        cfg["filename"] = filename
        cfg["name"] = utils.extract_name(filename)

        df = fileloader.load_dataframe(cfg)
        # df_top_N = fileloader.get_top_N_taxids(df, cfg.N_taxids)

        if False:
            taxid = 241227
            group = df.query("taxid == @taxid")

        d_fits = None
        if cfg.make_fits:
            d_fits, df_results = fit.get_fits(df, cfg)
            all_fit_results[cfg.name] = df_results

        if cfg.make_plots:
            plot.set_style()
            plot.plot_error_rates(cfg, df, d_fits=d_fits)

    if len(all_fit_results) >= 1:
        plot.set_style()
        N_alignments_mins = [0, 10, 100, 1000, 10_000, 100_000]
        plot.plot_fit_results(all_fit_results, cfg, N_alignments_mins=N_alignments_mins)


if utils.is_ipython():

    print("Doing iPython plot")

    # filenames = [
    #     "./data/input/data_ancient.txt",
    #     "./data/input/data_control.txt",
    # ]

    filenames = [
        "./data/input/KapK-12-1-35-Ext-12-Lib-12-Index2.col.sorted.sam.gz.family.bdamage.gz.counts.txt",
        "./data/input/EC-Ext-14-Lib-14-Index1.col.sorted.sam.gz.family.bdamage.gz.counts.txt",
    ]

    cfg = DotDict(
        {
            "N_taxids": -1,
            "max_pos": None,
            "verbose": True,
            "make_fits": True,
            "make_plots": True,
            "max_plots": 1000,
            "force_reload": False,
            "force_plots": False,
            "force_fits": False,
            "parallel_plots": True,
            "num_cores": 6,
        }
    )

    if False:
        main(filenames, cfg)
