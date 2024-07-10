# Transcription App

This is a simple transcription application that converts audio files in `.m4a` format to text using the Google Web Speech API. The application first converts the `.m4a` file to `.wav` format for compatibility with the speech recognition library, and then transcribes the audio content to text.

## Directory Structure

src/
    app/
        transcribe.py
        media/
            voice001.m4a


## Requirements

- Python 3.6+
- `pydub` library
- `speech_recognition` library
- `ffmpeg` (for audio format conversion)

## Setup

1. **Clone the Repository**
    ```sh
    git clone <repository-url>
    cd <repository-name>
    ```

2. **Create a Virtual Environment**
    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Install ffmpeg**
    - On Debian/Ubuntu:
        ```sh
        sudo apt-get install ffmpeg
        ```
    - On MacOS (using Homebrew):
        ```sh
        brew install ffmpeg
        ```

## Usage

1. **Ensure your directory structure is as follows:**
    ```
    src/
        app/
            transcribe.py
        media/
            voice001.m4a
    ```

2. **Navigate to the `app` directory:**
    ```sh
    cd src/app
    ```

3. **Run the transcription script:**
    ```sh
    python transcribe.py
    ```

4. **Check the output**
    - The transcribed text will be printed in the console.
    - The transcribed text will be saved in `media/transcription.txt`.

## File Description

- **transcribe.py:** The main script for converting and transcribing the audio file.
- **voice001.m4a:** Sample audio file to be transcribed. Place your own `.m4a` files here.

## Script Explanation

- **Script Directory:** The script gets its current directory to correctly handle relative paths.
- **Audio Path:** The path to the `.m4a` file is computed relative to the script directory.
- **File Existence Check:** The script checks if the audio file exists at the specified path before proceeding.
- **Conversion:** The script converts the `.m4a` file to `.wav` using `pydub`.
- **Recognition:** The script uses the `speech_recognition` library to transcribe the audio content to text using the Google Web Speech API.
- **Output:** The transcribed text is printed and saved to a file.

## Troubleshooting

- Ensure the file `voice001.m4a` is present in the `media` directory and is named exactly as specified.
- Verify that `ffmpeg` is installed and accessible from your command line.
- Check the permissions of your audio file to ensure it is readable.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please create a pull request or submit an issue for any improvements or bug fixes.

