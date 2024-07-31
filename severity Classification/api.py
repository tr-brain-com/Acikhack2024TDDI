from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import BertTokenizer
from simpletransformers.classification import ClassificationModel
import clean

app = FastAPI()

# Define label mapping
label_mapping = {
    0: "önemsiz",
    1: "az önemli",
    2: "çok önemli"
}

# Load the saved model
model_path = 'model'
model = ClassificationModel(
    'bert',
    model_path,
    num_labels=len(label_mapping),
    use_cuda=torch.cuda.is_available()
)

# Load the tokenizer
tokenizer = BertTokenizer.from_pretrained(model_path)

# Define request and response models
class RequestBody(BaseModel):
    text: str

class ResponseBody(BaseModel):
    sentiment: str

@app.post("/predict", response_model=ResponseBody)
async def predict(request_body: RequestBody):
    # Get and clean the incoming text
    #clean_input_text = clean_text(request_body.text)
    clean_input_text=clean.CLEANING(request_body.text,True, False,True).clean()

    # Tokenize the cleaned text
    inputs = tokenizer(
        clean_input_text,
        return_tensors='pt',
        truncation=True,
        padding=True,
        max_length=512
    )

    # Make sure we use the same device as the model
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.model.to(device)
    inputs = {key: value.to(device) for key, value in inputs.items()}

    # Make prediction
    outputs = model.model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=1).cpu().numpy()

    # Convert the predictions to human-readable labels
    sentiment = label_mapping[predictions[0]]

    return ResponseBody(sentiment=sentiment)
