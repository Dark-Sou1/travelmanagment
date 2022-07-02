import tkinter
import tkinter.messagebox
import customtkinter
from rtadubai import Nol, Salik
from PIL import Image, ImageTk
customtkinter.set_appearance_mode("System")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("TravelManagement")
        self.iconphoto(True, tkinter.PhotoImage(file = r"gui\rta.png"))
        self.geometry("780x520")
        self.resizable(False, False)
        self.login_screen()

    def login_screen(self):

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_login = customtkinter.CTkFrame(master=self,width=400,height=200,corner_radius=5)
        self.frame_login.grid(row=0, column=0, sticky="nswe",padx = 20, pady = 20)

        self.label_login = customtkinter.CTkLabel(master=self.frame_login,text="Login",text_font=("Roboto Medium", 30))
        self.label_login.pack(pady=70)

        self.entry_id = customtkinter.CTkEntry(master=self.frame_login,width=200,placeholder_text="Username")
        self.entry_id.pack(pady=10)

        self.entry_password = customtkinter.CTkEntry(master=self.frame_login,width=200,show="*",placeholder_text="Password")
        self.entry_password.pack(pady=10)

        self.button_login = customtkinter.CTkButton(master=self.frame_login,text="Login",command=self.login)
        self.button_login.pack(pady=10)

    def main_screen(self):
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frame_left = customtkinter.CTkFrame(master=self,width=180,corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame left ============
        
        self.label_main = customtkinter.CTkLabel(master=self.frame_left,text="TravelManagement",text_font=("Roboto Medium", -18))
        self.label_main.grid(row=1,pady=20,padx =20)

        self.button_salik = customtkinter.CTkButton(master=self.frame_left,text="Salik",command=lambda: print("Hello, World!"))
        self.button_salik.grid(row=2,pady=10,padx=10)

        self.button_nol = customtkinter.CTkButton(master=self.frame_left,text="Nol",command=lambda: print("Hello, World!"))
        self.button_nol.grid(row=3,padx=10,pady=15)

        # ============ frame right =============

        self.frame_display_right = customtkinter.CTkFrame(master=self.frame_right,width=490,height=200,corner_radius=5)
        self.frame_display_right.grid(row=0, column=0, sticky="nswe",padx = 20, pady = 20)


    def login(self):
        self.frame_login.destroy()
        self.main_screen()

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    app = App()
    app.run()
