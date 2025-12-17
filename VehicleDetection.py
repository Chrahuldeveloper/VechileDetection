import kagglehub
import os
import yaml
import subprocess

path = kagglehub.dataset_download("nadinpethiyagoda/vehicle-dataset-for-yolo")
print("Path to dataset files:", path)

path = "/root/.cache/kagglehub/datasets/nadinpethiyagoda/vehicle-dataset-for-yolo/versions/1/vehicle dataset/valid"
print(os.listdir(path))

train_path = "/root/.cache/kagglehub/datasets/nadinpethiyagoda/vehicle-dataset-for-yolo/versions/1/vehicle dataset/train/images"
val_path   = "/root/.cache/kagglehub/datasets/nadinpethiyagoda/vehicle-dataset-for-yolo/versions/1/vehicle dataset/valid/images"

classes_path = "/root/.cache/kagglehub/datasets/nadinpethiyagoda/vehicle-dataset-for-yolo/versions/1/vehicle dataset/classes.txt"
with open(classes_path) as f:
    names = [line.strip() for line in f.readlines()]

yaml_data = {
    "train": train_path,
    "val": val_path,
    "nc": len(names),
    "names": names
}

with open("/content/vehicle.yaml", "w") as f:
    yaml.dump(yaml_data, f)

print("YAML created successfully.")
print(open("/content/vehicle.yaml").read())

subprocess.run([
    "yolo",
    "train",
    "model=yolo11n.pt",
    "data=/content/vehicle.yaml",
    "epochs=50",
    "imgsz=640"
])

subprocess.run([
    "yolo",
    "predict",
    "model=/content/runs/detect/train/weights/best.pt",
    "source=/content/test.jpg",
    "conf=0.25"
])
