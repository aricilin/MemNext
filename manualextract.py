import tkinter as tk
from tkinter import filedialog


def select_file():
    global file_path, filename, sentences, current_sentence, text_box,train_data,train_list,visual_list
    file_path = filedialog.askopenfilename()
    filename =  file_path.split('/')[len(file_path.split('/'))-1]
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        sentences = content.split(". ")
        sentences = [s.strip() for s in sentences if s.strip()]
    current_sentence = 0
    train_list.clear()
    visual_list.clear()
    train_data.clear()
    root.title(f"extraction manuelle {filename}")
    show_sentence()

def prev_sentence():
    global current_sentence, sentences, text_box
    if current_sentence > 0:
        current_sentence -= 1
        show_sentence()

def next_sentence():
    global current_sentence, sentences, text_box
    if current_sentence < len(sentences) - 1:
        current_sentence += 1
        show_sentence()

def show_sentence():
    global current_sentence, sentences, text_box,sentence,train_data
    sentence = sentences[current_sentence]
    text_box.delete('1.0', tk.END)
    text_box.insert(tk.END, sentence)
    train_list.clear()
    visual_list.clear()
    affichage["text"]=""
    

def add():
    global sentence, text_input, train_list,train_data,visual_list
    word = text_input.get().split(':')[0]
    seed=text_input.get().split(':')[1]
    position = sentence.find(word)
    train_list.append((position,position+len(word),seed))
    visual_list.append((word,seed))
    print (train_list)
    affichage['text']=f"{visual_list}"

def Fin():
    global train_data,train_list,sentence
    train_data.append((sentence,train_list))
    print (train_data)
    affichage['text']="page finie"

def Save():
    global filename, train_data,train_list,sentence
    with open(f"training/{filename}","w",encoding="utf-8") as output:
        if len(train_data)==0  :
            if len(train_list)==0:
                affichage["text"]="rien à enregistrer"
                return
            else:
                Fin()
        elif train_data[-1]!=(sentence,train_list):
            Fin()
        
        output.write(str(train_data))
        affichage["text"]="fichier enregistré"

# create the main window and GUI elements
root = tk.Tk()
root.title("extraction manuelle")
current_sentence = 0
sentences = []
file_path = ""
filename = ""
train_list=[]
train_data=[]
visual_list=[]

frame = tk.Frame(root)
frame_choix =tk.Frame(root)

button_select_file = tk.Button(frame, text="Select File", command=select_file).grid(row=0,column=1,padx=10)
text_box = tk.Text(root, width=80, height=10)
button_back = tk.Button(frame_choix, text="Previous", command=prev_sentence).grid(row=0,column=0,padx=10)
button_next = tk.Button(frame_choix, text="Next", command=next_sentence).grid(row=0,column=2,padx=10)
text_input = tk.Entry(root, width=80,textvariable="mot:seed")
button_add = tk.Button(frame_choix, text="Ajouter", command=add).grid(row=0,column=1,padx=10)
button_send = tk.Button(root,text="Fin page",command=Fin)
affichage = tk.Label (root,text="")
button_save = tk.Button(frame,text='enregistrer',command=Save).grid(row=0,column=0,padx=10)

# pack the GUI elements

frame.pack(expand=True)
text_box.pack()
text_input.pack()
frame_choix.pack(expand=True)
affichage.pack()
button_send.pack(padx=5, pady=5)



root.mainloop()
