# Image Optimizer

A handy tool to automatically resize and optimize images in a given folder for web use.

## Features

- Batch resizes and optimizes images.
- Can process `.png`, `.jpg`, `.jpeg`, `.gif`, and `.bmp` files.
- Outputs to a designated folder.

## Requirements

- Python 3.x
- Pillow library (install with `pip install Pillow`).

## Setup

Before running the script, ensure you update the following paths in the `image_optimizer.py` file:

- `SOURCE_DIRECTORY`: The path to the folder containing your images.
- `DESTINATION_DIRECTORY`: The path to the folder where you want the optimized images to be saved.

## Usage

After configuring the paths in the script, run it with:

```bash
python image_optimizer.py

The script will automatically resize and optimize all supported images in the SOURCE_DIRECTORY and save them to the DESTINATION_DIRECTORY.
Customization

You can adjust the target_size variable in the optimize_image function to your preferred dimensions.
Disclaimer

This script is provided for educational and professional purposes. Please ensure that you have the right to modify and handle the images before use. The author is not responsible for any misuse or damage that might occur.
