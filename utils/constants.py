from pathlib import Path
import glob
import os

gpcc_path = Path('')
selma_path = Path('')
out_dir = Path('')
config_dir = Path('')

config_files = glob.glob("config/*.cfg")
modes = [os.path.basename(f).replace(".cfg", "") for f in config_files]
modes.sort()

 #+ ["r0", "r1", "r2", "r3"]#, "p4", "p5"], "r4", "r5"]#, "r6", "r7", "r8", "r9", "r10", "r11"]
#, "p6", "p7", "p8", "p9", "p10", "p11"] + \
