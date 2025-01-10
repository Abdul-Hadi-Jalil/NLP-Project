from langdetect import detect, detect_langs
import os

def detect_language(text: str = None, file = None):
    if file:
        with open(file, 'r') as f:
            lang = detect(f.read())
        return lang
    else:
        return detect(text=text)


def check_file_path(file_path: str):
    if not os.path.exists(file_path):
        return 'i'
    elif not os.path.isfile(file_path):
        return 'n'
    else:
        return 'y'


def main():
    
    file_path = input("Enter the file path: ")

    is_file = check_file_path(file_path)

    if is_file == 'i':
        print("Invalid path or file does not exist")
    elif is_file == 'n':
        print("The path is valid but it is not a file")
    else:
        lang = detect_language(file = file_path)
        print(f"The given file is in {lang}")
    

    
    def test_cases():
        print("### Testing Various Cases ###")

        # Test Case 1: Non-existent file
        file_path_1 = "non_existent_file.txt"
        print(f"\nTest Case 1: File path - {file_path_1}")
        is_file_1 = check_file_path(file_path_1)
        if is_file_1 == 'i':
            print("Output: Invalid path or file does not exist")
        else:
            print("Output: Test failed!")

        # Test Case 2: Valid file path with content in English
        file_path_2 = "test_english.txt"
        with open(file_path_2, 'w') as f:
            f.write("This is a test file with English content.")
        print(f"\nTest Case 2: File path - {file_path_2}")
        is_file_2 = check_file_path(file_path_2)
        if is_file_2 == 'y':
            lang_2 = detect_language(file=file_path_2)
            print(f"Output: Detected language is {lang_2}")
        else:
            print("Output: Test failed!")

        # Test Case 3: Valid file path with content in French
        file_path_3 = "test_french.txt"
        with open(file_path_3, 'w') as f:
            f.write("Ceci est un fichier de test avec du contenu en français.")
        print(f"\nTest Case 3: File path - {file_path_3}")
        is_file_3 = check_file_path(file_path_3)
        if is_file_3 == 'y':
            lang_3 = detect_language(file=file_path_3)
            print(f"Output: Detected language is {lang_3}")
        else:
            print("Output: Test failed!")

        # Test Case 4: Path to a directory
        dir_path = "test_directory"
        os.makedirs(dir_path, exist_ok=True)
        print(f"\nTest Case 4: Path - {dir_path}")
        is_file_4 = check_file_path(dir_path)
        if is_file_4 == 'n':
            print("Output: The path is valid but it is not a file")
        else:
            print("Output: Test failed!")

        # Test Case 5: Valid file path with content in Spanish
        file_path_5 = "test_spanish.txt"
        with open(file_path_5, 'w') as f:
            f.write("Este es un archivo de prueba con contenido en español.")
        print(f"\nTest Case 5: File path - {file_path_5}")
        is_file_5 = check_file_path(file_path_5)
        if is_file_5 == 'y':
            lang_5 = detect_language(file=file_path_5)
            print(f"Output: Detected language is {lang_5}")
        else:
            print("Output: Test failed!")

        # Cleanup
        os.remove(file_path_2)
        os.remove(file_path_3)
        os.remove(file_path_5)
        os.rmdir(dir_path)

    #test_cases()


if __name__=="__main__":
    main()