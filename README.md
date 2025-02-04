# Featureless Point Cloud Registration


## Overview
This project focuses on **featureless point cloud registration**, where **Iterative Closest Point (ICP)** and other geometric alignment techniques are used to register point clouds without relying on explicit features.

## Dataset
- **ModelNet10** (Synthetic Object Models)
- **Format:** `.off` (Object File Format)

## Methodology
1. **Data Preprocessing**
   - Convert point cloud formats as needed.
2. **Point Cloud Registration Techniques**
   - **ICP (Iterative Closest Point)** for fine alignment.
3. **Evaluation**
   - Alignment error metrics.
   - Visualization of registered point clouds.


## Installation & Usage
### Prerequisites
- Python 3.8+
- Open3D, NumPy, SciPy
- Matplotlib for visualization

### Installation
```bash
pip install -r requirements.txt
```

### Run
```python main.py```

## Future Work
- Integrate **deep learning-based point cloud registration**.
- Improve robustness under noisy conditions.
- Extend support for **multi-view registration**.

## Acknowledgments
- **ModelNet10** for synthetic object models.
- **Open3D Library** for point cloud processing.
