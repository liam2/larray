import os
import larray as la


_TEST_DIR = os.path.join(os.path.dirname(__file__), 'tests')

EXAMPLE_FILES_DIR = os.path.join(_TEST_DIR, 'data')
# TODO : replace 'demography.h5' by 'population_session.h5' and remove 'demo' ?
AVAILABLE_EXAMPLE_DATA = {
    'demo': os.path.join(EXAMPLE_FILES_DIR, 'population_session.h5'),
    'demography': os.path.join(EXAMPLE_FILES_DIR, 'demography.h5')
}
AVAILABLE_EXAMPLE_FILES = os.listdir(EXAMPLE_FILES_DIR)

EXAMPLE_EXCEL_TEMPLATES_DIR = os.path.join(_TEST_DIR, 'excel_template')


def get_example_filepath(fname):
    """Return absolute path to an example file if exist.

    Parameters
    ----------
    fname : str
        Filename of an existing example file.

    Returns
    -------
    Filepath
        Absolute filepath to an example file if exists.

    Notes
    -----
    A ValueError is raised if the provided filename does not represent an existing example file.

    Examples
    --------
    >>> fpath = get_example_filepath('examples.xlsx')
    """
    fpath = os.path.abspath(os.path.join(EXAMPLE_FILES_DIR, fname))
    if not os.path.exists(fpath):
        raise ValueError("Example file {} does not exist. "
                         "Available example files are: {}".format(fname, AVAILABLE_EXAMPLE_FILES))
    return fpath


def load_example_data(name):
    """Load arrays used in the tutorial so that all examples in it can be reproduced.

    Parameters
    ----------
    name : str
        Example data to load. Available example datasets are:

        - demography

    Returns
    -------
    Session
        Session containing one or several arrays

    Examples
    --------
    >>> demo = load_example_data('demography')
    >>> demo.pop.info # doctest: +SKIP
    26 x 3 x 121 x 2 x 2
     time [26]: 1991 1992 1993 ... 2014 2015 2016
     geo [3]: 'BruCap' 'Fla' 'Wal'
     age [121]: 0 1 2 ... 118 119 120
     sex [2]: 'M' 'F'
     nat [2]: 'BE' 'FO'
    >>> demo.qx.info # doctest: +SKIP
    26 x 3 x 121 x 2 x 2
     time [26]: 1991 1992 1993 ... 2014 2015 2016
     geo [3]: 'BruCap' 'Fla' 'Wal'
     age [121]: 0 1 2 ... 118 119 120
     sex [2]: 'M' 'F'
     nat [2]: 'BE' 'FO'
    """
    if name is None:
        name = 'demography'
    if not isinstance(name, str):
        raise TypeError("Expected string for argument example_data")
    if name not in AVAILABLE_EXAMPLE_DATA.keys():
        raise ValueError("example_data must be chosen from list {}".format(list(AVAILABLE_EXAMPLE_DATA.keys())))
    return la.Session(AVAILABLE_EXAMPLE_DATA[name])
