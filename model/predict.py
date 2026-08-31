import pandas as pd 
import pickle   

with open("model/model.pkl", 'rb') as f:
    model = pickle.load(f)

MODEL_VERSION  = '1.0.0'

class_labels = model.classes_.tolist() 





def predict_output(input_dict : dict):

    df = pd.DataFrame([input_dict])
    predicted_class = model.predict(df)[0] 
    probabilities = model.predict_proba(df)[0]  
    confidence = max(probabilities)

    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }
     