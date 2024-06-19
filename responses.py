from random import choice

def get_response(user_input):
    lowered = user_input.lower()

    if lowered == "":
        return "well, you\'re awfully silent..."
    elif "hello" in lowered:
        return "Hello there!"
    elif "hamsy" in lowered:
        return "Muie!"
    else:
        return choice([
            "I don\'t understand...",
            "What are you talking about?",
            "Do you mind rephrasing that?"
        ])