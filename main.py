import tkinter as tk
#importing the sms.py file
import sms

#dummy variable for addressing the remaining no of tokens
remaining_tokens = 1

#dummy sequence to identify the phone numbers
sequence = ['+916238637381','+916238637381','+916238637381']


#function for looping through the phone numbers
def sms_send(remaining_tokens,token,phone_number1,phone_number2):
    #while the system is not empty
    while remaining_tokens != 0:
        #dummy range
        for i in range(0,3):
            #index imagined as their token numbers
            if i == token:
                new_text1 = sequence[i]
                #changing the label display
                phone_number1.config(text=new_text1)
                message_text="Your time will come shortly"
                recipient_number = sequence[i]
                #calling the sms function
                sms.send_sms(message_text, recipient_number)

                #cheching if there is a number left in sequence
                if sequence[i+1]:
                    new_text2 = sequence[i+1]
                    #changing the label display
                    phone_number2.config(text=new_text2)
                    message_text="Please reach the counter"
                    recipient_number = sequence[i+1]
                    #calling the sms function
                    sms.send_sms(message_text, recipient_number)
        #dummy decrementation for closing the loop       
        remaining_tokens = remaining_tokens-1


                
#tkinter gui function
def token_system():
    root = tk.Tk()
    root.title("Token System")

    frame = tk.Frame(root, padx=100, pady=100)
    frame.pack()

    label1 = tk.Label(frame, text="Phone number 1:")
    label1.grid(row=0, column=0, sticky="w")

    label2 = tk.Label(frame, text="Phone Number 2:")
    label2.grid(row=1, column=0, sticky="w")

    phone_number1 = tk.Label(frame, text="")
    phone_number1.grid(row=0, column=1, padx=10)

    phone_number2 = tk.Label(frame, text="")
    phone_number2.grid(row=1, column=1, padx=10)

    label3 = tk.Label(frame, text="Token No:")
    label3.grid(row=0, column=2, sticky="w")

    label4 = tk.Label(frame, text="Token No:")
    label4.grid(row=1, column=2, sticky="w")

    token_no1 = tk.Label(frame, text="01")
    token_no1.grid(row=0, column=3, sticky="w")
    
    token_no2 = tk.Label(frame, text="02")
    token_no2.grid(row=1, column=3, sticky="w")

    #dummy variable to represent the token number to be called
    token = 1

    #dummy variable
    remaining_tokens = 1
    
    #assigning the function to a variable
    starting_send = sms_send(remaining_tokens, token, phone_number1, phone_number2)

    button = tk.Button(frame, text="Call Next Token", command=starting_send)
    button.grid(row=2, column=1, sticky="w")

    root.mainloop()


if __name__ == "__main__":
    token_system()