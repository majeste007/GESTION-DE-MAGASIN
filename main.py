from tkinter import *
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
from time import strftime
import tempfile,  random, os

class SuperMarche:
    def __init__(self, root) -> None:
        self.root = root
        self.root.title("Super Marché")
        self.root.geometry("1366x720+0+0")
        title = Label(self.root, text="PNS Super Market", font=("algerian",45), bg='cyan', fg='black')
        title.pack(side=TOP, fill=X)

        def heure():
            hr = strftime("%H:%M:%S")
            lblheure.config(text=hr)
            lblheure.after(1000, heure)

        lblheure = Label(self.root, text="HH:MM:SS", font=("algerian",15), bg='cyan', fg='black')
        lblheure.place(x=0, y=25, width=120, height=45)
        heure()

        #Nos variables
        self.c_nom = StringVar()
        self.c_phon = StringVar()
        self.n_factu = StringVar()
        z = random.randint(1000, 9999)
        self.n_factu.set(z)
        self.c_email = StringVar()
        self.rech_factu = StringVar()
        self.produit = StringVar()
        self.prix = DoubleVar()
        self.qte = IntVar()
        self.totalBrut = IntVar()
        self.taxe = IntVar()
        self.totalNet = IntVar()

        #les categories
        self.listCategorie = ['selection','Vêtement','Style de vie','Telephone']
        self.listSousCategorieVetement = ['Pantalon','T-Shirt','Shirt'] 
        self.pantalon = ['Levis','Mufti','Skykar']       
        self.prixLevis = 5000       
        self.prixMufti = 1000      
        self.prixSkykar = 3000

        self.tshirt = ['Polo','Roadster','Jack & jones']     
        self.prixPolo = 1500       
        self.prixRoadster = 2550       
        self.prixJackJones = 3600 

        self.shirt = ['Peter England','Louis Philipe','Park Avenue']     
        self.prixPeterEngland = 1500       
        self.prixLouisPhilipe = 2550       
        self.prixParkAvenue = 3600 

        self.listSousCategorieSDV = ['Bath Soap','Crème','Huile de cheveux']
        self.bathSoap= ['Livebuy','Lux','Santoor','Pearl']
        self.prixLivebuy = 1400
        self.prixLux = 2400
        self.prixSantoor = 1450
        self.prixPearl = 2100

        self.creme = ['Fair&Lovely','Ponds','Olay','Garnier']
        self.prixFair = 1560
        self.prixPonds = 1410
        self.prixOlay = 4530
        self.prixGarnier = 1250

        self.huile = ['Parachute','Jasmine','Bajaj']
        self.prixParachute = 1450
        self.prixJasmine = 2300
        self.prixBajaj = 1500

        #phone
        self.listSousCategoriePhone = ["Iphone",'Huawei','Samsung']
        self.iPhone = ['Iphone XR','Iphone 11', 'Iphone 12']
        self.prixiPhoneXR = 450000
        self.prixiPhone11 = 650000
        self.prixiPhone12 = 930000

        self.huawei = ['Hauwei Y9S','Huawei P8','Huawei Mate']
        self.prixhuaweiY9S = 180000
        self.prixhuaweiP8 = 280000
        self.prixhuaweiMate = 296000

        self.samsung = ['samsung M12','samsung 16','samsung M21']
        self.prixSamsungM12 = 156000
        self.prixSamsung16 = 256000
        self.prixSamsungM21 = 306000


        # ZOne principale
        mainFrame = Frame(self.root, bd=2, relief=GROOVE, bg='white')
        mainFrame.place(x=10, y=100, width=1346,height=600)

        #client
        clientFrame = LabelFrame(mainFrame, text="Client",font=("algerian",12),bg='white')
        clientFrame.place(x=10, y=5, width=320, height=150)

        self.lblContact = Label(clientFrame, text="Contact",font=("algerian",11), bg='white')
        self.lblContact.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.textContact = Entry(clientFrame,textvariable=self.c_phon, font=('times new roman',11))
        self.textContact.grid(row=0, column=1, sticky=W, padx=5, pady=2)


        self.lblNom = Label(clientFrame, text="Nom",font=("algerian",11), bg='white')
        self.lblNom.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        self.textNom = Entry(clientFrame,textvariable=self.c_nom, font=('times new roman',11))
        self.textNom.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        self.lblEmail = Label(clientFrame, text="Email",font=("algerian",11), bg='white')
        self.lblEmail.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        self.textEmail = Entry(clientFrame,textvariable=self.c_email, font=('times new roman',11))
        self.textEmail.grid(row=2, column=1, sticky=W, padx=5, pady=2)


        #produits
        produitFrame = LabelFrame(mainFrame, text="Produit ",font=("algerian",12),bg='white')
        produitFrame.place(x=350, y=5, width=470, height=150)

        self.lblCategorie = Label(produitFrame, text="Categorie",font=("algerian",11), bg='white')
        self.lblCategorie.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        self.textCategorie = ttk.Combobox(produitFrame, font=('times new roman',10), values=self.listCategorie, state="readonly")
        self.textCategorie.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        self.textCategorie.current(0)
        self.textCategorie.bind('<<ComboboxSelected>>', self.fonctionchoixCategorie)


        self.lblSousCategorie = Label(produitFrame, text="Sous Categorie",font=("algerian",11), bg='white')
        self.lblSousCategorie.grid(row=1, column=0, sticky=W, padx=5, pady=2)
        self.textSousCategorie = ttk.Combobox(produitFrame, font=('times new roman',10), values=[""], state="readonly")
        self.textSousCategorie.grid(row=1, column=1, sticky=W, padx=5, pady=2)
        self.textSousCategorie.current(0)
        self.textSousCategorie.bind('<<ComboboxSelected>>', self.fonctionchoixSousCategorie)

        self.lblNomProduit = Label(produitFrame, text="Nom produit",font=("algerian",11), bg='white')
        self.lblNomProduit.grid(row=2, column=0, sticky=W, padx=5, pady=2)
        self.textNomProduit =  ttk.Combobox(produitFrame, font=('times new roman',10),textvariable=self.produit, state="readonly")
        self.textNomProduit.grid(row=2, column=1, sticky=W, padx=5, pady=2)
        self.textNomProduit.bind('<<ComboboxSelected>>', self.fonctionNomProduit)

        self.lblPrix = Label(produitFrame, text="Prix",font=("algerian",11), bg='white')
        self.lblPrix.grid(row=0, column=2, sticky=W, padx=5, pady=2)
        self.textPrix =  ttk.Combobox(produitFrame, font=('times new roman',10),width=15, textvariable=self.prix,state="readonly")
        self.textPrix.grid(row=0, column=3, sticky=W, padx=5, pady=2)

        self.lblQte = Label(produitFrame, text="QTE",font=("algerian",11), bg='white')
        self.lblQte.grid(row=1, column=2, sticky=W, padx=5, pady=2)
        self.textQte =  ttk.Entry(produitFrame, font=('times new roman',10),width=15,textvariable=self.qte)
        self.textQte.grid(row=1, column=3, sticky=W, padx=5, pady=2)

        recher_frame = Frame(mainFrame, bd=2, bg="white")
        recher_frame.place(x=830, y=10, width=500, height=70)
        
        self.lbl_recherche = Label(recher_frame, text="N° Facture", font=("times new roman",13,"bold"), bg="white")
        self.lbl_recherche.grid(row=0, column=0, sticky=W, padx=5, pady=2)
        
        self.txt_recherche = ttk.Entry(recher_frame,textvariable=self.rech_factu, font=("times new roman",13,"bold"))
        self.txt_recherche.grid(row=0, column=1, sticky=W, padx=5, pady=2)
        
        self.btn_recherche = Button(recher_frame,text="rechercher", font=("times new roman",13,"bold"))
        self.btn_recherche.grid(row=0, column=2, sticky=W, padx=5, pady=2)
        
        # facture
        Facture_label = LabelFrame(mainFrame, text="Facture", bg="crimson", font=("times new roman",13,"bold"))
        Facture_label.place(x=830, y=70, width=500, height=500)
        
        self.scroll_y = Scrollbar(Facture_label, orient=VERTICAL)
        
        self.text_area = Text(Facture_label,yscrollcommand=self.scroll_y.set, bg="white",fg='blue', font=("times new roman",13))
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.text_area.yview)
        self.text_area.pack(fill=BOTH, expand=1)

    def fonctionchoixCategorie(self, event=''):
        if self.textCategorie.get() == 'Vêtement':
            self.textSousCategorie.config(values=self.listSousCategorieVetement)
            self.textSousCategorie.current(0)
        if self.textCategorie.get() == 'Style de vie':
            self.textSousCategorie.config(values=self.listSousCategorieSDV)
            self.textSousCategorie.current(0)
        if self.textCategorie.get() == 'Telephone':
            self.textSousCategorie.config(values=self.listSousCategoriePhone)
            self.textSousCategorie.current(0)

    def fonctionchoixSousCategorie(self, event=''):
        #vetements
        if self.textSousCategorie.get() == 'Pantalon':
            self.textNomProduit.config(values=self.pantalon)
            self.textNomProduit.current(0)
        if self.textSousCategorie.get() == 'T-Shirt':
            self.textNomProduit.config(values=self.tshirt)
            self.textNomProduit.current(0)
        if self.textSousCategorie.get() == 'Shirt':
            self.textNomProduit.config(values=self.shirt)
            self.textNomProduit.current(0)
        #Style de vie
        if self.textSousCategorie.get() == 'Bath Soap':
            self.textNomProduit.config(values=self.bathSoap)
            self.textNomProduit.current(0)
        if self.textSousCategorie.get() == 'Crème':
            self.textNomProduit.config(values=self.creme)
            self.textNomProduit.current(0)
        if self.textSousCategorie.get() == 'Huile de cheveux':
            self.textNomProduit.config(values=self.huile)
            self.textNomProduit.current(0)
                
        #Telephone
        if self.textSousCategorie.get() == 'Iphone':
            self.textNomProduit.config(values=self.iPhone)
            self.textNomProduit.current(0)
        if self.textSousCategorie.get() == 'Huawei':
            self.textNomProduit.config(values=self.huawei)
            self.textNomProduit.current(0)
        if self.textSousCategorie.get() == 'Samsung':
            self.textNomProduit.config(values=self.samsung)
            self.textNomProduit.current(0)
            
    def fonctionNomProduit(self, event=""):
        #Vêtements
        if self.textNomProduit.get() == 'Levis':
            self.textPrix.config(values=self.prixLevis)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Mufti':
            self.textPrix.config(values=self.prixMufti)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Skykar':
            self.textPrix.config(values=self.prixSkykar)
            self.textPrix.current(0)
            self.qte.set(1)
        # 'Polo','Roadster','Jack & jones'
        if self.textNomProduit.get() == 'Polo':
            self.textPrix.config(values=self.prixPolo)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Roadster':
            self.textPrix.config(values=self.prixRoadster)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Jack & jones':
            self.textPrix.config(values=self.prixJackJones)
            self.textPrix.current(0)
            self.qte.set(1)
        # 'Peter England','Louis Philipe','Park A'
        if self.textNomProduit.get() == 'Peter England':
            self.textPrix.config(values=self.prixPeterEngland)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Louis Philipe':
            self.textPrix.config(values=self.prixLouisPhilipe)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Park Avenue':
            self.textPrix.config(values=self.prixParkAvenue)
            self.textPrix.current(0)
            self.qte.set(1)
        # 'Livebuy','Lux','Santoor','Pearl'
        if self.textNomProduit.get() == 'Livebuy':
            self.textPrix.config(values=self.prixLivebuy)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Lux':
            self.textPrix.config(values=self.prixLux)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Santoor':
            self.textPrix.config(values=self.prixSantoor)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Pearl':
            self.textPrix.config(values=self.prixPearl)
            self.textPrix.current(0)
            self.qte.set(1)
        # 'Fair&Lovely','Ponds','Olay','Garnier'
        if self.textNomProduit.get() == 'Fair&Lovely':
            self.textPrix.config(values=self.prixFair)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Ponds':
            self.textPrix.config(values=self.prixPonds)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Olay':
            self.textPrix.config(values=self.prixOlay)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Garnier':
            self.textPrix.config(values=self.prixGarnier)
            self.textPrix.current(0)
            self.qte.set(1)
        # 'Parachute','Jasmine','Bajaj'
        if self.textNomProduit.get() == 'Parachute':
            self.textPrix.config(values=self.prixParachute)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Jasmine':
            self.textPrix.config(values=self.prixJasmine)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Bajaj':
            self.textPrix.config(values=self.prixBajaj)
            self.textPrix.current(0)
            self.qte.set(1)
        # les bigos
        if self.textNomProduit.get() == 'Iphone XR':
            self.textPrix.config(values=self.prixiPhoneXR)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Iphone 11':
            self.textPrix.config(values=self.prixiPhone11)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Iphone 12':
            self.textPrix.config(values=self.prixiPhone12)
            self.textPrix.current(0)
            self.qte.set(1)
                
        if self.textNomProduit.get() == 'Hauwei Y9S':#,'Huawei P8','Huawei Mate':
            self.textPrix.config(values=self.prixhuaweiY9S)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Huawei P8':
            self.textPrix.config(values=self.prixhuaweiP8)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'Huawei Mate':
            self.textPrix.config(values=self.prixhuaweiMate)
            self.textPrix.current(0)
            self.qte.set(1)
                
        if self.textNomProduit.get() == 'samsung M12':#,'samsung 16','samsung M21':
            self.textPrix.config(values=self.prixSamsungM12)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'samsung 16':
            self.textPrix.config(values=self.prixSamsung16)
            self.textPrix.current(0)
            self.qte.set(1)
        if self.textNomProduit.get() == 'samsung M21':
            self.textPrix.config(values=self.prixSamsungM21)
            self.textPrix.current(0)
            self.qte.set(1)
                

                






if __name__== "__main__":
    root = Tk()
    ob = SuperMarche(root)
    root.mainloop()

