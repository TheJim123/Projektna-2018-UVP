import tkinter as tk
import random as r

class Karakter:
    def __init__(self):
        self.ime = ''
        self.level = 0
        self.rase = ['Dwarf', 'Elf', 'Halfling', 'Human']
        self.rasa = ''
        self.razredi = ['Druid', 'Rogue', 'Warrior', 'Wizard']
        self.razred = ''
        self.atributi = [1, 1, 0, 0]
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
        if (level > 5) or (level < 0):
            pass
        else:
            self.level = level
        
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
        if vrednost > 10:
            pass
        else:
            self.hp = vrednost

    def doloci_pp(self, vrednost):
        if vrednost > 10:
            pass
        else:
            self.pp = vrednost

    def spremeni_hp(self, vrednost):
        self.hp += vrednost

    def spremeni_pp(self, vrednost):
        self.pp += vrednost

    
        

class Sheet:
    def __init__(self):
        self.karakter = Karakter()
        window = tk.Tk()
###############################################################################
        vrh = tk.Frame(window, bg='black', bd=2)
###############################################################################
        imensko_polje = tk.Frame(vrh, bd=1, bg='gray')
        imenska_oznaka = tk.Label(imensko_polje, text='Name:')
        imenski_vnos = tk.Entry(imensko_polje)

        imenska_oznaka.grid(column=1, row=1)
        imenski_vnos.grid(column=2, row=1)
        imensko_polje.grid(column=1, row=1)
###############################################################################
        level_polje = tk.Frame(vrh, bd=1, bg='gray')
        level_oznaka = tk.Label(level_polje, text='Level:')
        level_vnos = tk.Entry(level_polje)

        level_oznaka.grid(column=1, row=1)
        level_vnos.grid(column=2, row=1)
        level_polje.grid(column=2, row=1)
###############################################################################
        rasno_polje = tk.Frame(vrh, bd=1, bg='gray')
        rasna_oznaka = tk.Label(rasno_polje, text='Race:')
        
        rasna_spremenljivka = tk.StringVar(rasno_polje)
        izbire = self.karakter.rase
        rasna_spremenljivka.set(self.karakter.rasa)
        
        rasni_meni = tk.OptionMenu(rasno_polje, rasna_spremenljivka, *izbire)

        rasna_oznaka.grid(column=1, row=1)
        rasni_meni.grid(column=2, row=1)
        rasno_polje.grid(column=3, row=1)        
###############################################################################
        razredno_polje = tk.Frame(vrh, bd=1, bg='gray')
        razredna_oznaka = tk.Label(razredno_polje, text='Class:')
        
        razredna_spremenljivka = tk.StringVar(razredno_polje)
        izbire = self.karakter.razredi
        razredna_spremenljivka.set(self.karakter.razred)

        razredni_meni = tk.OptionMenu(razredno_polje, razredna_spremenljivka, *izbire)

        razredna_oznaka.grid(column=1, row=1)
        razredni_meni.grid(column=2, row=1)
        razredno_polje.grid(column=4, row=1)
###############################################################################
        vrh.grid(column=3, row=1)
###############################################################################
        atributi = tk.Frame(window, bg='black', bd=2)
###############################################################################
        
###############################################################################
        atributi.grid(column=1, row=3)
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

