import os
import shutil
import sys
import subprocess

def install_opendatasets():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "opendatasets"])

def download_high_res_data():
    print("👗 Vestiary Data Downloader")
    print("--------------------------------")
    print("This script will download the High-Resolution Fashion Dataset from Kaggle.")
    print("NOTE: This requires a Kaggle account and API key (kaggle.json).")
    print("The dataset is approximately 15GB.")
    
    confirm = input("Do you want to proceed? (y/n): ")
    if confirm.lower() != 'y':
        print("Download cancelled.")
        return

    try:
        import opendatasets as od
    except ImportError:
        print("Installing opendatasets...")
        install_opendatasets()
        import opendatasets as od

    dataset_url = "https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset"
    data_dir = "high_res_data"
    
    print(f"Downloading to {data_dir}...")
    od.download(dataset_url, data_dir)
    
    print("\n✅ Download Complete!")
    print("\nTo use this data:")
    print(f"1. Go to {data_dir}/fashion-product-images-dataset/featured_fashion_product_images/images/")
    print("2. Copy the contents to your project's 'images/images/' folder.")
    print("   (Backup your current images first!)")

if __name__ == "__main__":
    download_high_res_data()
