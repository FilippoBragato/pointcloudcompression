from utils.constants import *
from utils.general import *
import pandas as pd
import time
import os

    
def compress_with_gpcc(file_path, mode):
    """

    """
    bin_file_path = Path("temp.bin")
    ply_file_path = Path("temp.ply")
    write_ply(ply_file_path.resolve(), read_ply(file_path.resolve()))
    out_path = out_dir.joinpath(mode).joinpath(file_path.name)
    os.makedirs(out_path.parent, exist_ok=True)

    compress_command = f"{gpcc_path.resolve()} " +\
        f"--mode=0 " +\
        f"--config={config_dir.joinpath(mode).with_suffix('.cfg').resolve()} "+\
        f"--uncompressedDataPath=\"{ply_file_path.resolve()}\" " +\
        f"--compressedStreamPath=\"{bin_file_path.resolve()}\" --srcUnit=1"
    decompress_command = f"{gpcc_path.resolve()} "+\
        f"--mode=1 "+\
        f"--reconstructedDataPath=\"{out_path.resolve()}\" "+\
        f"--compressedStreamPath=\"{bin_file_path.resolve()}\" --srcUnit=1"

    c_out = os.system(compress_command)
    d_out = os.system(decompress_command)

    os.remove(bin_file_path)
    os.remove(ply_file_path)

    points = read_ply(out_path)
    points = np.array(points)/10000
    np.save(out_path.with_suffix(".npy"), points)

    os.remove(out_path)


def convert_test_set():
    """
    Converts the test set from the original raw format to using G-PCC.
    """
    test_files_path = get_files_path(selma_path)
    for file_path in test_files_path:
        for mode in modes:
            print(mode)
            compress_with_gpcc(file_path, mode)
    

if __name__ == "__main__":
    convert_test_set()