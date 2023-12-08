from pathlib import Path
import glob
import os

gpcc_path = Path('/home/filo/Desktop/PhD/papers/02_Compression/mpeg-pcc-tmc13/build/tmc3/tmc3')
selma_path = Path('/home/filo/Desktop/PhD/papers/02_Compression/selma/')
out_dir = Path('/home/filo/Desktop/PhD/papers/02_Compression/scratch/output')
config_dir = Path('/home/filo/Desktop/PhD/papers/02_Compression/scratch/config')

config_files = glob.glob("config/*.cfg")
modes = [os.path.basename(f).replace(".cfg", "") for f in config_files]
modes.sort()

 #+ ["r0", "r1", "r2", "r3"]#, "p4", "p5"], "r4", "r5"]#, "r6", "r7", "r8", "r9", "r10", "r11"]
#, "p6", "p7", "p8", "p9", "p10", "p11"] + \
