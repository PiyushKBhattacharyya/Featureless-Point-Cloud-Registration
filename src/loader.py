import open3d as o3d

def load_off_file(file_path):
    """
    Load a .off file and return it as a point cloud.
    """
    # Read the .off file as a triangle mesh
    mesh = o3d.io.read_triangle_mesh(file_path)
    
    # Check if the mesh contains valid triangles
    if not mesh.has_triangles():
        print(f"Error: {file_path} does not contain valid triangles.")
        return None
    
    # Sample points from the mesh (featureless registration)
    pcd = mesh.sample_points_poisson_disk(number_of_points=10000)
    
    return pcd

def load_pcd_file(file_path):
    """
    Load a .pcd file and return it as a point cloud.
    """
    # Read the .pcd file as a point cloud
    pcd = o3d.io.read_point_cloud(file_path)
    
    return pcd