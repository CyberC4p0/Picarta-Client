# Unofficial Picarta Client

This is a command-line tool for interacting with the Picarta API to localize images. The tool allows you to provide an API token and an image file path/url to get localization results. The API token can be saved for future use, and you can update it at any time.

For quota & pricing inquiries, please visit: [Picarta Pricing](https://picarta.ai/pricing)

## Features

- Localize images using the Picarta API
- Display results in a readable format
- Provide command-line arguments for flexibility

## Requirements

- Python 3.x
- Picarta Python package

## Installation

1. Clone the repository or download the script.
2. Install the required Python package:
    ```sh
    pip install picarta
    ```

## Usage

### Command-Line Arguments

You can provide the API token and image file path/url as command-line arguments:

```sh
python main.py --api_token your_api_token --img_path /path/to/image.jpg
```

### Argument Parser Setup
The script uses an argument parser to handle various command-line arguments. Below are the available arguments and their descriptions:

* `--api_token`: API Token for Picarta.
* `--img_path`: OS Path or URL to the image file.
* `--update_token`: Update the stored API Token.
* `--top_k`: Number of top predictions to return (default is 3).
* `--center_latitude`: Center latitude for location search.
* `--center_longitude`: Center longitude for location search.
* `--radius`: Radius for location search in kilometers.

### Example Output
The results will be displayed in a readable format, including AI confidence, country, latitude, longitude, city, province, and top predictions.
```
Absolute path to image: C:\path\to\image\file.jpg
File size: 35957 bytes
API Token submitted

Result(s):

Prediction 1:
  City: Stafford
  Country: United States
  Province: Oregon
  Confidence: 93.61%
  GPS: [45.375286, -122.70602]

Prediction 2:
  City: View Park-Windsor Hills
  Country: United States
  Province: California
  Confidence: 93.31%
  GPS: [33.99668, -118.32776]

Prediction 3:
  City: Sueca
  Country: Spain
  Province: Valencia
  Confidence: 93.04%
  GPS: [39.216743, -0.301651]


For more information on Picarta pricing, visit: https://picarta.ai/pricing
```

### Printing EXIF Data
If the image contains EXIF data, you can print the latitude, longitude, and country information. The script will check for the presence of EXIF data and print it if available.
```py
# Print EXIF data if available
if 'exif_lat' in result:
    print(f"EXIF Latitude: {result['exif_lat']}")
if 'exif_lon' in result:
    print(f"EXIF Longitude: {result['exif_lon']}")
if 'exif_country' in result:
    print(f"EXIF Country: {result['exif_country']}")
```

## License
This project is licensed under the MIT License.

## Acknowledgements
[PicartaAI](https://github.com/PicartaAI) for providing the API
