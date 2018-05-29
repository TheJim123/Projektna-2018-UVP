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
        
    def doloci_spell_save(self):
        if self.razred == 'Druid':
            self.spell_save = self.level + self.aspect + 3
        elif self.razred == 'Wizard':
            self.spell_save = self.level + self.intellect + 3
        else:
            self.spell_save = 0

    def spremeni_hp(self, vrednost):
        self.hp += vrednost

    def spremeni_pp(self, vrednost):
        self.pp += vrednost

    
        

class Sheet:
    def __init__(self):
        self.karakter = Karakter()
        window = tk.Tk()
###############################################################################
        vrh = tk.Frame(window, bd=0.5, bg = 'gray')
###############################################################################
        imensko_polje = tk.Frame(vrh, bd=0.5)
        imenska_oznaka = tk.Label(imensko_polje, text='Name:')
        imenski_vnos = tk.Entry(imensko_polje)

        imenska_oznaka.grid(column=1, row=1)
        imenski_vnos.grid(column=2, row=1)
        imensko_polje.grid(column=1, row=1)
###############################################################################
        level_polje = tk.Frame(vrh, bd=0.5)
        level_oznaka = tk.Label(level_polje, text='Level:')
        
        level_spremenljivka = tk.IntVar(level_polje)
        leveli = self.karakter.leveli
        level_spremenljivka.set(self.karakter.level)

        level_meni = tk.OptionMenu(level_polje, level_spremenljivka, *leveli)

        level_oznaka.grid(column=1, row=1)
        level_meni.grid(column=2, row=1)
        level_polje.grid(column=2, row=1)
###############################################################################
        rasno_polje = tk.Frame(vrh, bd=0.5)
        rasna_oznaka = tk.Label(rasno_polje, text='Race:')
        
        rasna_spremenljivka = tk.StringVar(rasno_polje)
        rase = self.karakter.rase
        rasna_spremenljivka.set(self.karakter.rasa)
        
        rasni_meni = tk.OptionMenu(rasno_polje, rasna_spremenljivka, *rase)

        rasna_oznaka.grid(column=1, row=1)
        rasni_meni.grid(column=2, row=1)
        rasno_polje.grid(column=3, row=1)        
###############################################################################
        razredno_polje = tk.Frame(vrh, bd=0.5)
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
        levo = tk.Frame(window, bg='gray')
###############################################################################
        attribute_frame = tk.Frame(levo,bg='gray', bd=0.5)
###############################################################################
        attributes = tk.Frame(attribute_frame, bd=1)
        attributes_naslov = tk.Label(attributes, text='Attributes')
        attributes_naslov.pack()
        attributes.grid(column=1, row=1)
###############################################################################
        aspect_frame = tk.Frame(attribute_frame)
        aspect_label = tk.Label(aspect_frame, text = 'Aspect:')
        aspect_stat = tk.Label(aspect_frame, text = str(self.karakter.aspect))
        aspect_var = tk.IntVar(aspect_frame)
        aspect_plus = tk.Checkbutton(aspect_frame, variable = aspect_var)
        aspect_label.grid(column=1, row=1)
        aspect_stat.grid(column=2, row=1)
        aspect_plus.grid(column=3, row=1)
        aspect_frame.grid(column=1, row=2)
###############################################################################
        intellect_frame = tk.Frame(attribute_frame)
        intellect_label = tk.Label(intellect_frame, text = 'Intellect:')
        intellect_stat = tk.Label(intellect_frame, text = str(self.karakter.intellect))
        intellect_var = tk.IntVar(intellect_frame)
        intellect_plus = tk.Checkbutton(intellect_frame, variable = intellect_var)
        intellect_label.grid(column=1, row=1)
        intellect_stat.grid(column=2, row=1)
        intellect_plus.grid(column=3, row=1)
        intellect_frame.grid(column=1, row=3)
###############################################################################
        power_frame = tk.Frame(attribute_frame)
        power_label = tk.Label(power_frame, text = 'Power:')
        power_stat = tk.Label(power_frame, text = str(self.karakter.power))
        power_var = tk.IntVar(power_frame)
        power_plus = tk.Checkbutton(power_frame, variable = power_var)
        power_label.grid(column=1, row=1)
        power_stat.grid(column=2, row=1)
        power_plus.grid(column=3, row=1)
        power_frame.grid(column=1, row=4)
