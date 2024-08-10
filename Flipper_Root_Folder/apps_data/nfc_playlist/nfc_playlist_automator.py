import os
import argparse


def generate_nfc_playlists(script_dir, output_name="NFC_Playlists.txt"):
    """
    Generate NFC playlists by walking through all subdirectories and files starting from the given script directory.

    Args:
        script_dir (str): The directory to start walking from.
        output_name (str, optional): The name of the output file. Defaults to "NFC_Playlists.txt".

    Returns:
        None

    Raises:
        ValueError: If there is an error constructing the relative path.

    This function generates NFC playlists by walking through all subdirectories and files starting from the given script directory.
    It uses the provided output file name or defaults to "NFC_Playlists.txt". It opens the output file in append mode and writes
    the modified path to the output file for each .nfc file found. The modified path is constructed by appending '/ext/nfc/' to the
    beginning of the relative path.
    """
    # Use the provided output file name or default to "NFC_Playlists.txt"
    output_file = output_name

    # Open the output file in append mode
    with open(output_file, 'a') as f:
        # Walk through all subdirectories and files starting from script_dir
        for root, dirs, files in os.walk(script_dir):
            for file in files:
                # Check if the file extension is .nfc
                if file.endswith('.nfc'):
                    # Construct the relative path from script_dir to the current file
                    try:
                        relative_path = os.path.relpath(os.path.join(str(root), str(file)), str(script_dir))
                    except ValueError as e:
                        print(f"Error: {e}")
                        break
                    # Append '/ext/nfc/' to the beginning of the relative path
                    nfc_playlist_path = f"/ext/nfc/{relative_path}"

                    # Write the modified path to the output file
                    f.write(nfc_playlist_path + '\n')


if __name__ == "__main__":
    # Set up argument parser
    print("Welcome to the NFC Playlist Generator!")
    print("Made for the Flipper Zero NFC Playlist Application.")
    print("Automates the generation of NFC playlists for Flipper Zero.")
    parser = argparse.ArgumentParser(description="Generate NFC playlists.")
    parser.add_argument("--name", type=str, help="Specify the name of the output file.", default="NFC_Playlists.txt")

    # Parse arguments
    args = parser.parse_args()

    # Assuming the script is located in C:\Users\Hp\Desktop\nfc
    script_dir = os.path.dirname(os.path.abspath(__file__))
    generate_nfc_playlists(script_dir, args.name)
