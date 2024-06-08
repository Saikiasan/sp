import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import tempfile
import shutil

# Function to download images from a webpage
def download_images_from_webpage(url):
    # Create a temporary directory to save images
    temp_dir = tempfile.mkdtemp()
    
    try:
        # Fetch the webpage content
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
            return None

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all image tags
        img_tags = soup.find_all('img')

        # List to hold paths of downloaded images
        image_paths = []

        for img in img_tags:
            img_url = img.get('src')
            if not img_url:
                continue
            
            # Handle relative URLs
            if img_url.startswith('/'):
                img_url = url + img_url

            # Download the image
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                # Create an image file path
                img_name = os.path.join(temp_dir, os.path.basename(img_url))
                with open(img_name, 'wb') as f:
                    f.write(img_response.content)
                image_paths.append(img_name)
            else:
                print(f"Failed to download image. Status code: {img_response.status_code}")

        return temp_dir, image_paths

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Function to create a PDF from downloaded images
def create_pdf_from_images(image_paths, pdf_path):
    images = []
    for img_path in image_paths:
        image = Image.open(img_path)
        # Convert to RGB if image is in palette mode (like PNG with transparency)
        if image.mode in ('RGBA', 'P'):
            image = image.convert('RGB')
        images.append(image)
    
    # Save the images as a PDF
    if images:
        images[0].save(pdf_path, save_all=True, append_images=images[1:])

# Function to clean up temporary directory
def clean_up_temp_dir(temp_dir):
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)

# Main function to download images, create PDF, and clean up
def main(url, output_pdf_path):
    temp_dir, image_paths = download_images_from_webpage(url)
    
    if image_paths:
        create_pdf_from_images(image_paths, output_pdf_path)
        print(f"PDF created at: {output_pdf_path}")
        clean_up_temp_dir(temp_dir)
        print("Temporary files cleaned up.")
    else:
        print("No images found or failed to download images.")

if __name__ == "__main__":
    webpage_url = input("Enter the webpage URL: ")
    output_pdf = "output.pdf"
    main(webpage_url, output_pdf)
