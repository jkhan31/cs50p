import os
from PIL import Image
import pytesseract
from tqdm import tqdm
import requests

def extract_text_from_image(image_path):
    img = Image.open(image_path)
    text = pytesseract.image_to_string(img)
    return text

def download_image_from_url(url, file_name):
    response = requests.get(url, stream=True)
    with open(file_name, 'wb') as image_file:
        for chunk in response.iter_content(chunk_size=128):
            image_file.write(chunk)

def process_single_image(image_path):
    extracted_text = extract_text_from_image(image_path)
    text_file_name = os.path.splitext(os.path.basename(image_path))[0] + ".txt"
    text_file_path = os.path.join(os.path.dirname(image_path), text_file_name)
    save_text_to_file(extracted_text, text_file_path)

def process_images_in_folder(folder_path):
    num_images = sum([len(files) for _, _, files in os.walk(folder_path)])
    progress_bar = tqdm(total=num_images, unit="image")

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                image_path = os.path.join(root, file)
                process_single_image(image_path)
                progress_bar.update(1)

    progress_bar.close()

def save_text_to_file(text, file_path):
    with open(file_path, 'w') as text_file:
        text_file.write(text)

def main():
    source = input("Please provide the path to the folder containing images, a single image file, or a URL: ")

    if os.path.isdir(source):
        process_images_in_folder(source)
        print("Text extraction completed successfully.")
    elif os.path.isfile(source) and source.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        process_single_image(source)
        print("Text extraction completed successfully.")
    elif source.startswith('http'):
        try:
            response = requests.head(source)
            if response.status_code == 200:
                image_name = os.path.basename(source)
                download_image_from_url(source, image_name)
                process_single_image(image_name)
                os.remove(image_name)
                print("Text extraction completed successfully.")
            else:
                print("Error: Invalid URL.")
        except Exception as e:
            print(f"Error downloading image from URL: {e}")
    else:
        print("Invalid input. Please provide a valid local folder path, a single image file, or a URL.")

if __name__ == "__main__":
    main()