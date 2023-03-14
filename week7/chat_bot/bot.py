import random

program_name = 'Chat Bot Program'

def generate_computer_response():
    return random.choice([
        'That\'s very interesting. Tell me more?',
        'Really? How did that happen?',
        'Why do you think that is?',
        'No way! And then what?',
        'What makes you say that?',
        'How did you come to that conclusion?',
        'Can you elaborate on that?',
        'I\'d like to hear more about it?',
        'Please tell me more.',
        'So how did you feel about that?',
        'What will you do next?'
    ])