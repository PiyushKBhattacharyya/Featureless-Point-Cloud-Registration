import os
from src.loader import load_off_file
from src.registration import apply_icp, evaluate_icp_registration
from src.visualizer import visualize_registration, visualize_saved_point_cloud
from src.utils import save_point_cloud

def main():
    # Define paths
    data_dir = "dataset/ModelNet10/bed"
    output_dir = "dataset/ModelNet10_point_clouds"
    threshold = 0.05  # ICP threshold for point correspondence

    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # List categories in the data directory
    categories = os.listdir(data_dir)
    
    for category in categories:
        category_folder = os.path.join(data_dir, category, 'train')  # Assuming point clouds are in 'train' folder
        
        # Process only if category folder exists
        if os.path.isdir(category_folder):
            print(f"Processing category: {category}")
            
            # Get all .off files in the category folder
            off_files = [f for f in os.listdir(category_folder) if f.endswith('.off')]
            off_files.sort()  # Sort the files to maintain order
            
            # Register each consecutive pair of .off files in the category
            for i in range(len(off_files) - 1):
                # Load source and target point clouds from .off files
                source_off_path = os.path.join(category_folder, off_files[i])
                target_off_path = os.path.join(category_folder, off_files[i + 1])
                
                # Load point clouds
                source_pcd = load_off_file(source_off_path)
                target_pcd = load_off_file(target_off_path)
                
                # Apply ICP only if both point clouds are valid
                if source_pcd and target_pcd:
                    icp_result = apply_icp(source_pcd, target_pcd, threshold)
                    
                    # Print ICP results
                    print(f"ICP Registration between {off_files[i]} and {off_files[i + 1]}:")
                    fitness, inlier_rmse = evaluate_icp_registration(icp_result, source_pcd, target_pcd)
                    print(f"Fitness Score: {fitness:.4f}, Inlier RMSE: {inlier_rmse:.4f}")

                    # Visualize the result
                    visualize_registration(source_pcd, target_pcd, icp_result.transformation)

                    # Save the registered source point cloud
                    output_path = os.path.join(output_dir, f"{category}_{off_files[i].replace('.off', '_registered.pcd')}")
                    save_point_cloud(source_pcd, output_path)
                    print(f"Saved registered point cloud: {output_path}")

                    # Visualize the saved point cloud
                    visualize_saved_point_cloud(output_path)

            print(f"Finished processing category: {category}")

if __name__ == "__main__":
    main()