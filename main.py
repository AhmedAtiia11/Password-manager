from tkinter import *
from tkinter import messagebox
import random,json

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password_function():
    password_entry.delete(0,END)

    chosen_letters=[random.choice(letters) for char in range(random.randint(8, 10))]
    chosen_symbols=[random.choice(symbols) for char in range(random.randint(2, 4))]
    chosen_numbers=[random.choice(numbers) for char in range(random.randint(2, 4))]
    my_list=chosen_letters+chosen_numbers+chosen_symbols
    random.shuffle(my_list)

    password="".join(my_list)    
    password_entry.insert(0,password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password_function():      
    saved_website=website_entry.get().lower()
    saved_email=email_entry.get()
    saved_password=password_entry.get()
    data_to_save={saved_website:{"Email":saved_email,"Password":saved_password}}
    if len(saved_password)==0 or len(saved_email)==0 or len(saved_website)==0:
        messagebox.showerror(title="Error",message="You have left some fields empty\n Please fill all boxs")
    else:    
        is_ok=messagebox.askokcancel(title="website",message=f"Are you happy with the result\nWebsite:{saved_website}\nEmail:{saved_email}\nPassword:{saved_password}\n IS it ok to save?")
        if is_ok:
            # with open("Data.txt",mode="a")as file:    
            #     file.write(f"{saved_website} | {saved_email} | {saved_password}\n")
            try:
                with open("Data.json","r")as file:
                    data=json.load(file)
            except :
                with open("Data.json","w")as file:
                    json.dump(data_to_save,file,indent=4)
            else:
                data.update(data_to_save)
                with open("Data.json","w")as file:    
                    json.dump(data,file,indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)
           

def search_function():
    website_to_search=website_entry.get()
    try:
        with open("Data.json")as file:
            saved_data=json.load(file)
    except:
        messagebox.showerror(title="Error File Not Found",message="No Data File Found\nPlease cd to the json file first") 
    else:           
        if website_to_search in saved_data:
            messagebox.showinfo(title=f"{website_to_search.capitalize()}'s Data",message=f"Email: {saved_data[website_to_search]['Email']}\nPassword: {saved_data[website_to_search]['Password']}")
        else:
            messagebox.showerror(title='Error',message=f"{website_to_search.capitalize()}'Data Not Found")
    #     for item in saved_data:

    #         if item==website_to_search:
                # messagebox.showinfo(title=f"{item}'s Data",message=f"Email: {saved_data[item]['Email']}\nPassword: {saved_data[item]['Password']}")

# ---------------------------- UI SETUP ------------------------------- #
#screen
window=Tk()
window.config(padx=50,pady=50)
window.title("Password generator")
background=PhotoImage(file="logo.png")

#Website name entry
website_entry =Entry(width=30)
website_entry.focus()
website_label=Label(text="Web site :",font=("courier",15,"normal"))
website_entry.grid(row=1,column=1)
website_label.grid(row=1,column=0)

#Email entry
email_entry =Entry(width=50)
email_entry.insert(END,"your_default_email@gmail.com")
email_label=Label(text="Email/Username :",font=("courier",15,"normal"))
email_entry.grid(row=2,column=1,columnspan=2)
email_label.grid(row=2,column=0)


#password entry
password_entry =Entry(width=30)
password_label=Label(text="Password :",font=("courier",15,"normal"))
password_entry.grid(row=3,column=1)
password_label.grid(row=3,column=0)


#Button
password_button=Button(text="Generate password",command=generate_password_function)
add_button=Button(text="ADD password",width=47,command=add_password_function)
search_button=Button(text="Search",width=15,command=search_function)
password_button.grid(row=3,column=2)
add_button.grid(row=4,column=1,columnspan=2)
search_button.grid(row=1,column=2)



#Lock image
Canvas=Canvas(width=200,height=190)
Canvas.create_image(100,95,image=background)
Canvas.grid(row=0,column=1)



window.mainloop()