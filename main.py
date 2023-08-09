import tkinter as tk
import sms

remaining_tokens = 1
sequence = ['+916238637381','916238637381','916238637381']

def sms_send(remaining_tokens,token,phone_number1,phone_number2):
    while remaining_tokens != 0:
        for i in sequence:
            if i == token:
                new_text1 = sequence[i]
                phone_number1.config(text=new_text1)
                sms.message_text="Your time will come shortly"
                sms.recipient_number = sequence[i]
                sms.send_sms()

                if sequence[i+1]:
                    new_text2 = sequence[i+1]
                    phone_number2.config(text=new_text2)
                    sms.message_text="Please reach the counter"
                    sms.recipient_number = sequence[i+1]
                    sms.send_sms()
                
                remaining_tokens = remaining_tokens-1


                

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

    token = 1
    remaining_tokens = 1
    
    starting_send = sms_send(remaining_tokens, token, phone_number1, phone_number2)

    button = tk.Button(frame, text="Call Next Token", command=starting_send)
    button.grid(row=2, column=1, sticky="w")
    button.pack()

    root.mainloop()


if __name__ == "__main__":
    token_system()