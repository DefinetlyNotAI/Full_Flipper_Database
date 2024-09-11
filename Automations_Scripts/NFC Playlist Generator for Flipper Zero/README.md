# NFC Playlists Generator

This Python script generates playlists for NFC (Near Field Communication) devices by scanning through directories for files with the `.nfc` extension and compiling their paths into a text file. This tool is particularly useful for organizing NFC playlists in a structured manner.

## Features

- Scans through directories recursively starting from a specified root directory.
- Identifies files with the `.nfc` extension.
- Generates a playlist file containing relative paths to the `.nfc` files, prefixed with `/ext/nfc/`.
- Allows specifying the output file name via command-line arguments.

## Requirements

- Python 3.x

## Usage

To generate NFC playlists, run the script from the command line. Optionally, you can specify the output file name using the `--name` flag.

```sh
python generate_nfc_playlists.py --name <output_file_name>.txt
```

Replace `<output_file_name>` with your desired output file name. If the `--name` flag is omitted, the default output file name is `NFC_Playlists.txt`.

The directory where the scan starts is where the script is located.
It auto fixes and appends required format for the `FAP` application itself.
The script has been tested

## Example

Assuming the script is located at `C:\Users\Hp\Desktop\nfc`, running:

```sh
python generate_nfc_playlists.py --name MyPlaylists.txt
```

will scan the directory `C:\Users\Hp\Desktop\nfc` and its subdirectories for `.nfc` files, generating `MyPlaylists.txt` containing the paths to these files.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues if you encounter any bugs or have feature suggestions.

## License

This project is licensed under the MIT License - see the [LICENSE](/LICENSE) file for details.

## Contact

Shahm Najeeb - Nirt_12023@outlook.com

Project link can be found [here](https://github.com/DefinetlyNotAI/Hack_Club/Mini_Python_Projects/NFC_Playlists_Generator_Flipper_Zero)
