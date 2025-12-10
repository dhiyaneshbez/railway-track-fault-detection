import os

dataset_path = "dataset"  # change if needed
labels = set()

for split in ["train", "valid", "test"]:  # loops over folders
    label_dir = os.path.join(dataset_path, split, "labels")
    if not os.path.exists(label_dir):
        continue
    for file in os.listdir(label_dir):
        if file.endswith(".txt"):
            with open(os.path.join(label_dir, file), "r") as f:
                for line in f:
                    cls_id = line.split()[0]  # first number = class ID
                    labels.add(int(cls_id))

print("Unique class IDs found:", sorted(labels))
print("Number of classes (nc):", len(labels))
