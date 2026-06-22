import os
healthy = len(os.listdir("dataset/healthy"))
diseased = len(os.listdir("dataset/diseased"))
print("Healthy Images:", healthy)
print("Diseased Images:", diseased)
print("Dataset prepared for CNN training")
