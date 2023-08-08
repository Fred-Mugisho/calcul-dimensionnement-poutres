import customtkinter
from verif_rigidite_poutres import my_screen as rigidite_screen
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

def my_screen():
    root = customtkinter.CTk()
    root.geometry("600x500")
    root.resizable(False, False)
    root.title("CALCUL ET DIMENSIONNEMENT DES POUTRES")

    def continuer_config():
        try:
            qv_entry_value = qv_entry.get()
            qh_entry_value = qh_entry.get()
            Gv_entry_value = Gv_entry.get()
            Gh_entry_value = Gh_entry.get()
            angle_alpha_entry_value = angle_alpha_entry.get()
            nsd_entry_value = nsd_entry.get()
            grand_a_entry_value = grand_a_entry.get()
            
            
            root.destroy()
            rigidite_screen()
            
        except Exception as e:
            error.configure(text=e, text_color='red')
        
        
        
                
    frame1 = customtkinter.CTkFrame(master=root)
    frame1.pack(pady=40, padx=10)
    titre = customtkinter.CTkLabel(master=frame1, text="VERIFICATION EN FLEXION DEVIÉE", font=("Roboto", 24, 'bold'))
    titre.pack(pady=12, padx=10)
    
    qv_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de qv", font=("Roboto", 16), width=420, height=30)
    qv_entry.pack(pady=12, padx=10)
    qh_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de qh", font=("Roboto", 16), width=420, height=30)
    qh_entry.pack(pady=12, padx=10)
    Gv_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de Gv", font=("Roboto", 16), width=420, height=30)
    Gv_entry.pack(pady=12, padx=10)
    Gh_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de Gh", font=("Roboto", 16), width=420, height=30)
    Gh_entry.pack(pady=12, padx=10)
    angle_alpha_entry = customtkinter.CTkEntry(master=frame1, placeholder_text="Entrer la valeur de l'angle alpha", font=("Roboto", 16), width=420, height=30)
    angle_alpha_entry.pack(pady=12, padx=10)
    
    frame2 = customtkinter.CTkFrame(master=root)
    frame2.pack(pady=0, padx=10)
    
    nsd_entry = customtkinter.CTkEntry(master=frame2, placeholder_text="Entrer la valeur de Nsd", font=("Roboto", 16), width=420, height=30)
    nsd_entry.pack(pady=12, padx=10)
    grand_a_entry = customtkinter.CTkEntry(master=frame2, placeholder_text="Entrer la valeur de A", font=("Roboto", 16), width=420, height=30)
    grand_a_entry.pack(pady=12, padx=10)
    
    error = customtkinter.CTkLabel(master=root, text="", font=("Roboto", 16,))
    error.pack(pady=2, padx=10)

    button = customtkinter.CTkButton(master=frame2, text="VERIFIER", width=300, height=30, font=("Roboto", 16, 'bold'), command=continuer_config)
    button.pack(pady=12, padx=10)

    root.mainloop()