#import bot, user_input

from bot import program_name, generate_computer_response
from user_input import ask_questions

print('Welcome to ' + program_name)

print('Type "STOP" to end.')

ask_questions('How was your day?')

while True:
    bot_response = generate_computer_response()
    respnse = ask_questions(bot_response)
    if respnse.upper() == 'STOP':
        break
    
print('Thanks for the interesting conversation!')