from PIL import Image
import os

# Define the source and destination directories
SOURCE_DIRECTORY = '/path/to/your/images'
DESTINATION_DIRECTORY = '/path/to/optimized/images'

def optimize_image(file_path, output_folder):
    # Open an image file
    with Image.open(file_path) as img:
        # The target resolution
        target_size = (800, 600)
        # Resize the image
        img = img.resize(target_size, Image.ANTIALIAS)
        
        # Define the output file path
        filename = os.path.basename(file_path)
        output_file_path = os.path.join(output_folder, filename)
        
        # Save the optimized image
        img.save(output_file_path, optimize=True, quality=85)

def main():
    # Create destination directory if it doesn't exist
    if not os.path.exists(DESTINATION_DIRECTORY):
        os.makedirs(DESTINATION_DIRECTORY)
    
    # Process all images in the source directory
    for image_name in os.listdir(SOURCE_DIRECTORY):
        if image_name.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            file_path = os.path.join(SOURCE_DIRECTORY, image_name)
            optimize_image(file_path, DESTINATION_DIRECTORY)

    print("Image optimization complete. Check the destination directory for optimized images.")

if __name__ == "__main__":
    main()
