import os

for root, dir, files in os.walk("/root"):
    for file in files:
        if file.endswith('.txt'):
            print(f"{root}/{file}")
