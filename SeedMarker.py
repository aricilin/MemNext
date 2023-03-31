import tkinter as tk
from tkinter import filedialog
import tkinter.scrolledtext as st
import re
import ast
import nltk

def select_file():
    global file_path, filename, sentences, current_sentence, text_box,train_data,visual_list,last_filepath
    train_data.clear()
    
    file_path = filedialog.askopenfilename()
    filename =  file_path.split('/')[len(file_path.split('/'))-1]
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            last_filepath=file_path
            content = f.read()
            # pretraitement regex pour ajouter un espace après un point suivit d'un charater
            content = re.sub(r'(?<=[.])(?=[\[ \n])', r' ', content)
            content = re.sub(r'\[[^\]]+\]', '', content)
            sentences = nltk.sent_tokenize(content)    
            """ sentences = content.split(". ")
            sentences = [s.strip() for s in sentences if s.strip()] """
    except FileNotFoundError:
            file_path=last_filepath
            filename =file_path.split('/')[len(file_path.split('/'))-1]
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                # pretraitement regex pour ajouter un espace après un point suivit d'un charater
                content = re.sub(r'(?<=[.])(?=[\[ \n])', r' ', content)
                content = re.sub(r'\[[^\]]+\]', '', content)
                sentences = nltk.sent_tokenize(content)
                """ sentences = content.split(". ")
                sentences = [s.strip() for s in sentences if s.strip()] """
    except PermissionError:
        file_path=last_filepath
        filename =file_path.split('/')[len(file_path.split('/'))-1]

        with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                # pretraitement regex pour ajouter un espace après un point suivit d'un charater
                content = re.sub(r'(?<=[.])(?=[\[ \n])', r' ', content)
                content = re.sub(r'\[[^\]]+\]', '', content)
                sentences = nltk.sent_tokenize(content)
                """ sentences = content.split(". ")
                sentences = [s.strip() for s in sentences if s.strip()] """

    current_sentence = 0
    root.title(f"Seed Marker {filename}")
    show_sentence()
    try:
        train_data=load_data()
    except FileNotFoundError:
        return
    except SyntaxError:
        return
    show_data()
   

def prev_sentence():#show the previous sentence
    global current_sentence, sentences, text_box
    if current_sentence > 0:
        current_sentence -= 1
        show_sentence()
        show_data()


def next_sentence():#show the next sentence
    global current_sentence, sentences, text_box
    if current_sentence < len(sentences) - 1:
        current_sentence += 1
        show_sentence()
        show_data()


def show_sentence():#print the sentence in the text_box
    global current_sentence, sentences, text_box,sentence,train_data
    sentence = sentences[current_sentence]
    text_box.delete('1.0', tk.END)
    text_box.insert(tk.END, sentence)
    visual_list.clear()
    

def sentence_in_data ():#return the position of the sentence in the saved data or -1
    global sentence,train_data
    for i in range (len(train_data)):
        if train_data[i][0]==sentence:
            return i
    return -1
    
def Mark_Seed(x):#tag the seed in the text and saved it in the files
    global sentence,train_data,visual_list
    

    try :# presence of selected object
        word = text_box.get(tk.SEL_FIRST, tk.SEL_LAST)
        first  = text_box.count("1.0", "sel.first")
        text_box.tag_add(x, "sel.first", "sel.last")
        last =text_box.index("sel.last")
        first = first[0]
    except TypeError:
        word = text_box.get(1.0, tk.SEL_LAST)
        first  = text_box.count("1.0", "sel.first")
        text_box.tag_add(x, "sel.first", "sel.last")
        last =text_box.index("sel.last")
        first = first[0]
    except tk.TclError:# one click selection with insert position 
        word = text_box.get("insert wordstart", "insert wordend")
        first = (int(text_box.index("insert wordstart").split('.')[1]))
        last = text_box.index("insert wordend")

    seed = button_Mark_Seed[x]["text"]
    position = sentence_in_data()
    visual_list.append((word,seed))
    seed_nb[int(x)]['text']+=1
    nb=0
    if position!=-1:#correction of offset positions by suppr button
        for i in (train_data[position][1]):
            
            if i[1]<first:
                nb+=1
    try:#creating tuple
        tuple = (first-nb,first-nb+len(word),seed)
    except TypeError:#error dist first char of text with selection
        tuple = (0,len(word),seed)
    with open(f"training/{filename}","w",encoding="utf-8") as output: #saving data
        if len(train_data) == 0 or position ==-1: #no data or sentence not in the training data
            train_data.append((sentence,[tuple]))
            output.write(str(train_data))
        elif position!=-1:# sentence in training data
            if tuple not in train_data[position][1]:
                train_data[position][1].append(tuple)
            output.write(str(train_data))
    text_box.window_create(last, window = tk.Button(text_box, text="x",command= lambda :suppr(tuple)))  
    show_sentence()
    show_data()
    

