# Assistant-application
Console bot helper, recognizes the commands entered from the keyboard and responds according to the entered command.

Bot capabilities and commands:

- The bot is in an endless loop, waiting for a user command.
- The bot completes its work if it meets words.
- The bot is not case sensitive.
The bot accepts commands:

        - "hello", replies to the console "How can I help you?"
        
        - "add ...". With this command, the bot saves a new contact in memory (in the dictionary, for example). Instead of ... the - user enters the name and phone number, necessarily with a space.
        
        - "change ..." With this command, the bot stores the new phone number of the existing contact in memory. Instead of ... the user enters the name and phone number, necessarily with a space.
        
        - "phone ...." With this command, the bot outputs the phone number for the specified contact to the console. Instead of ... the user enters the name of the contact whose number should be displayed.
        
        - "show all". With this command, the bot outputs all saved contacts with phone numbers to the console.
        
        - "good bye", "close", "exit" by any of these commands, the bot ends its work after outputting "Good bye!" to the console.
