from transformers import MarianMTModel, MarianTokenizer

# Initialize tokenizer and model for translation
def get_translation_model(src_lang, tgt_lang):
    model_name = f'Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}'
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return tokenizer, model

# Translate text
def translate_text(text, src_lang, tgt_lang):
    try:
        tokenizer, model = get_translation_model(src_lang, tgt_lang)
        inputs = tokenizer.encode(text, return_tensors="pt", truncation=True)
        outputs = model.generate(inputs, max_length=512)
        translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return translated_text
    except Exception as e:
        return f"Error: {str(e)}"

# Read text from file
def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return None

# Main function
if __name__ == "__main__":
    print("Welcome to the File Translator!")

    # Get user inputs
    file_path = input("Enter the path to the text file: ").strip()
    source_language = input("Enter the source language code (e.g., 'ur' for Urdu, 'en' for English): ").strip()
    target_language = input("Enter the target language code (e.g., 'en' for English, 'fr' for French): ").strip()

    # Read text from file
    text = read_file(file_path)
    if text is None:
        print(f"Error: File '{file_path}' not found.")
    else:
        print(f"Translating text from {source_language} to {target_language}...")
        translated_text = translate_text(text, source_language, target_language)
        print("\n--- Original Text ---")
        print(text)
        print("\n--- Translated Text ---")
        print(translated_text)
