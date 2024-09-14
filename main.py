import argparse
from picarta import Picarta
import json
import os

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

localizer = Picarta(api_token)
print("API Token submitted")

result = localizer.localize(img_path=img_path)

# Pretty print the result
def pretty_print(result):
    print("\nResult:")
    print(f"AI Confidence: {result['ai_confidence'] * 100:.2f}%")
    print(f"AI Country: {result['ai_country']}")
    print(f"AI Latitude: {result['ai_lat']}")
    print(f"AI Longitude: {result['ai_lon']}")
    print(f"City: {result['city']}")
    print(f"Province: {result['province']}")
    print("\nTop Predictions:")
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
