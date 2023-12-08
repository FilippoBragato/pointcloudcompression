import numpy as np


def str_array(array):
    return ", ".join([str(x) for x in array])

content = "mode: 0" + "\n" + \
          "trisoupNodeSizeLog2: 0" + "\n" + \
          "mergeDuplicatedPoints: 1" + "\n" + \
          "neighbourAvailBoundaryLog2: 8" + "\n" + \
          "intra_pred_max_node_size_log2: 6" + "\n" + \
          "positionQuantizationScale: {}" + "\n" + \
          "maxNumQtBtBeforeOt: 4" + "\n" + \
          "minQtbtSizeLog2: 0" + "\n" \
          "disableAttributeCoding: 1" + "\n" 

lidar =   "planarEnabled: 1" + "\n" + \
          "angularEnabled: 1" + "\n" + \
          "lidarHeadPosition: 0.0, 0.0, 0.0" + "\n" + \
          "numLasers: 64" + "\n" \
          "planarBufferDisabled: 1" + "\n" \
          "zCompensationEnabled: 1" + "\n" \
          "lasersNumPhiPerTurn: 100000" + "\n" 

l_theta = "lasersTheta: " + str_array(np.linspace(-np.pi/6, np.pi/18, 64)) + "\n"
l_z =     "lasersZ: " + str_array(np.zeros(64)) + "\n"
l_phi =   "lasersNumPhiPerTurn: "  + str_array(np.ones(64, dtype=int)*1563) + "\n"

lidar = lidar + l_theta + l_z + l_phi

raht =    "rahtPredictionSearchRange: 5000" + "\n"

if __name__=="__main__":

    scales = [0.0125, 0.03125, 0.125, 0.375]
    for i, scale in enumerate(scales):
        with open("config/p{}.cfg".format(i), "w") as f:
            conf = content.format(scale) + lidar
            f.write(conf)
        # with open("config/r{}.cfg".format(i), "w") as f:
        #     conf = content.format(scale) + lidar + raht
        #     f.write(conf)