import open3d as o3d
import numpy as np

def apply_icp(source, target, threshold=0.05):
    """
    Apply ICP (Iterative Closest Point) for point cloud registration.
    """
    print(f"Source Point Cloud type: {type(source)}")
    print(f"Target Point Cloud type: {type(target)}")
    
    # Check the number of points in each point cloud
    print(f"Source Point Cloud has {len(source.points)} points.")
    print(f"Target Point Cloud has {len(target.points)} points.")

    # Identity matrix as the initial transformation
    init_transformation = np.eye(4)
    print(f"Initial Transformation Matrix:\n{init_transformation}")

    # Define the ICP method (Point-to-Point)
    estimation_method = o3d.pipelines.registration.TransformationEstimationPointToPoint(with_scaling=False)
    
    # Perform ICP registration with the defined method
    icp_result = o3d.pipelines.registration.registration_icp(
        source, target, threshold,
        init_transformation,  # Identity matrix as initial transformation
        estimation_method,    # Explicitly specify the estimation method
        o3d.pipelines.registration.ICPConvergenceCriteria(max_iteration=200)
    )
    
    return icp_result

def evaluate_icp_registration(icp_result, source, target):
    """
    Evaluate the quality of the ICP registration by calculating the fitness score and inlier RMSE.
    """
    fitness = icp_result.fitness  # Fitness score
    inlier_rmse = icp_result.inlier_rmse  # Inlier RMSE
    
    print(f"Fitness: {fitness:.4f}")
    print(f"Inlier RMSE: {inlier_rmse:.4f}")
    
    return fitness, inlier_rmse