import argparse
import base64
import os
import requests
from picarta import Picarta

def get_home_directory():
    return os.path.expanduser("~")

# Function to save API token to a file in the home directory
def save_api_token(token, filename="api_token.txt"):
    home_dir = get_home_directory()
    file_path = os.path.join(home_dir, filename)
    with open(file_path, "w") as file:
        file.write(token)

# Function to read API token from a file in the home directory
def read_api_token(filename="api_token.txt"):
    home_dir = get_home_directory()
    file_path = os.path.join(home_dir, filename)
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return file.read().strip()
    return None

# Set up argument parser
parser = argparse.ArgumentParser(description="Unofficial Picarta Client")
parser.add_argument("--api_token", type=str, help="API Token for Picarta")
parser.add_argument("--img_path", type=str, help="Path to the image file")
parser.add_argument("--update_token", action="store_true", help="Update the stored API Token")
parser.add_argument("--top_k", type=int, default=3, help="Number of top predictions to return")
parser.add_argument("--center_latitude", type=float, help="Center latitude for location search")
parser.add_argument("--center_longitude", type=float, help="Center longitude for location search")
parser.add_argument("--radius", type=int, help="Radius for location search in kilometers")

# Parse arguments
args = parser.parse_args()

# Check if the user wants to update the API token
if args.update_token:
    api_token = input("Enter new API Token: ")
    save_api_token(api_token)
    print("API Token updated.")
else:
    api_token = args.api_token or read_api_token()
    if not api_token:
        api_token = input("API Token: ")
        save_api_token(api_token)

img_path = args.img_path or input("URL/Path to image file: ")

# Convert relative path to absolute path
if not (img_path.startswith("http://") or img_path.startswith("https://")):
    img_path = os.path.abspath(img_path)
    print(f"\nAbsolute path to image: {img_path}")

# Check if the file exists
if not os.path.exists(img_path):
    print(f"Error: File not found at {img_path}")
    exit(1)

# Check file permissions
if not os.access(img_path, os.R_OK):
    print(f"Error: No read permissions for file at {img_path}")
    exit(1)

# Check file size
file_size = os.path.getsize(img_path)
print(f"File size: {file_size} bytes")

localizer = Picarta(api_token)
print("API Token submitted")

# Geolocate the image
result = localizer.localize(
    img_path=img_path,
    top_k=args.top_k,
    center_latitude=args.center_latitude,
    center_longitude=args.center_longitude,
    radius=args.radius
)

# Pretty print the result
def pretty_print(result):
    print("\nResult(s):\n")

    # Print EXIF data if available
    if 'exif_lat' in result:
        print(f"EXIF Latitude: {result['exif_lat']}")
    if 'exif_lon' in result:
        print(f"EXIF Longitude: {result['exif_lon']}")
    if 'exif_country' in result:
        print(f"EXIF Country: {result['exif_country']}")

    for key, value in result['topk_predictions_dict'].items():
        print(f"Prediction {key}:")
        print(f"  City: {value['address']['city']}")
        print(f"  Country: {value['address']['country']}")
        print(f"  Province: {value['address']['province']}")
        print(f"  Confidence: {value['confidence'] * 100:.2f}%")
        print(f"  GPS: {value['gps']}")
        print()

pretty_print(result)

# Display the pricing link
print("\nFor more information on Picarta pricing, visit: https://picarta.ai/pricing")

