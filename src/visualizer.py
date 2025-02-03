import open3d as o3d

def visualize_registration(source, target, transformation):
    """
    Visualize the source and target point clouds after applying the ICP transformation to the source point cloud.
    """
    # Apply the transformation to the source point cloud
    source_temp = source.transform(transformation)
    
    # Visualize the point clouds
    o3d.visualization.draw_geometries([source_temp, target], window_name="ICP Registered Point Clouds")

def visualize_saved_point_cloud(output_path):
    """
    Visualize the saved point cloud from a .pcd file.
    """
    saved_pcd = o3d.io.read_point_cloud(output_path)
    o3d.visualization.draw_geometries([saved_pcd], window_name="Saved Point Cloud")