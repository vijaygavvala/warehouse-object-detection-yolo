import os

print("Starting Warehouse Object Detection Project")

print("1. Train Model")
print("2. Predict Objects")
print("3. Evaluate Model")

choice = input("Enter option (1/2/3): ")

if choice == "1":
    os.system("python notebook/train.py")

elif choice == "2":
    os.system("python predict.py")

elif choice == "3":
    os.system("python evaluate.py")

else:
    print("Invalid option")
