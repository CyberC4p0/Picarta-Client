# Unofficial Picarta Client

This is a command-line tool for interacting with the Picarta API to localize images. The tool allows you to provide an API token and an image file path/url to get localization results. The API token can be saved for future use, and you can update it at any time.

For quota & pricing inquiries, please visit: [Picarta Pricing](https://picarta.ai/pricing)

## Features

- Localize images using the Picarta API
- Save and reuse API token
- Update API token when needed
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
OR
```sh
python main.py --api_token your_api_token --img_path https://i.postimg.cc/5NTGHCjn/IMG-0336.jpg
```
### Saving API Token
The first time you run the script, you will be prompted to enter your API token. The token will be saved in a file named `api_token.txt` in your home directory. You won’t need to enter the token again unless you choose to update it.

### Updating API Token
To update the stored API token, use the `--update_token` flag:
```
python main.py --update_token
```
### Running Without Arguments
If you run the script without command-line arguments, you will be prompted to enter the API token and image file path/url:
```
python main.py
API Token: your_api_token
Enter the path to the image file: /path/to/image.jpg
```
Example Output
The results will be displayed in a readable format, including AI confidence, country, latitude, longitude, city, province, and top predictions.
```
Result:
AI Confidence: 93.60%
AI Country: Turkey
AI Latitude: 41.03879
AI Longitude: 29.000744
City: Sisli
Province: Istanbul

Top Predictions:
Prediction 1:
  City: Sisli
  Country: Turkey
  Province: Istanbul
  Confidence: 93.60%
  GPS: [41.03879, 29.000744]

Prediction 2:
  City: Sisli
  Country: Turkey
  Province: Istanbul
  Confidence: 92.56%
  GPS: [41.038864, 29.00085]

...
```

## License
This project is licensed under the MIT License.

## Acknowledgements
[PicartaAI](https://github.com/PicartaAI) for providing the API
