# generator.py
import spacy
nlp = spacy.load("en_core_web_sm")

def preprocess_input(topic):
    doc = nlp(topic)
    return [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]

def generate_blog(topic):
    template_path = /data/title_generation.txt
    
    try:
        with open(template_path, 'r') as f:
            templates = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return "Template file not found."

    # Format each template with the provided topic
    titles = [template.format(topic=topic) for template in templates]
    
    # Numbered title list
    return "\n".join([f"{i+1}. {title}" for i, title in enumerate(titles)])