###############################################################################
        reflex_frame = tk.Frame(attribute_frame)
        reflex_label = tk.Label(reflex_frame, text = 'Reflex:')
        reflex_stat = tk.Label(reflex_frame, text = str(self.karakter.reflex))
        reflex_var = tk.IntVar(reflex_frame)
        reflex_plus = tk.Checkbutton(reflex_frame, variable = reflex_var)
        reflex_label.grid(column=1, row=1)
        reflex_stat.grid(column=2, row=1)
        reflex_plus.grid(column=3, row=1)
        reflex_frame.grid(column=1, row=5)
###############################################################################
        attribute_frame.pack()
###############################################################################
        magic_frame = tk.Frame(levo)
###############################################################################
        magic = tk.Frame(magic_frame)
        magic_naslov = tk.Label(magic, text = 'Magic')
        mp = tk.Label(magic, text='mp: {}'.format(self.karakter.mp))
        spell_save = tk.Label(magic, text = 'spell save: {}'.format(self.karakter.spell_save))
        magic_naslov.grid(column=2, row=1)
        mp.grid(column=1, row=2)
        spell_save.grid(column=3, row=2)
        magic.pack()
        spellbook = tk.Frame(magic_frame, bg='gray')
        spell_1 = tk.Frame(spellbook)
        spell_1_name_label = tk.Label(spell_1, text='Spell:')
        spell_1_name = tk.Entry(spell_1)
        spell_1_cost_label = tk.Label(spell_1, text='Cost:')
        spell_1_cost = tk.Entry(spell_1)
        spell_1_name_label.grid(column=1, row=1)
        spell_1_name.grid(column=2, row=1)
        spell_1_cost_label.grid(column=3, row=1)
        spell_1_cost.grid(column=4, row=1)
        spell_1.pack()
################################################################################
        spell_2 = tk.Frame(spellbook)
        spell_2_name_label = tk.Label(spell_2, text='Spell:')
        spell_2_name = tk.Entry(spell_2)
        spell_2_cost_label = tk.Label(spell_2, text='Cost:')
        spell_2_cost = tk.Entry(spell_2)
        spell_2_name_label.grid(column=1, row=1)
        spell_2_name.grid(column=2, row=1)
        spell_2_cost_label.grid(column=3, row=1)
        spell_2_cost.grid(column=4, row=1)
        spell_2.pack()
################################################################################
        spell_3 = tk.Frame(spellbook)
        spell_3_name_label = tk.Label(spell_3, text='Spell:')
        spell_3_name = tk.Entry(spell_3)
        spell_3_cost_label = tk.Label(spell_3, text='Cost:')
        spell_3_cost = tk.Entry(spell_3)
        spell_3_name_label.grid(column=1, row=1)
        spell_3_name.grid(column=2, row=1)
        spell_3_cost_label.grid(column=3, row=1)
        spell_3_cost.grid(column=4, row=1)
        spell_3.pack()
################################################################################
        spell_4 = tk.Frame(spellbook)
        spell_4_name_label = tk.Label(spell_4, text='Spell:')
        spell_4_name = tk.Entry(spell_4)
        spell_4_cost_label = tk.Label(spell_4, text='Cost:')
        spell_4_cost = tk.Entry(spell_4)
        spell_4_name_label.grid(column=1, row=1)
        spell_4_name.grid(column=2, row=1)
        spell_4_cost_label.grid(column=3, row=1)
        spell_4_cost.grid(column=4, row=1)
        spell_4.pack()
################################################################################
        spell_5 = tk.Frame(spellbook)
        spell_5_name_label = tk.Label(spell_5, text='Spell:')
        spell_5_name = tk.Entry(spell_5)
        spell_5_cost_label = tk.Label(spell_5, text='Cost:')
        spell_5_cost = tk.Entry(spell_5)
        spell_5_name_label.grid(column=1, row=1)
        spell_5_name.grid(column=2, row=1)
        spell_5_cost_label.grid(column=3, row=1)
        spell_5_cost.grid(column=4, row=1)
        spell_5.pack()
################################################################################
        spellbook.pack()
###############################################################################
        magic_frame.pack()
###############################################################################
        skill_frame = tk.Frame(levo)
################################################################################
        skill_naslov = tk.Label(skill_frame, text='Skills:')
        skills = tk.Frame(skill_frame)
        skill_1 = tk.Entry(skills)
        skill_1.grid(column=1, row=1)
        skill_2 = tk.Entry(skills)
        skill_2.grid(column=3, row=1)
        skill_3 = tk.Entry(skills)
        skill_3.grid(column=1, row=2)
        skill_4 = tk.Entry(skills)
        skill_4.grid(column=3, row=2)
        skill_naslov.pack()
        skills.pack()
################################################################################
        skill_frame.pack()
###############################################################################
        levo.grid(column = 1, row = 2)
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

