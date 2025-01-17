from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

def sentiment_analysis(file_path):
    with open(file_path, 'r') as file:
        document = file.read()

    model_name = "xlm-roberta-base"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)
    sentiment_pipeline = pipeline(task="sentiment-analysis", model=model, tokenizer=tokenizer)
    
    results = sentiment_pipeline(document)
    return results

def print_results(results):
    for result in results:
        label = result['label']
        score = result['score']
        if label == 'LABEL_0':  # Assuming 'LABEL_0' corresponds to 'Negative' 
            sentiment = "Negative"
        elif label == 'LABEL_1':  # Assuming 'LABEL_1' corresponds to 'Neutral'
            sentiment = "Neutral"
        else:  # Assuming 'LABEL_2' corresponds to 'Positive'
            sentiment = "Positive"
        print(f"Sentiment: {sentiment} (Score: {score:.2f})")

def main():
    file_path = r'sentiment.txt'
    results = sentiment_analysis(file_path)
    print_results(results)

if __name__ == "__main__":
    main()