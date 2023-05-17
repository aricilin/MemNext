import tkinter as tk
from tkinter import filedialog
import tkinter.scrolledtext as st
import re
import ast
import nltk
import converter
# nltk.download('punkt')


def select_file():
    global file_path, filename, sentences, current_sentence, text_box, train_data, visual_list, last_filepath
    train_data.clear()

    
    file_path = converter.converter(filedialog.askopenfilename())

    if file_path == -1: # unkown format case
        text_box.delete('1.0', tk.END)
        text_box.insert("1.0"," Erreur : Format inconnu")
        return 
    
    
    elif file_path == 0: #cancel case
        if last_filepath == 0 :
            text_box.delete('1.0', tk.END)
            text_box.insert("1.0"," Cancel")
            return
        else :
            file_path = last_filepath
            
    filename = file_path.split('/')[len(file_path.split('/'))-1]
 
    with open(file_path, "r", encoding="utf-8") as f:
        last_filepath = file_path
        content = f.read()
        # pretraitement regex pour ajouter un espace après un point suivit d'un charater
        # content = re.sub(r'(?<=[.])(?=[\[ \n])', r' ', content)
        # content = re.sub(r'\[[^\]]+\]', '', content)
        # sentences = nltk.sent_tokenize(content)
        sentences = list(filter(lambda x : x != '', content.split('\n\n')))
        pagenb.configure(state='normal')
        pagenb.delete(1.0,"end")
        pagenb.insert(1.0,f"{len(sentences)}")
        pagenb.configure(state='disabled')
    current_sentence = 0
    root.title(f"Seed Marker {filename}")
    show_sentence()
    try:
        train_data = load_data()
    except FileNotFoundError:
        return
    except SyntaxError:
        return
    show_data()


def prev_sentence():  # show the previous sentence
    global current_sentence, sentences, text_box
    if current_sentence > 0:
        current_sentence -= 1
        show_sentence()
        show_data()


def next_sentence():  # show the next sentence
    global current_sentence, sentences, text_box
    if current_sentence < len(sentences) - 1:
        current_sentence += 1
        show_sentence()
        show_data()

def last_sentence():  # show the next sentence
    global current_sentence, sentences, text_box
    if current_sentence < len(sentences)-1:
        current_sentence =len(sentences) -1
        show_sentence()
        show_data()

def first_sentence():  # show the first sentence
    global current_sentence, sentences, text_box
    if current_sentence > 0:
        current_sentence =0
        show_sentence()
        show_data()

def show_sentence():  # print the sentence in the text_box
    global current_sentence, sentences, text_box, sentence, train_data
    text_box.configure(state='normal')
    sentence = sentences[current_sentence]
    text_box.delete('1.0', tk.END)
    text_box.insert(tk.END, sentence)
    visual_list.clear()
    text_box.configure(state='disabled')
    page.delete(1.0,"end")
    page.insert(1.0,f"{current_sentence+1}")
    



def sentence_in_data():  # return the position of the sentence in the saved data or -1
    global sentence, train_data
    for i in range(len(train_data)):
        if train_data[i][0] == sentence:
            return i
    return -1


