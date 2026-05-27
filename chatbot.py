from datetime import datetime as dt

# Greetting
crrnt_time = dt.now().hour
def greet():
    if crrnt_time < 12 :
        return("Good Morning!!")
    elif crrnt_time < 18:
        return("Good AfterNoon!!")
    elif crrnt_time > 18:
        return("Good Evening!!")

usr_name = input("Can you Enter Your-Name:").upper().strip()

WELCOME_TEXT=f"""
 Hi,(^_^)
 {greet()}{usr_name}
 I am a hardcode chatbot made by -ssannssarr
 Well even I am hardcoded I can talk to you.
 If you wanna leave just say Bye!
"""
print(WELCOME_TEXT)
