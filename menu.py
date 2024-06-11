'''
if you have'nt installed open AI and pillow, you need to write "pip install --upgrade openai pillow" in the console
You need to paste your open ai organization ID and your API key (available on openai.com) in the lines below
'''

import tkinter as tk
from tkinter import ttk
import openai
import urllib.request
from PIL import Image, ImageTk
import io

global image_label,photo,root

def update_image(new_url):
   
    # update 'photo' with the nex image
    global photo
    photo = load_image(new_url)
    image_label.config(image=photo)    # update the widget of our window

def load_image(url):
    with urllib.request.urlopen(url) as u:
        raw_data = u.read()
    im = Image.open(io.BytesIO(raw_data))
    im = im.resize((512, 512), Image.ANTIALIAS)
    return ImageTk.PhotoImage(im)

def generate(final_prompt):
    client=openai
    ##insert here your open ai api key and your organization code
    client.organization="INSERT CODE"
    client.api_key=("INSERT KEY") 
    
    response=client.images.generate(
      model="dall-e-3",  #we use dall e 3, but I don't think this IA is the more efficient to do this task
      prompt=final_prompt,
      size='1024x1024',
      quality="standard",
      n=1,)
    
    image_url = response.data[0].url
    return(image_url)




def submit(): 
    #### Here we can change the prompt to change the results
    final_prompt="A website for a company"
    if entries[0].get()!="":
        final_prompt+=" called "+entries[0].get()
    if entries[1].get()!="":
        final_prompt+=" with this description :"+entries[1].get()+"."
    if entries[2].get()!="":
        final_prompt+=" The aim of the website is :"+entries[2].get()+"."
    if comboboxes[1].get()!="":
        final_prompt+=" The style is "+comboboxes[1].get()
    if entries[0].get()!="":
        final_prompt+=" There is a top navigation bar with the name "+entries[0].get()+"."
    if comboboxes[0].get()!="":
        final_prompt+=" There is their logo at the "+comboboxes[0].get()+" of the page."
    if comboboxes[2].get()!="":
        final_prompt+=" The background is "+comboboxes[2].get()+"."
    if comboboxes[3].get()!="":
        final_prompt+=" The buttons are  "+comboboxes[3].get()+"."
    if comboboxes[4].get()!="":
        final_prompt+=" The font is "+comboboxes[4].get()+"."
    if comboboxes[5].get()!="":
        final_prompt+=" We particularly want to highlight: "+comboboxes[5].get()+" in the middle of the website."
    final_prompt+=" The text is in english."
           
    print(final_prompt)
    url=generate(final_prompt)
    #print(url)
    update_image(url)

    

def reset():
    # reset the inputs
    for entry in entries:
        entry.delete(0, tk.END)
    for combo in comboboxes:
        combo.set('')

# window creation
root = tk.Tk()
root.title("Test Prompt for website mockups")

# labels creation

entries = []

label = ttk.Label(root, text="Comapny name")
label.grid(row=1, column=0, padx=10, pady=10)
entry = ttk.Entry(root,width=35)
entry.grid(row=1, column=1, padx=10, pady=10)
entries.append(entry)

label = ttk.Label(root, text="Describe your company")
label.grid(row=2, column=0, padx=10, pady=10)
entry = ttk.Entry(root,width=40)
entry.grid(row=2, column=1, padx=10, pady=10)
entries.append(entry)

label = ttk.Label(root, text="Describe the aim of your website")
label.grid(row=3, column=0, padx=10, pady=10)
entry = ttk.Entry(root,width=40)
entry.grid(row=3, column=1, padx=10, pady=10)
entries.append(entry)

label = ttk.Label(root, text="Number of navigable menus")
label.grid(row=4, column=0, padx=10, pady=10)
entry = ttk.Entry(root)
entry.grid(row=4, column=1, padx=10, pady=10)
entries.append(entry)

#we load an empty image first (we should download it instead of using an URL)
photo = load_image("https://th.bing.com/th/id/R.84313e683af9dd645b86a0025302c351?rik=0pCiPRqxS3BQFg&riu=http%3a%2f%2fwww.solidbackgrounds.com%2fimages%2f1024x1024%2f1024x1024-dim-gray-solid-color-background.jpg&ehk=1t7TFzovmoaMN1umLMpHDx%2b%2fZAbhB0sR8BhwGaXjbsA%3d&risl=&pid=ImgRaw&r=0")
image_label = tk.Label(root, image=photo)
image_label.grid(row=0, column=4, rowspan=12, padx=10, pady=10)


# labels and comboboxes creation
comboboxes = []

label = ttk.Label(root, text="Position of the logo")
label.grid(row=5, column=0, padx=10, pady=10)
combo = ttk.Combobox(root, values=["Top left corner", "Top right corner", "Footpage"],width=20)
combo.grid(row=5, column=1, padx=10, pady=10)
comboboxes.append(combo)

label = ttk.Label(root, text="Style")
label.grid(row=1, column=2, padx=10, pady=10)
combo = ttk.Combobox(root, values=["corporate","Minimalist","friendly","Modern","Elegant","Technologic"])
combo.grid(row=1, column=3, padx=10, pady=10)
comboboxes.append(combo)

label = ttk.Label(root, text="Background color")
label.grid(row=2, column=2, padx=10, pady=10)
combo = ttk.Combobox(root, values=["Grey", " Black", "White","Green","Cream","Red","Blue","Yellow","Orange"])
combo.grid(row=2, column=3, padx=10, pady=10)
comboboxes.append(combo)

label = ttk.Label(root, text="Buttons color")
label.grid(row=3, column=2, padx=10, pady=10)
combo = ttk.Combobox(root, values=["Grey", " Black", "White","Green","Cream","Red","Blue","Yellow","Orange"])
combo.grid(row=3, column=3, padx=10, pady=10)
comboboxes.append(combo)

label = ttk.Label(root, text="Font color")
label.grid(row=4, column=2, padx=10, pady=10)
combo = ttk.Combobox(root, values=["Grey", " Black", "White","Green","Cream","Red","Blue","Yellow","Orange"])
combo.grid(row=4, column=3, padx=10, pady=10)
comboboxes.append(combo)

label = ttk.Label(root, text="Features you want to highlight")
label.grid(row=5, column=2, padx=10, pady=10)
combo = ttk.Combobox(root, values=["Seach bar","customer testimonial","images of our products side by side","Nothing"],width=30)
combo.grid(row=5, column=3, padx=10, pady=10)
comboboxes.append(combo)

# Submit and Reset buttons
submit_btn = ttk.Button(root, text="Submit (Wait 10 seconds)", command=submit)
submit_btn.grid(row=10, column=2, pady=20)

reset_btn = ttk.Button(root, text="Reset", command=reset)
reset_btn.grid(row=10, column=1, pady=20)


def on_close():
    # window closing
   
    root.destroy()  # destroy the winfow
    root.quit()     # stop mainloop and stop the program

root.protocol("WM_DELETE_WINDOW", on_close)
# start the app
root.mainloop()
