import tkinter as tk
from tkinter import filedialog
import re
import ast


def select_file():
    global file_path, filename, sentences, current_sentence, text_box,train_data,visual_list
    train_data.clear()
    file_path = filedialog.askopenfilename()
    filename =  file_path.split('/')[len(file_path.split('/'))-1]
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        # pretraitement regex pour ajouter un espace après un point suivit d'un charater
        content = re.sub(r'(?<=[.])(?=[\[ \n])', r' ', content)
        content = re.sub(r'\[[^\]]+\]', '', content)
        sentences = content.split(". ")
        sentences = [s.strip() for s in sentences if s.strip()]
    current_sentence = 0
    root.title(f"Seed Marker {filename}")
    show_sentence()
    try:
        train_data=load_data()
    except FileNotFoundError:
        return
    show_data()
   

def prev_sentence():
    global current_sentence, sentences, text_box
    if current_sentence > 0:
        current_sentence -= 1
        show_sentence()
        show_data()


def next_sentence():
    global current_sentence, sentences, text_box
    if current_sentence < len(sentences) - 1:
        current_sentence += 1
        show_sentence()
        show_data()


def show_sentence():
    global current_sentence, sentences, text_box,sentence,train_data
    sentence = sentences[current_sentence]
    text_box.delete('1.0', tk.END)
    text_box.insert(tk.END, sentence)
    visual_list.clear()
    affichage["text"]=""
    show_data()

def sentence_in_data ():
    global sentence,train_data
    for i in range (len(train_data)):
        if train_data[i][0]==sentence:
            return i
    return -1
    
def Mark_Seed(x):
    global sentence,train_data,visual_list
    try :# presence of selected object
        word = text_box.get(tk.SEL_FIRST, tk.SEL_LAST)
    except tk.TclError:
        return
    seed = button_Mark_Seed[x]["text"]
    first  = text_box.count("1.0", "sel.first")
    
    try:#creating tuple
        tuple = (first[0],first[0]+len(word),seed)
    except TypeError:
        tuple = (0,len(word),seed)
    visual_list.append((word,seed))
    affichage['text']=f"{visual_list}"
    text_box.tag_add(x, "sel.first", "sel.last")
    position = sentence_in_data()
    with open(f"training/{filename}","w",encoding="utf-8") as output: #saving data
        if len(train_data) == 0 or position ==-1: #no data or sentence not in the training data
            train_data.append((sentence,[tuple]))
            output.write(str(train_data))
        elif position!=-1:# sentence in training data
            if tuple not in train_data[position][1]:
                train_data[position][1].append(tuple)
            output.write(str(train_data))  

def load_data():
    with open(f"training/{filename}","r",encoding="utf-8") as local:
        data=local.readline()
        data= ast.literal_eval(data)
        return data

def show_data():
    global train_data
    position=sentence_in_data()
    if position !=-1:
        for start, end, tag in train_data[position][1]:
            text_box.tag_add(tag, f'1.{start}',f'1.{end}')



# create the main window and GUI elements
root = tk.Tk()
root.title("Seed Marker")
current_sentence = 0
sentences = []
file_path = ""
filename = ""
train_data=[]
visual_list=[]
button_Mark_Seed=[]
seed={
    0 :{"color":"#F3F4ED"},
    1 :{"color":"#F28482"},
    2 :{"color":"#96BB7C"},
    3 :{"color":"#76b5c5"},
    4 :{"color":"#abdbe3"},
    5 :{"color":"#D6EFC7"},
    6 :{"color":"#F5CAC3"},
    7 :{"color":"#7D1F35","foreground":"white"},
    8 :{"color":"#158467", "foreground":"white"},
    9 :{"color":"#22577A","foreground":"white"},
}

# create Frames

frame = tk.Frame(root)
frame_choix =tk.Frame(root)
frame_bar=tk.Frame(root)

# create Elements

#button_save = tk.Button(frame,text='enregistrer',command=Save, bg='brown', fg='white')
#button_save.grid(row=0,column=0,padx=10)
button_select_file = tk.Button(root, text="Choisir un fichier", command=select_file, bg='grey', fg='white')
button_select_file.pack(pady=5)
text_box = tk.Text(root, width=80, height=10)

button_back = tk.Button(frame_bar, text="Précédent", command=prev_sentence, bg='grey', fg='white')
button_back.grid(row=0,column=0,padx=10)
button_next = tk.Button(frame_bar, text="Suivant", command=next_sentence, bg='grey', fg='white')
button_next.grid(row=0,column=2,padx=10)
text_comm = tk.Entry(frame_bar, width=40)
text_comm.grid(row=0,column=1)

for x in range (len(seed)):
    try:
        button_Mark_Seed.append ( tk.Button(frame_choix, text=f"{x}",bg=seed[x]['color'],fg=seed[x]['foreground'], command= lambda a = x:Mark_Seed(a)))
    except KeyError:
        button_Mark_Seed.append ( tk.Button(frame_choix, text=f"{x}",bg=seed[x]['color'], command= lambda a = x:Mark_Seed(a)))
    button_Mark_Seed[x].grid(row=0,column=x,padx=10)


affichage = tk.Label (root,text="")


# pack the GUI elements

text_box.pack()
frame_bar.pack(expand=True,pady=5)
frame_choix.pack(expand=True)
affichage.pack(pady=5)


# configure text tags

for x in range(len(seed)):
    try: 
        text_box.tag_configure(f"{x}",background=f"{seed[x]['color']}",foreground=seed[x]["foreground"])
    except KeyError:
        text_box.tag_configure(f"{x}",background=f"{seed[x]['color']}")


root.mainloop()
