from pathlib import Path
import starfile

from tomo_viewer import TomoViewer


def star_import(starfile_path):
    """
    load data from a .star file and return a ready-to-go Micrograph object
    """
    df = starfile.read(starfile_path)

    split_micrographs = df.groupby('rlnMicrographName')

    micrographs = {}
    for name, df in split_micrographs:
        short_name = Path(name).stem
        micrographs[short_name] = TomoViewer(df, name=short_name)

    return micrographs
