import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import filedialog

class Article:
    def __init__(self, nom, prix):
        self.nom = nom
        self.prix = prix

class VenteApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Application de Vente")
        self.master.configure(bg="#F0F0F0")
        
        self.articles = []
        
        self.create_widgets()
    
    def create_widgets(self):
        self.label_nom = tk.Label(self.master, text="Nom de l'article:", bg="#F0F0F0", fg="black", font=("Arial", 12))
        self.label_nom.grid(row=0, column=0, padx=10, pady=10)
        
        self.entry_nom = tk.Entry(self.master, font=("Arial", 12))
        self.entry_nom.grid(row=0, column=1, padx=10, pady=10)
        
        self.label_prix = tk.Label(self.master, text="Prix de l'article:", bg="#F0F0F0", fg="black", font=("Arial", 12))
        self.label_prix.grid(row=1, column=0, padx=10, pady=10)
        
        self.entry_prix = tk.Entry(self.master, font=("Arial", 12))
        self.entry_prix.grid(row=1, column=1, padx=10, pady=10)
        
        self.button_ajouter = ttk.Button(self.master, text="Ajouter", command=self.ajouter_article)
        self.button_ajouter.grid(row=2, column=0, padx=10, pady=10)
        
        self.button_afficher = ttk.Button(self.master, text="Afficher", command=self.afficher_articles)
        self.button_afficher.grid(row=2, column=1, padx=10, pady=10)
        
        self.button_supprimer = ttk.Button(self.master, text="Supprimer", command=self.supprimer_article)
        self.button_supprimer.grid(row=2, column=2, padx=10, pady=10)
        
        self.button_modifier = ttk.Button(self.master, text="Modifier", command=self.modifier_article)
        self.button_modifier.grid(row=2, column=3, padx=10, pady=10)
        
        self.button_effacer = ttk.Button(self.master, text="Effacer", command=self.effacer_articles)
        self.button_effacer.grid(row=2, column=4, padx=10, pady=10)
        
        self.button_sauvegarder = ttk.Button(self.master, text="Sauvegarder", command=self.sauvegarder_articles)
        self.button_sauvegarder.grid(row=2, column=5, padx=10, pady=10)
        
        self.button_restaurer = ttk.Button(self.master, text="Restaurer", command=self.restaurer_articles)
        self.button_restaurer.grid(row=2, column=6, padx=10, pady=10)
        
        self.listbox_articles = tk.Listbox(self.master, width=50, bg="white", fg="black", font=("Arial", 12))
        self.listbox_articles.grid(row=4, column=0, columnspan=7, padx=10, pady=10)
    
    def ajouter_article(self):
        nom = self.entry_nom.get()
        prix = self.entry_prix.get()
        
        if nom and prix:
            try:
                prix = float(prix)
                article = Article(nom, prix)
                self.articles.append(article)
                self.listbox_articles.insert(tk.END, f"{article.nom} - {article.prix} €")
                self.entry_nom.delete(0, tk.END)
                self.entry_prix.delete(0, tk.END)
                messagebox.showinfo("Succès", "L'article a été ajouté avec succès.")
            except ValueError:
                messagebox.showerror("Erreur", "Veuillez entrer un prix valide.")
        else:
            messagebox.showerror("Erreur", "Veuillez remplir tous les champs.")
    
    def afficher_articles(self):
        self.listbox_articles.delete(0, tk.END)
        
        for article in self.articles:
            self.listbox_articles.insert(tk.END, f"{article.nom} - {article.prix} €")
    
    def supprimer_article(self):
        selected_index = self.listbox_articles.curselection()
        
        if selected_index:
            self.listbox_articles.delete(selected_index)
            del self.articles[selected_index[0]]
            messagebox.showinfo("Succès", "L'article a été supprimé avec succès.")
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un article.")
    
    def modifier_article(self):
        selected_index = self.listbox_articles.curselection()
        
        if selected_index:
            selected_article = self.articles[selected_index[0]]
            self.entry_nom.delete(0, tk.END)
            self.entry_prix.delete(0, tk.END)
            self.entry_nom.insert(tk.END, selected_article.nom)
            self.entry_prix.insert(tk.END, selected_article.prix)
            self.listbox_articles.delete(selected_index)
            del self.articles[selected_index[0]]
            messagebox.showinfo("Succès", "L'article a été modifié avec succès.")
        else:
            messagebox.showerror("Erreur", "Veuillez sélectionner un article.")
    
    def effacer_articles(self):
        self.listbox_articles.delete(0, tk.END)
        self.articles.clear()
        messagebox.showinfo("Succès", "Les articles ont été effacés avec succès.")
    
    def sauvegarder_articles(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    for article in self.articles:
                        file.write(f"{article.nom},{article.prix}\n")
                messagebox.showinfo("Succès", "Les articles ont été sauvegardés avec succès.")
            except IOError:
                messagebox.showerror("Erreur", "Impossible de sauvegarder les articles dans le fichier.")
    
    def restaurer_articles(self):
        file_path = filedialog.askopenfilename(filetypes=[("Fichiers texte", "*.txt"), ("Tous les fichiers", "*.*")])
        if file_path:
            self.listbox_articles.delete(0, tk.END)
            self.articles.clear()
            try:
                with open(file_path, "r") as file:
                    for line in file:
                        nom, prix = line.strip().split(",")
                        prix = float(prix)
                        article = Article(nom, prix)
                        self.articles.append(article)
                        self.listbox_articles.insert(tk.END, f"{article.nom} - {article.prix} €")
                messagebox.showinfo("Succès", "Les articles ont été restaurés avec succès.")
            except (FileNotFoundError, ValueError):
                messagebox.showerror("Erreur", "Impossible de restaurer les articles à partir du fichier.")

root = tk.Tk()
app = VenteApp(root)
root.mainloop()