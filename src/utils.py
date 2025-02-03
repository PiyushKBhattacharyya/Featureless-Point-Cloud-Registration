import open3d as o3d

def save_point_cloud(pcd, file_path):
    """
    Save the point cloud to a .pcd file.
    """
    o3d.io.write_point_cloud(file_path, pcd)
    print(f"Saved the point cloud to: {file_path}") 