def Mark_Seed(x):  # tag the seed in the text and saved it in the files
    global sentence, train_data, visual_list,lastseed

    try:  # presence of selected object
        # word = text_box.get(tk.SEL_FIRST, tk.SEL_LAST) # update needed if used

        first = text_box.count("1.0", "sel.first", "displayindices")[0]
        last = text_box.count("1.0", "sel.last", "displayindices")[0]
        # ugly while loops otherwise an indexerror happens
        #completion selection
    except TypeError:  # position 0
        # word = text_box.get(1.0, tk.SEL_LAST)
        first = 0
        last = text_box.count("1.0", "sel.last", "displayindices")[0]

    except tk.TclError:  # one click selection with insert position
        word = text_box.get("insert wordstart", "insert wordend")
        first = text_box.count("1.0", "insert wordstart", "displayindices")
        if first == None:
            first = 0
        else:
            first = first[0]
        last = text_box.count("1.0", "insert wordend", "displayindices")[0]
    vw = text_box.yview() # Save the current position(percentage) of the top left corner
    seed = button_Mark_Seed[x]["text"]
    position = sentence_in_data()
    # visual_list.append((word, seed))
    seed_nb[int(x)]['text'] += 1
    nb = 0
    if position != -1:  # correction of the offset position created by the suppr button
        train_data[position][1].sort(key=lambda tup: tup[0])#sorting data 
        for tuple in (train_data[position][1]):
            if tuple[1] < first-nb:
                nb += 1
    first -= nb
    last -= nb
    # auto completion + ugly loop or indexerror
    while(True):
        if sentence[last].isalpha() or sentence[last]=="-":
            last+=1
        else:
            break
    while(True):
        if (sentence[first-1].isalpha() or sentence[first-1]=="-") and sentence[first-2]!= "\\" :
            first-=1
        else:
            break
    tuple = (first, last, seed)
    lastseed=tuple
    with open(f"training/{filename}", "w", encoding="utf-8") as output:  # saving data
        if len(train_data) == 0 or position == -1:  # no data or sentence not in the training data
            train_data.append((sentence, [tuple]))
            output.write(str(train_data))
        elif position != -1:  # sentence in training data
            if tuple not in train_data[position][1]:
                train_data[position][1].append(tuple)
            output.write(str(train_data))
    show_sentence()
    show_data()
    text_box.yview_moveto(vw[0])


def load_data():
    with open(f"training/{filename}", "r", encoding="utf-8") as local:
        data = local.readline()
        data = ast.literal_eval(data)
        return data


def show_data():  # highlight the text with the saved data
    global button_suppr_list, train_data, sentence,lastseed
    text_box.configure(state='normal')
    for i in range(len(seed_nb)):
        seed_nb[i]['text'] = 0
    position = sentence_in_data()
    for i in range (len(train_data)):#position of the sentence in the data
        for infos in train_data[i][1]:
            seed_nb[int(infos[2])]['text'] += 1
    if position != -1:#if there is data saved
        for start, end, tag in train_data[position][1]:
            tuple = (start, end, str(tag))
            nb1=nb2 = 0
            ligne1 = ligne2 = 1
            endoflineposition =eol1 = eol2 = 0
            # of = offset to get the char position  (line.position)
            i = of1 = of2 = 0
            try:
                while i < end:
                    if sentence[i] == "\n":
                        endoflineposition = i
                        ligne2 += 1
                        of2 = i + 1

                        if i < start:
                            ligne1 += 1
                            of1 = i + 1
                    i += 1
                if position != -1:  # correction of offset positions created by suppr button
                    for couple in (train_data[position][1]):
                        # reached the word to print
                        if (start == couple[0] and end == couple[1]):
                            break
                        if couple[1] > of1 and couple[1] < start:
                            nb1 += 1
                            nb2+=1
                            if ligne1 != ligne2 and couple[1] < of2 :
                                nb2 -= 1
                
                firstp = f'{ligne1}.{start-of1+nb1}'
                lastp = f'{ligne2}.{end-of2+nb2}'
                #(firstp, lastp) = position_tkinter((start, end, nb))

                text_box.tag_add(tag, firstp, lastp)
                button_suppr_list.append(text_box.window_create(text_box.index(
                    lastp), window=tk.Button(text_box, text="x", command=lambda x=tuple: suppr(x))))
            except IndexError:
                    suppr(lastseed)
                    
    text_box.configure(state='disabled')

#work in progress
# def position_tkinter(tuple):  # return the start and end position in tkinter format of the selected tuple in absolute position 
#     global sentence
#     ligne1 = ligne2 = 1
#     i = of1 = of2 = 0
#     while i < tuple[1]:
#         if sentence[i] == "\n":
#             ligne2 += 1
#             of2 += i+1
#             if i < tuple[0]:
#                 ligne1 += 1
#                 of1 += i+1
#         i += 1
#     return (f'{ligne1}.{tuple[0]-of1}', f'{ligne2}.{tuple[1]-of2}')


