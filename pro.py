from tkinter import *
from tkinter import ttk
from googletrans import Translator
from googletrans import LANGUAGES

root = Tk()
root.title("Language Translator")
root.geometry("600x400")
root.configure(bg = "skyblue")

language = list(LANGUAGES.values())

label_heading = Label(root, text = "Language Translator", bg = "#fced95", font = ("Bell MT", 30, "bold"))
label_heading.place(relx = 0.5, rely = 0.1, anchor = CENTER)

input_label = Label(root, text = "Enter Text", bg = "#fced95", font = ("Bell MT", 17 , "bold"))
input_label.place(relx = 0.02, rely = 0.3, anchor = W)

d1 = ttk.Combobox(root, state = "readonly", values = language, width = 25)
d1.place(relx = 0.02, rely = 0.2, anchor = W)
d1.set("English")

input_text = Text(root, font = ("Bell MT", 15, "bold"), height = 6, wrap = WORD, width = 20, padx = 10, pady = 1, bd = 0)
input_text.place(relx = 0.02, rely = 0.55, anchor = W)

output_label = Label(root, text = "Output", bg = "#fced95", font = ("Bell MT", 20, "bold"))
output_label.place(relx = 0.98, rely = 0.3, anchor = E)

d2 = ttk.Combobox(root, state = "readonly", values = language, width = 25)
d2.place(relx = 0.98, rely = 0.2, anchor = E)
d2.set("Choose Output Language")

output_text = Text(root, font = ("Bell MT", 15, "bold"), height = 6, wrap = WORD, width = 20, padx = 10, pady = 1, bd = 0)
output_text.place(relx = 0.98, rely = 0.55, anchor = E)


def translate():
    source_lang = d1.get()
    dest_lang = d2.get()
    
    translator = Translator()
    
    try:
        translated = translator.translate(text = input_text.get(1.0, END), src = source_lang, dest = dest_lang)
        output_text.delete(1.0, END)
        output_text.insert(END, translated.text)
        
    except:
        print("Try Again")

translate_btn = Button(root, text = "Translate", command = translate, font = ("Bell MT", 15, "bold"), bg = "yellow", fg = "black", relief = FLAT, padx = 10, pady = 1)
translate_btn.place(relx = 0.5, rely = 0.8, anchor = CENTER)

root.mainloop()