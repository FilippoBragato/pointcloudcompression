import open3d as o3d
from plyfile import PlyData, PlyElement
import numpy as np
import open3d as o3d
import numpy as np
from .constants import *

def get_files_path(selma_path):
    """
    Returns the path to the test files.
    """
    with open("val.txt", "r") as f:
        files = f.readlines()
    files = [x.strip() for x in files]
    out = []
    for f in files:
        folder = f.split("_")[:-1]
        folder = "_".join(folder)
        o = selma_path.joinpath("selma", folder, "LIDAR_TOP", f).with_suffix(".ply")
        out.append(o)
    return out

def read_ply(filename, const=100):
    """Reads a .ply file and returns a numpy array."""
    points = PlyData.read(filename)
    
    pts = list(zip(np.array(points["vertex"]["x"]*const),
                   np.array(points["vertex"]["y"]*const),
                   np.array(points["vertex"]["z"]*const)))

    
    return pts

def write_ply(filename, points):
    """Writes a numpy array to a .ply file."""
    ply_out = np.array(points,
                       dtype=[("x", np.float32),
                              ("y", np.float32),
                              ("z", np.float32)])
    el = PlyElement.describe(ply_out, "vertex")
    PlyData([el], text=False).write(filename)

def visualize_ply(filename, camera_model=None):
    """Visualizes a .ply file."""
    points = np.load(filename)
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(points)
    if camera_model:
        vis = o3d.visualization.Visualizer()
        vis.create_window()
        mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()
        vis.add_geometry(pcd)
        vis.add_geometry(mesh)

        vc = vis.get_view_control()
        vc.convert_from_pinhole_camera_parameters(camera_model)
        vis.run()

    else:
        mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()
        o3d.visualization.draw_geometries([pcd, mesh])


def visualize_all_ply():
    """
    Visualizes all the ply files in the test set.
    """

    camera_model = o3d.io.read_pinhole_camera_parameters("camera.json")
    test_files_path = get_files_path(selma_path)
    vis = o3d.visualization.Visualizer()
    vis.create_window()
    pcd = o3d.io.read_point_cloud(str(test_files_path[0]))
    mesh = o3d.geometry.TriangleMesh.create_coordinate_frame()
    vis.clear_geometries()
    vis.add_geometry(pcd)
    vis.add_geometry(mesh)

    vc = vis.get_view_control()
    vc.convert_from_pinhole_camera_parameters(camera_model)

    vis.poll_events()
    vis.update_renderer()

    vis.run()


    

    vcpcp = vis.get_view_control().convert_to_pinhole_camera_parameters()

    vis.destroy_window()


    for file_path in test_files_path:
        for mode in modes:
            out_path = out_dir.joinpath(mode).joinpath(file_path.name).with_suffix(".npy")
            visualize_ply(out_path, camera_model=vcpcp)