def load_data():
    with open(f"training/{filename}","r",encoding="utf-8") as local:
        data=local.readline()
        data= ast.literal_eval(data)
        return data

def show_data():#highlight the text with the saved data
    global button_suppr_list,train_data
    for i in range (len(seed_nb)):
        seed_nb[i]['text']=0
    position = sentence_in_data()
    if position !=-1:
        
        for start, end, tag in train_data[position][1]:
            nb=0
            if position!=-1:#correction of offset positions by suppr button
                
                for i in (train_data[position][1]):
                    if (start==i[0] and end==i[1]):
                        break
                    if i[1]<start:
                        nb+=1
            text_box.tag_add(tag, f'1.{start+nb}',f'1.{end+nb}')
            tuple = (start,end,str(tag))
            button_suppr_list.append(text_box.window_create(text_box.index(f'1.{end+nb}'), window = tk.Button(text_box, text="x",command= lambda x=tuple :suppr(x))))
            seed_nb[int(tag)]['text']+=1

def suppr(tuple):
    global sentence,train_data
    position=sentence_in_data()
    #print(f'{position} \n {tuple}') 
    train_data[position][1].remove(tuple)
    with open(f"training/{filename}","w",encoding="utf-8") as output: #saving data
        output.write(str(train_data))
    show_sentence()
    show_data()



def open_popup():#deletion window
   def delete():
    global train_data
    position= sentence_in_data()
    train_data.pop(position)
    top.destroy()
    show_sentence()
    show_data()
    with open(f"training/{filename}","w",encoding="utf-8") as output: #saving data
        output.write(str(train_data))
   top= tk.Toplevel(root)
   top.geometry("750x250")
   top.title("confirmation")
   tk.Label(top,font=('Helvetica 14 bold'), text= "Voulez vraiment effacer les graines de la page actuelle ?").pack()
   tk.Button(top,text="Annuler",command=top.destroy,bg="blue",fg="white").place_configure(x=150,y=80,width=200,height=100)
   tk.Button(top,text="Supprimer",command=delete,bg="red",fg="white").place_configure(x=450,y=80,width=200,height=100)




# create the main window and GUI elements
root = tk.Tk()
root.title("Seed Marker")
current_sentence=0
sentences = []
file_path = ""
filename = ""
train_data=[]
visual_list=[]
button_suppr_list=[]
button_Mark_Seed=[]
seeds={
    0 :{"color":"#F3F4ED"},
    1 :{"color":"#F28482"},
    2 :{"color":"#96BB7C"},
    3 :{"color":"#76b5c5"},
    4 :{"color":"#abdbe3"},
    5 :{"color":"#D6EFC7"},
    6 :{"color":"#F5CAC3"},
    7 :{"color":"#7D1F35","foreground":"white"},
    8 :{"color":"#158467","foreground":"white"},
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

text_box = st.ScrolledText(root,wrap="word", width=80, height=15)



button_back = tk.Button(frame_bar, text="Précédent", command=prev_sentence, bg='grey', fg='white')
button_back.grid(row=0,column=0,padx=10)
button_next = tk.Button(frame_bar, text="Suivant", command=next_sentence, bg='grey', fg='white')
button_next.grid(row=0,column=2,padx=10)
text_comm = tk.Entry(frame_bar, width=40)
text_comm.grid(row=0,column=1)

for x in range (len(seeds)):
    try:
        button_Mark_Seed.append ( tk.Button(frame_choix, text=f"{x}",bg=seeds[x]['color'],fg=seeds[x]['foreground'], command= lambda  a=x:Mark_Seed(a)))
    except KeyError:
        button_Mark_Seed.append ( tk.Button(frame_choix, text=f"{x}",bg=seeds[x]['color'], command= lambda a=x:Mark_Seed(a)))
    button_Mark_Seed[x].grid(row=1,column=x,padx=10)
    button_Mark_Seed[x].config(width=3)

seed_nb=[]
for x in range(len(seeds)):
    seed_nb.append(tk.Label(frame_choix,text=0))
    seed_nb[x].grid(row=0,column=x,padx=10)

affichage = tk.Label (root,text="")
delete_button = tk.Button(root,bg="red",text="effacer la page",command=open_popup)



# pack the GUI elements
frame_choix.pack(expand=True)
text_box.pack()
frame_bar.pack(expand=True,pady=5)
affichage.pack(pady=5)
delete_button.pack()


# configure text tags

for x in range(len(seeds)):
    try: 
        text_box.tag_configure(f"{x}",background=f"{seeds[x]['color']}",foreground=seeds[x]["foreground"])
    except KeyError:
        text_box.tag_configure(f"{x}",background=f"{seeds[x]['color']}")


root.mainloop()
