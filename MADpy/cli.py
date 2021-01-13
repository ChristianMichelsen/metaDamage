import click
from dotmap import DotMap as DotDict

from MADpy import fileloader
from MADpy import fit
from MADpy import plot
from MADpy import utils

from main import main


@click.command()
@click.argument("filename", type=click.Path(exists=True), nargs=-1)
@click.option("--verbose", is_flag=True, default=False, help="Verbose. Flag. Default is True.")
@click.option(
    "--number_of_fits",
    default=10,
    help="Number of fits to make. Default is 10. '-1' or '0' indicates to fit all TaxIDs.",
)
@click.option("--number_of_plots", default=10, help="Number of plots to make. Default is 10.")
@click.option(
    "--make_plots", default=True, is_flag=True, help="Make plots. Flag. Default is True",
)
@click.option(
    "--make_fits", default=True, is_flag=True, help="Make plots. Flag. Default is True",
)
@click.option("--num_cores", default=1, help="Number of cores to use. Default is 1.")
@click.option(
    "--force_plots", is_flag=True, default=False, help="Force plots. Flag. Default is False",
)
@click.version_option()
def cli(
    filename,
    verbose,
    number_of_fits,
    number_of_plots,
    make_plots,
    make_fits,
    num_cores,
    force_plots,
):
    """Metagenomics Ancient Damage python: MADpy

    FILENAME is the name of the file(s) to fit (with the ancient-model)

    run as e.g.:

    \b
        $ MADpy --verbose --number_of_fits 10 --num_cores 2 ./data/input/data_ancient.txt

    or by running two files and then compare them:

    \b
        $ MADpy --verbose --number_of_fits 10 --num_cores 2 ./data/input/data_ancient.txt ./data/input/data_control.txt

    """

    filenames = filename

    cfg = DotDict(
        {
            "N_taxids": number_of_fits,
            "max_pos": None,
            "verbose": verbose,
            "make_fits": make_fits,
            "make_plots": make_plots,
            "max_plots": number_of_plots,
            "force_reload": False,
            "force_plots": force_plots,
            "force_fits": False,
            "num_cores": num_cores,
        }
    )

    main(filenames, cfg)
