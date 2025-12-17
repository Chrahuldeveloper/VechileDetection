Vehicle Detection using YOLO

This project demonstrates vehicle detection using the Ultralytics YOLOv8 model.
The model is trained on a custom vehicle dataset and can detect vehicles in images.

Note: Datasets and trained weights are not included in the repo. See instructions below.

🛠️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/<your-username>/VehicleDetection.git
cd VehicleDetection

2️⃣ Install dependencies
pip install ultralytics kagglehub pyyaml

3️⃣ Download dataset
import kagglehub
kagglehub.dataset_download("nadinpethiyagoda/vehicle-dataset-for-yolo")