def suppr(tuple):#suppr the tuple from the traininga data
    global sentence, train_data
    vw = text_box.yview() # Save the current position(percentage) of the top left corner
    position = sentence_in_data()
    #print(f'{position} \n {tuple}')
    train_data[position][1].remove(tuple)
    with open(f"training/{filename}", "w", encoding="utf-8") as output:  # saving data
        output.write(str(train_data))
    show_sentence()
    show_data()
    text_box.yview_moveto(vw[0])#keep position in text
    

def open_popup():  # deletion window
    global current_sentence
    position = sentence_in_data()
    if current_sentence == position:
        def delete():
            global train_data
            position = sentence_in_data()
            train_data.pop(position)
            top.destroy()
            show_sentence()
            show_data()
            with open(f"training/{filename}", "w", encoding="utf-8") as output:  # saving data
                output.write(str(train_data))
        top = tk.Toplevel(root)
        top.geometry("750x250")
        top.title("confirmation")
        tk.Label(top, font=('Helvetica 14 bold'),
                text="Voulez vraiment effacer les graines de la page actuelle ?").pack()
        tk.Button(top, text="Annuler", command=top.destroy, bg="blue",
                fg="white").place_configure(x=150, y=80, width=200, height=100)
        tk.Button(top, text="Supprimer", command=delete, bg="red",
                fg="white").place_configure(x=450, y=80, width=200, height=100)

def indata(x):#from a tkinter position return the groupe if in data else -1
    global sentence,train_data
    posi=sentence_in_data()
    if posi==-1:#no data on page
        return
    

def wordclic(event):
    global sentence, train_data,rel
    tuple=rel

    secondword=text_box.index("current")
    tuple+= " "+secondword
    text_box.unbind("<Button-1>")
    text_box.config(cursor="arrow")
    rel_box.configure(state='normal')
    rel_box.insert(tk.END,tuple)
    rel_box.insert(tk.END,"\n")
    rel_box.configure(state="disabled")


def Mark_Rel(x):
    global rel
    word = text_box.get("insert wordstart", "insert wordend")
    first = text_box.count("1.0", "insert wordstart", "displayindices")
    if first == None:
        first = 0
    else:
        first = first[0]
    last = text_box.count("1.0", "insert wordend", "displayindices")[0]
    
    rel=word+" " +x
    text_box.bind("<Button-1>", wordclic)
    text_box.config(cursor="crosshair")


# create the main window and GUI elements
root = tk.Tk()
root.title("Seed Marker")
current_sentence = 0
last_filepath=0
sentences = []
file_path = ""
filename = ""
train_data = []
visual_list = []
button_suppr_list = []
button_Mark_Seed = []
button_rel_list=[]
seeds = {
    0: {"color": "#F3F4ED"},
    1: {"color": "#F28482"},
    2: {"color": "#96BB7C"},
    3: {"color": "#76b5c5"},
    4: {"color": "#abdbe3"},
    5: {"color": "#D6EFC7"},
    6: {"color": "#F5CAC3"},
    7: {"color": "#7D1F35", "foreground": "white"},
    8: {"color": "#158467", "foreground": "white"},
    9: {"color": "#22577A", "foreground": "white"},
}

# create Frames
frame_left=tk.Frame(root)
frame_top = tk.Frame(frame_left)
frame_choix = tk.Frame(frame_left)
frame_bar = tk.Frame(frame_left)

# create Elements
text_comm = tk.Entry(frame_bar, width=40)
text_comm.grid(row=0, column=1)

button_select_file = tk.Button(frame_top, text='\u2193',font=("Courier", 15), command=select_file, bg='grey', fg='white')
button_select_file.grid(row=0,column=0,rowspan =2)
page=tk.Text(frame_top,width=6,height=1)
page.insert(1.0,"0")
page.grid(row=0,column=3)
pagenb=tk.Text(frame_top,width=6,height=1)
pagenb.grid(row=1,column=3)
pagenb.insert(1.0,"0")
pagenb.configure(state='disabled')

