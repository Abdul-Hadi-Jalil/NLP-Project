from flask import Flask, request, jsonify
import os
from werkzeug.utils import secure_filename
from AIFile import doc_summary1, sentiment_analysis, lang_detector, lang_translation  # Importing AI functions

app = Flask(__name__)

# Set the folder for file uploads
app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'docx'}  # Modify as necessary

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Function to check file extensions
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Helper function to handle file saving
def handle_file_upload():
    if 'file' not in request.files:
        return None, 'No file part in request', 400
    file = request.files['file']
    if file.filename == '':
        return None, 'No selected file', 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return file_path, None, 200
    else:
        return None, 'Invalid file type', 400

@app.route('/summarizer', methods=['POST'])
def summarizer():
    file_path, error_message, status_code = handle_file_upload()
    
    if error_message:
        return jsonify({'error': error_message}), status_code

    try:
        # Generate the summary using the textrank_summarizer function
        generated_summary = doc_summary1.textrank_summarizer(file_path, top_n=3)
        return jsonify({'summary': generated_summary}), 200
    except Exception as e:
        return jsonify({'error': f'Error generating summary: {str(e)}'}), 500

@app.route('/sentiment', methods=['POST'])
def sentiment_analysis_route():
    file_path, error_message, status_code = handle_file_upload()
    
    if error_message:
        return jsonify({'error': error_message}), status_code

    try:
        # Perform sentiment analysis on the file's content
        results = sentiment_analysis.sentiment_analysis(file_path)
        return jsonify({'sentiment_results': results}), 200
    except Exception as e:
        return jsonify({'error': f'Error performing sentiment analysis: {str(e)}'}), 500

@app.route('/translation', methods=['POST'])
def language_translation():
    # Handle file upload
    file_path, error_message, status_code = handle_file_upload()

    if error_message:
        return jsonify({'error': error_message}), status_code

    # Retrieve source and target languages from the request
    src_lang = request.form.get('src_lang', None)  # None indicates auto-detection for source language
    tgt_lang = request.form.get('tgt_lang', 'ur')  # Default target language is Urdu ('ur')

    try:
        # Read the uploaded file
        with open(file_path, 'r') as f:
            file_text = f.read()

        if not src_lang:
            src_lang = lang_detector.detect_language(text=file_text)

        # Call translation function
        results = lang_translation.translate_text(text=file_text, src_lang=src_lang, tgt_lang=tgt_lang)

        return jsonify({
            'translation_results': results,
            'source_language': src_lang or 'auto-detected',  # Show 'auto-detected' if src_lang is None
            'target_language': tgt_lang
        }), 200
    except Exception as e:
        return jsonify({'error': f'Error performing translation: {str(e)}'}), 500

@app.route('/detector', methods=['POST'])
def language_detector_route():
    file_path, error_message, status_code = handle_file_upload()

    if error_message:
        return jsonify({'error': error_message}), status_code
    
    try:
        with open(file_path, 'r') as f:
            file_text = f.read()
        results = lang_detector.detect_language(text=file_text)
        return jsonify({'language_detection_result': results}), 200
    except Exception as e:
        return jsonify({'error': f'Error detecting language: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
