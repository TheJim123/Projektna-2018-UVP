import tkinter as tk
import random as r

class Karakter:
    def __init__(self):
        self.ime = ''
        self.level = 1
        self.leveli = [1, 2, 3, 4, 5]
        self.rase = ['Dwarf', 'Elf', 'Halfling', 'Human']
        self.rasa = ''
        self.razredi = ['Druid', 'Rogue', 'Warrior', 'Wizard']
        self.razred = ''
        self.aspect = 0
        self.intellect = 0
        self.power = 0
        self.reflex = 0
        self.pp = 0
        self.hp = 0
        self.mp = 0
        self.sposobnosti = []
        self.oklep = []
        self.orozje = []
        self.seznam_urokov = []
        self.spell_save = 0
        self.xp = 0
        
    def nastavi_ime(self, ime):
        self.ime = ime

    def nastavi_level(self, level):
        self.level = level #drop-down meni
        
    def izberi_raso(self, rasa):
        self.rasa = rasa #drop-down meni

    def izberi_razred(self, razred):
        self.razred = razred #drop-down meni

    def povecaj_aspect(self, vrednost):
        self.aspect += vrednost

    def povecaj_intellect(self, vrednost):
        self.intellect += vrednost

    def povecaj_power(self, vrednost):
        self.power += vrednost

    def povecaj_reflex(self, vrednost):
        self.reflex += vrednost

    def doloci_hp(self, vrednost):
        if vrednost > 10 or vrednost < 0:
            pass
        else:
            self.hp = vrednost

    def doloci_pp(self):
            self.pp = 10 - self.hp

    def spremeni_hp(self, vrednost):
        self.hp += vrednost

    def spremeni_pp(self, vrednost):
        self.pp += vrednost

    
        

class Sheet:
    def __init__(self):
        self.karakter = Karakter()
        window = tk.Tk()
###############################################################################
        vrh = tk.Frame(window,bg='gray', bd=0.5)
###############################################################################
        imensko_polje = tk.Frame(vrh, bd=0.5, bg='gray')
        imenska_oznaka = tk.Label(imensko_polje, text='Name:')
        imenski_vnos = tk.Entry(imensko_polje)

        imenska_oznaka.grid(column=1, row=1)
        imenski_vnos.grid(column=2, row=1)
        imensko_polje.grid(column=1, row=1)
###############################################################################
        level_polje = tk.Frame(vrh, bd=0.5, bg='gray')
        level_oznaka = tk.Label(level_polje, text='Level:')
        
        level_spremenljivka = tk.IntVar(level_polje)
        leveli = self.karakter.leveli
        level_spremenljivka.set(self.karakter.level)

        level_meni = tk.OptionMenu(level_polje, level_spremenljivka, *leveli)

        level_oznaka.grid(column=1, row=1)
        level_meni.grid(column=2, row=1)
        level_polje.grid(column=2, row=1)
###############################################################################
        rasno_polje = tk.Frame(vrh, bd=0.5, bg='gray')
        rasna_oznaka = tk.Label(rasno_polje, text='Race:')
        
        rasna_spremenljivka = tk.StringVar(rasno_polje)
        rase = self.karakter.rase
        rasna_spremenljivka.set(self.karakter.rasa)
        
        rasni_meni = tk.OptionMenu(rasno_polje, rasna_spremenljivka, *rase)

        rasna_oznaka.grid(column=1, row=1)
        rasni_meni.grid(column=2, row=1)
        rasno_polje.grid(column=3, row=1)        
###############################################################################
        razredno_polje = tk.Frame(vrh, bd=0.5, bg='gray')
        razredna_oznaka = tk.Label(razredno_polje, text='Class:')
        
        razredna_spremenljivka = tk.StringVar(razredno_polje)
        razredi = self.karakter.razredi
        razredna_spremenljivka.set(self.karakter.razred)

        razredni_meni = tk.OptionMenu(razredno_polje, razredna_spremenljivka, *razredi)

        razredna_oznaka.grid(column=1, row=1)
        razredni_meni.grid(column=2, row=1)
        razredno_polje.grid(column=4, row=1)
###############################################################################
        vrh.grid(column=3, row=1)
###############################################################################
        atributi = tk.Frame(window, bg='black', bd=0.5)
###############################################################################
        attributes = tk.Frame(atributi, bg='black', bd=1)
        attributes_naslov = tk.Label(attributes, text='Attributes')
        attributes_naslov.pack()
        attributes.grid(column=1, row=1)
###############################################################################
        aspect_frame = tk.Frame(atributi)
        aspect_label = tk.Label(aspect_frame, text = 'Aspect:')
        aspect_stat = tk.Label(aspect_frame, text = str(self.karakter.aspect))
        aspect_var = tk.IntVar(aspect_frame)
        aspect_plus = tk.Checkbutton(aspect_frame, variable = aspect_var)
        aspect_label.grid(column=1, row=1)
        aspect_stat.grid(column=2, row=1)
        aspect_plus.grid(column=3, row=1)
        aspect_frame.grid(column=1, row=2)
###############################################################################
        intellect_frame = tk.Frame(atributi)
        intellect_label = tk.Label(intellect_frame, text = 'Intellect:')
        intellect_stat = tk.Label(intellect_frame, text = str(self.karakter.intellect))
        intellect_var = tk.IntVar(intellect_frame)
        intellect_plus = tk.Checkbutton(intellect_frame, variable = intellect_var)
        intellect_label.grid(column=1, row=1)
        intellect_stat.grid(column=2, row=1)
        intellect_plus.grid(column=3, row=1)
        intellect_frame.grid(column=1, row=3)
###############################################################################
        power_frame = tk.Frame(atributi)
        power_label = tk.Label(power_frame, text = 'Power:')
        power_stat = tk.Label(power_frame, text = str(self.karakter.power))
        power_var = tk.IntVar(power_frame)
        power_plus = tk.Checkbutton(power_frame, variable = power_var)
        power_label.grid(column=1, row=1)
        power_stat.grid(column=2, row=1)
        power_plus.grid(column=3, row=1)
        power_frame.grid(column=1, row=4)
###############################################################################
        reflex_frame = tk.Frame(atributi)
        reflex_label = tk.Label(reflex_frame, text = 'Reflex:')
        reflex_stat = tk.Label(reflex_frame, text = str(self.karakter.reflex))
        reflex_var = tk.IntVar(reflex_frame)
        reflex_plus = tk.Checkbutton(reflex_frame, variable = reflex_var)
        reflex_label.grid(column=1, row=1)
        reflex_stat.grid(column=2, row=1)
        reflex_plus.grid(column=3, row=1)
        reflex_frame.grid(column=1, row=5)
###############################################################################
        atributi.grid(column=1, row=2)
###############################################################################
        
###############################################################################
###############################################################################
###############################################################################
###############################################################################
###############################################################################
        window.mainloop()

    def nastavi_ime(self):
        ime = imensko_polje.get()
        self.karakter.nastavi_ime(ime)
        
    def nastavi_level(self):
        level = level_polje.get()
        self.karakter.nastavi_level(level)

    def nastavi_raso(self):
        rasa = rasno_polje.get()
        self.karakter.nastavi_raso(rasa)

    def nastavi_razred(self):
        razred = razredno_polje.get()
        self.karakter.nastavi_razred(razred)

Sheet()

