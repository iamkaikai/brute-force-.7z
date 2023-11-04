# 7z Password Brute Forcer

This simple Python script attempts to brute-force the password of a `.7z` (7-Zip) file using a provided length for a numeric password.

## Installation

Before running the script, you need to ensure you have Python installed on your system. This script was developed with Python 3 in mind.

1. Clone this repository or download the script to your local machine.

2. Set up a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Unix or MacOS
venv\Scripts\activate.bat # On Windows
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

To run the script, you can use the terminal or command prompt:

```bash
python brute_force_7z.py
```

When prompted, enter the path to the `.7z` file and the length of the digit password (e.g., `4` for a 4-digit password).

The script will try all possible combinations for the given digit length and print each attempt. When the correct password is found, it will be displayed, and the contents of the archive will be extracted to the current directory.

## Notes

- This tool is intended to be used on `.7z` files for which you have forgotten the password. Using this script on files that you are not authorized to access is against the law.
- The brute-forcing process can be time-consuming, especially for longer passwords, as it tries every possible combination.

## License

[MIT License](LICENSE.txt)
