import datetime
import webbrowser
import os
import pyjokes
import pygetwindow as gw
import pyautogui

def closed_tab(targets):
    for window in gw.getWindowsWithTitle("Chrome"):
        for target in targets:
            if target.lower() in window.title.lower():
                print(f"Closing: {window.title}")
                window.activate()
                pyautogui.hotkey('ctrl', 'w')  





def Action(message: str) -> str:
    msg = message.lower().strip()

    if  msg in ["your name","name","introduce"]:
        return "My name is Nexi, your virtual assistant. How can I help you today?"

    elif msg in ["hello", "hi", "hey","hii","hay","hye","namste"]:
        return "Hello there! How can I assist you today?"
    
    elif msg in ["how are you", "what about "]:
        return "I'm fine what about you!"
    

    elif "how's it going" in msg or "how is it going" in msg:
        return "It's going well, thank you! How about you?"
    
    
    elif "what's up" in msg or "whats up" in msg:
        return "Not much, just here to help you! What can I do for you?"
    
    elif "help" in msg:
        return "Sure! You can ask me about the weather, open websites like Google or YouTube, or just chat with me."
    elif "who are you" in msg:
        return "I am a AI voice assistant, here to help you with any questions or tasks you may have."

#  open work

    elif "open camera" in msg or "camera" in msg:
        os.system("start microsoft.windows.camera:")
        return "Camera opened"
    
    elif "open notepad" in msg or "notepad" in msg:
        os.system("notepad")
        return "Notepad opened"
    
#   
#     elif "current path" in data_btn or "path" in data_btn:
#        
#         return  f"Here is your current path {os.getcwd()}"
    
#     elif "set folder" in data_btn or "goto folder" in data_btn or "open folder" in data_btn:
#         path= os.getcwd()
#         try:
#             if "set folder" in data_btn:
#                 folder= data_btn.split('set folder')[1]
#                 os.chdir(f"{path} ")
#                 return 
#             elif "goto folder" in data_btn:
#                 folder= data_btn.split('goto folder')[1]
#                 return 
#             elif "open folder" in data_btn:
#                 folder= data_btn.split('open folder')[1]
#                 return 
#         except:
#             print("Unable to understand")    
#     elif data_btn.startswith("set folder"):
#         path = data_btn.replace("set folder", "").strip()
#         return set_folder(path)

#     elif "list files" in data_btn:
#         return list_files()

#     elif data_btn.startswith("open file"):
#         filename = data_btn.replace("open file", "").strip()
#         return open_file(filename)


# end work

    elif "how are you" in msg:
        return "I'm doing great, thanks for asking!"

    elif "thank you" in msg or "thanks" in msg:
        return "You're welcome!"

    elif "good morning" in msg:
        return "Good morning! I hope you have a great day ahead."
    
    elif "close youtube" in msg or "closed youtube" in msg :
        closed_tab("youtube")
        return "closing youtube!"
    
    elif "joke" in msg or "jokes" in msg :
        joke=pyjokes.get_joke(language="en",category="neutral")  
        return f"joke is:  {joke} hahaha"
    
    elif "play song" in msg or "song" in msg :
            add=r'C:\Users\vipin\OneDrive\Desktop\python\apython_notes'
            listsong=os.listdir(add) 
            os.startfile(os.path.join(add,listsong[0]))
            return f"playing song..."
    
    elif "close google" in msg or "closed google" in msg :
        closed_tab("google")
        return "closing google!"
    elif "close github" in msg or "closed github" in msg :
        closed_tab("github")
        return "closing github!"
    elif "close chatgpt" in msg or "closed chatgpt" in msg :
        closed_tab("chatgpt")
        return "closing chatgpt!"

    elif "time" in msg:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%H:%M')}."



    elif "open google" in msg:
        webbrowser.open("https://www.google.com")
        return "Opening Google for you."

    elif "open youtube" in msg or " open youtube" in msg:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube for you."

    elif "open github" in msg or "opens github" in msg:
        webbrowser.open("https://www.github.com")
        return "Opening GitHub for you."

    elif "open chatgpt" in msg or "open chatgpt" in msg:
        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT for you."

    elif "weather" in msg:
        webbrowser.open("https://www.google.com/search?q=weather")
        return "Here's the current weather forecast."

    else:
        return "I'm not sure how to help with that. Can you try asking something else?"
