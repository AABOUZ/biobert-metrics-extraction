import os
import random
import shutil

random.seed(42)

base_dir = "Data"
train_dir = os.path.join(base_dir, "train")
test_dir = os.path.join(base_dir, "test")

os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

pdfs = [
    f for f in os.listdir(base_dir)
    if f.lower().endswith(".pdf")
]

print("PDF trouvés :", len(pdfs))

random.shuffle(pdfs)

split = int(0.7 * len(pdfs))
train_pdfs = pdfs[:split]
test_pdfs = pdfs[split:]

for f in train_pdfs:
    shutil.move(
        os.path.join(base_dir, f),
        os.path.join(train_dir, f)
    )

for f in test_pdfs:
    shutil.move(
        os.path.join(base_dir, f),
        os.path.join(test_dir, f)
    )

print(f"Train : {len(train_pdfs)}")
print(f"Test  : {len(test_pdfs)}")
