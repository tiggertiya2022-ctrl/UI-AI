import os
import re
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pyttsx3

from aift import setting
setting.set_api_key('D3DsJCaRoXhwaW4Lik4cgYXC6kzFpRKm')
from aift.multimodal import textqa

# Initialize speech engine
engine = pyttsx3.init()

GUI = Tk()
GUI.title('โปรแกรมช่วยคิดเมนูอาหารวันนี้ by Tigger')
GUI.geometry('700x600')
GUI.state('zoomed')

# Get the folder of this script and image path
script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "galaxy.png")

# Try loading the background image
try:
    bg_photo = PhotoImage(file=image_path)
except Exception as e:
    messagebox.showerror("Image Load Error",
                         f"ไม่พบไฟล์ภาพพื้นหลัง:\n{image_path}\n\n{e}")
    bg_photo = None

# Place background label if image loaded
if bg_photo:
    bg_label = Label(GUI, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

style = ttk.Style()
style.configure('My.TButton', font=('TH Sarabun New', 24))

def format_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    return "\n".join(sentences)

def AIreply():
    user_text = v_input.get().strip()
    if not user_text:
        output_box.delete("1.0", END)
        output_box.insert(END, "กรุณาพิมพ์คำถามก่อน")
        return

    prompt = user_text  # no restriction, chat about anything

    result = textqa.generate(prompt)
    print("API result:", result)  # Debug: print full API response

    if 'content' in result:
        raw_text = result['content']
    else:
        # If 'content' key missing, show error message
        raw_text = "ขออภัย เกิดข้อผิดพลาดในการดึงข้อมูลจาก AI."
        if 'error' in result:
            raw_text += "\n" + str(result['error'])
        elif 'message' in result:
            raw_text += "\n" + str(result['message'])

    formatted_text = format_sentences(raw_text)

    output_box.delete("1.0", END)
    output_box.insert(END, formatted_text)

    # Speak the AI response
    engine.say(formatted_text)
    engine.runAndWait()

# Input field
v_input = StringVar()
E1 = ttk.Entry(GUI, textvariable=v_input, font=('TH Sarabun New', 24), width=30)
E1.place(relx=0.5, rely=0.05, anchor='n')

# Button
B1 = ttk.Button(GUI, text='ถาม AI', style='My.TButton', command=AIreply)
B1.place(relx=0.5, rely=0.15, anchor='n')

# Scrollable output box
frame = Frame(GUI, bg="black")
frame.place(relx=0.5, rely=0.25, relwidth=0.8, relheight=0.7, anchor='n')

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

output_box = Text(frame, font=('TH Sarabun New', 24), wrap=WORD,
                  yscrollcommand=scrollbar.set, bg="black", fg="white")
output_box.pack(expand=True, fill=BOTH)

scrollbar.config(command=output_box.yview)

GUI.mainloop()
