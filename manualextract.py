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
    root.title(f"Seed Marker {filename}")
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
    

def Mark_Seed(x):
    global sentence, text_input, train_list,train_data,visual_list
    word = text_box.get(tk.SEL_FIRST, tk.SEL_LAST)
    position = sentence.find(word)
    seed = button_Mark_Seed[x]["text"]
    train_list.append((position,position+len(word),seed))
    visual_list.append((word,seed))
    print (train_list)
    affichage['text']=f"{visual_list}"


def end():
    global train_data,train_list,sentence
    train_data.append((sentence,train_list))
    print (train_data)
    affichage['text']="page endie"

def Save():
    global filename, train_data,train_list,sentence
    with open(f"training/{filename}","w",encoding="utf-8") as output:
        if len(train_data)==0  :
            if len(train_list)==0:
                affichage["text"]="rien à enregistrer"
                return
            else:
                end()
        elif train_data[-1]!=(sentence,train_list):
            end()
        
        output.write(str(train_data))
        affichage["text"]="fichier enregistré"

# create the main window and GUI elements
root = tk.Tk()
root.title("Seed Marker")
current_sentence = 0
sentences = []
file_path = ""
filename = ""
train_list=[]
train_data=[]
visual_list=[]
button_Mark_Seed=[]

# create Frames

frame = tk.Frame(root)
frame_choix =tk.Frame(root)
frame_bar=tk.Frame(root)

# create Elements

button_save = tk.Button(frame,text='enregistrer',command=Save)
button_save.grid(row=0,column=0,padx=10)
button_select_file = tk.Button(frame, text="Choisir un fichier", command=select_file)
button_select_file.grid(row=0,column=1,padx=10)
text_box = tk.Text(root, width=80, height=10)

button_back = tk.Button(frame_bar, text="Précédent", command=prev_sentence)
button_back.grid(row=0,column=0,padx=10)
button_next = tk.Button(frame_bar, text="Suivant", command=next_sentence)
button_next.grid(row=0,column=2,padx=10)
text_input = tk.Entry(frame_bar, width=60,textvariable="mot:seed")
text_input.grid(row=0,column=1)

for x in range (10):
    
    button_Mark_Seed.append ( tk.Button(frame_choix, text=f"{x}", command= lambda a = x:Mark_Seed(a)))
    button_Mark_Seed[x].grid(row=0,column=x,padx=10)


affichage = tk.Label (root,text="")


# pack the GUI elements

frame.pack(expand=True,pady=5)
text_box.pack()
frame_bar.pack(expand=True,pady=5)
frame_choix.pack(expand=True)
affichage.pack()




root.mainloop()
