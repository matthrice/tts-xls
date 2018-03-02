# Text to Speech using IBM Watson

## Input an excel sheet, output a collection of .wav files

### Getting started with synthesis

1. Clone the repository
2. run `$ pip3 install -r requirements.txt`
3. Open settings.json and change
    ```
    {
    ...
    "username": "Enter username from IBM credentials",
    "password": "Enter password from IBM credentials",
    ...
    }
    ```
4. run `$ python3 text_to_speech.py your_input_file.xls`
5. Look in new directory output_files for .wav files

Optional: to change default output directory:

6. run `$ python3 text_to_speech.py your_input_file.xls your_output_directory`

### Setup Notes

* Python 3 and Pip 3 must be installed
* Must have an IBM Bluemix account and it must have a registered TTS project
* If using the *lite* version, synthesis is capped at 10,000 characters
* Phrases to synthesize must be contained in the first column, but the first row should be used as a label, not content
* Input file must be in same directory as script