button_back = tk.Button(frame_top, text="<",command=prev_sentence,font=("Courier", 15), bg='grey', fg='white')
button_back.grid(row=0, column=2, padx=10,rowspan =2)
button_next = tk.Button(frame_top, text=">", command=next_sentence,font=("Courier", 15), bg='grey', fg='white')
button_next.grid(row=0, column=4, padx=10,rowspan =2)

button_first = tk.Button(frame_top, text="|<",command=first_sentence,font=("Courier", 15), bg='grey', fg='white')
button_first.grid(row=0, column=1, padx=10,rowspan =2)
button_last = tk.Button(frame_top, text=">|",command=last_sentence,font=("Courier", 15), bg='grey', fg='white')

button_last.grid(row=0, column=5, padx=10,rowspan =2)

text_box = st.ScrolledText(frame_left, wrap="word", width=150, height=30)

rel_box = st.ScrolledText(frame_left, wrap="word", width=50)
rel_box.configure(state='disabled')


for x in range(len(seeds)):
    try:
        button_Mark_Seed.append(tk.Button(
            frame_choix, text=f"{x}",font=('bold'), bg=seeds[x]['color'], fg=seeds[x]['foreground'], command=lambda a=x: Mark_Seed(a)))
    except KeyError:
        button_Mark_Seed.append(tk.Button(
            frame_choix, text=f"{x}", bg=seeds[x]['color'],font=('bold'), command=lambda a=x: Mark_Seed(a)))
    button_Mark_Seed[x].grid(row=1, column=x, padx=10)
    button_Mark_Seed[x].config(width=3)

# for x in ["--", "<>", "->", "<-", "><", "-<" , ">-", "<<", ">>"]:
#     button_rel_list.append(tk.Button(
#         frame_choix, text=f"{x}",command=lambda a=x: Mark_Rel(a)))
#     pos=len(button_rel_list)-1
#     button_rel_list[pos].grid(row=2, column=pos, padx=10,pady=5)
#     button_rel_list[pos].config(width=3)
    
seed_nb = []
for x in range(len(seeds)):
    seed_nb.append(tk.Label(frame_choix, text=0))
    seed_nb[x].grid(row=0, column=x, padx=10)

affichage = tk.Label(root, text="")
delete_button = tk.Button(
    root, bg="red", text='\u232B',font=("Courier", 15), command=open_popup)


# pack the GUI elements
frame_top.pack(pady=5)
# frame_bar.pack(expand=True, pady=5) # comment barre
frame_choix.pack()
text_box.pack(fill=tk.BOTH, expand=True,side="left")
# affichage.pack(pady=5)
frame_left.pack(fill=tk.BOTH,expand=True)
frame_left.grid_propagate(True)
# rel_box.pack(side="right",fill=tk.Y)
delete_button.pack(side="bottom")


# configure text tags

for x in range(len(seeds)):
    try:
        text_box.tag_configure(
            f"{x}", background=f"{seeds[x]['color']}", foreground=seeds[x]["foreground"])
    except KeyError:
        text_box.tag_configure(f"{x}", background=f"{seeds[x]['color']}")


# bind keyboard shortcut
def key(event):
    #seed tagging event
    if event.char in ['0','1','2','3','4','5','6','7','8','9']: 
            x=event.char
            Mark_Seed(int(x))
    #movement shortcut
    elif event.keysym in ["Right","Down"]:
        next_sentence()
    elif event.keysym in ["Up","Left"]:
        prev_sentence()


def change_page(event):
    global current_sentence,sentences
    value =int(page.get("1.0","end"))
    if current_sentence != value:
        current_sentence = value-1
        show_sentence()
        show_data()
    return "break"
        

text_box.bind("<Key>", key)
page.bind('<Return>', change_page)

root.mainloop()
