from utils.constants import *
from utils.general import *
import pandas as pd
import time
import os
import DracoPy
from tqdm import tqdm
    
def compress_with_draco(file_path, compression_level, quantization_bits):
    original_point_cloud = read_ply(file_path.resolve(),const=1)
    out_path = out_dir.joinpath(f"d{quantization_bits*100+compression_level}").joinpath(file_path.name)
    os.makedirs(out_path.parent, exist_ok=True)
    compressed=DracoPy.encode(original_point_cloud, 
                                         compression_level=compression_level, 
                                         quantization_bits=quantization_bits)
    result = DracoPy.decode(compressed)
    points = np.array(result.points)
    np.save(out_path.with_suffix(".npy"), points)


def convert_test_set():
    """
    Converts the test set from the original raw format to using G-PCC.
    """
    test_files_path = get_files_path(selma_path)
    for file_path in tqdm(test_files_path):
        for quantization_bits in [7,8,9,10,11,12]:
            for compression_level in [0,5,10]:
                compress_with_draco(file_path, compression_level, quantization_bits)
    

if __name__ == "__main__":
    convert_test_set()
