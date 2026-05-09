from transformers import AutoTokenizer, AutoModelForQuestionAnswering, pipeline
import pandas as pd

# Load your datasets
faq_data = pd.read_csv("data/faq_data.csv")
train_data = pd.read_csv("data/train.csv")
all_data = pd.concat([faq_data, train_data])

# Load tokenizer + PyTorch model
tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-distilled-squad")
model = AutoModelForQuestionAnswering.from_pretrained("distilbert-base-uncased-distilled-squad")

# Classic text QA pipeline
qa_pipeline = pipeline("question-answering", model=model, tokenizer=tokenizer)

def get_answer(question):
    # Find exact match in Question column
    matches = all_data[all_data["Question"].str.contains(question, case=False, na=False)]
    
    if matches.empty:
        return "Sorry, I couldn't find an answer in the FAQ dataset."
    
    # Return the full Answer text from the CSV
    return " ".join(matches["Answer"].astype(str).tolist())

