import tkinter as tk
from PIL import Image,ImageTk
from threading import Thread
import time,ttt,random #Ici, on importe le module de la logique , du temps et random
from tkinter import messagebox
from itertools import chain

#Bonne nouvelle , on peut régler le problème du label[2], il suffit de tout mettre dans un thread principal et de changer d'information en fonction de la valeur envoyée par chaque fonction


class page_1(tk.Frame):
    """Cette page est pour l'accueil et elle sera comme mot de bienvenue"""
    def __init__(self,master):
        super().__init__(master)
        self.configure(bg = 'blue',relief = 'ridge')

        self.widgets()
    def widgets(self):
        """Fonction pour placer le ou les widgets sur l'écran"""
        self.label = tk.Label(self,text = "Tic Tac Toe \n  X  O  X \n Joue contre Max 😎 et testes ton niveau",fg = 'white',bg = 'blue',font = ("Comic Sans MS",20))
        self.info = tk.Label(self,text = "Sélectionner un niveau",font = ('Verdana',15),bg = "white",fg = 'blue')
        self.bouton = tk.Button(self,text = 'Lancer la partie',fg = 'blue',activeforeground='red',bg = 'black',font = ('Verdana',20),cursor='hand2')
        self.var = tk.StringVar(self)
        self.var.set('Moyen')
        self.liste_choix = ['Facile','Moyen','Difficile'] 
        self.choix = tk.OptionMenu(self,self.var,*self.liste_choix)
        self.choix.config(font=('Verdana',20),fg = 'blue',activebackground='blue',activeforeground='white')
        self.choix['menu'].configure(font=('Verdana',15),fg = 'white',bg = 'blue')
        #Placement des widgets sur l'écran
        self.label.place(relx = 0,rely = 0,relheight=0.4,relwidth = 1)
        self.info.place(relx =1/3,rely = 0.6,relheight=0.1,relwidth = 1/3)
        self.bouton.place(relx =1/3,rely = 0.45,relheight=0.11,relwidth = 1/3 )
        self.choix.place(relx=1/3,rely = 0.7,relheight=0.1,relwidth = 1/3)



class page_2(tk.Frame):
    """Cette page est là pour la présentation de notre cher max"""
    def __init__(self,master,path):
        super().__init__(master)
        self.path = path
        #Ceci nous permettra de connaitre la taille de la fenêtre 
        self.x = self.master.winfo_height()
        self.y = self.master.winfo_width()
        self.picture = ImageTk.PhotoImage(Image.open(self.path))
        #Définition du repère temps
        self.temps = time.time()
        #Ici, on place les widgets sur l'écran
        self.widgets()
        

    def widgets(self):
        #Ici, on a notre canva qu'on a définit ici
        self.canva = tk.Canvas(self,relief = 'ridge')
       
        #Ici, c'est notre label pour la description
        
        self.label = tk.Label(self,font = ('Comic Sans MS',20),fg = 'white',bg = 'blue')
        #Cet label est ajouté en sup pour des effets d'animations 
        self.label_supp = tk.Label(self,font = ('Comic Sans MS',20,"italic"),fg = 'white',bg = 'blue',cursor='hand2')
        self.canva.create_image(0,0,image = self.picture,anchor = 'nw')
        #Ici, on place le canva
        self.canva.place(relx = 0,rely = 0,relheight = 1,relwidth = 0.5)
        #Ici, on place le label
        self.label.place(relx = 0.5,rely = 0,relheight = 0.7,relwidth = 0.5)
        #Ici, on place le label supp
        self.label_supp.place(relx = 0.5,rely = 0.7,relheight = 0.3,relwidth = 0.5)
    def resize_fond(self,event):
        """Cette fonction va nous permettre de redimensionner la photo du personnage virtuel"""
        self.x = self.master.winfo_height()
        self.y = self.master.winfo_width()
        self.image = Image.open(self.path)
        self.new_image = self.image.resize((int(self.y/2),int(self.x)))
        self.picture = ImageTk.PhotoImage(self.new_image)
        self.canva.create_image( 0,0,image = self.picture,anchor = 'nw')
    def animation(self):
        """Cette fonction va nous permettre d'animer l'écran là"""
        self.texte_1 = "Je m'appelle Max et je serai \n ton adversaire durant \n chaque partie \n Veillons voir si tu peux \n me battre  "
        self.texte_2 = " Cliquez ici pour continuer  "
        self.label.configure(text = self.texte_1)
        
        self.duree = time.time() - self.temps
        if int(self.duree) % 2 == 0:
            self.label_supp.configure(text = self.texte_2)
        if int(self.duree % 2) == 1:
            self.label_supp.configure(text = '')
        self.master.after(500,self.animation)
    def alleger(self):
        """Cette fonction permettra de lancer les élements lourds dans un seul thread"""
        #Ici, on place la fonction resize fond
        Thread(target = self.master.bind,args = ('<Configure>',self.resize_fond),daemon = True).start()
        #Ici, on s'arrange pour notre animation 
        Thread(target = self.master.after,args = (500,self.animation),daemon = True).start()

 #Note pour tout ce qui me suivent actuellement 
 # C'est mieux de créer une classe régroupant tous les niveaux du jeu, allant du niveau facile au niveau difficile


#Ici, on va faire la classe correspondante à toute les niveaux du jeu
class niveau():
    """Cette classe va nous permettre de switcher entre toute les niveaux du jeu"""
    def __init__(self,liste_des_boutons:list,liste_des_mots:list,liste_des_labels:list):
        super().__init__()
        self.liste_des_boutons = liste_des_boutons
        self.liste_des_mots = liste_des_mots
        self.liste_des_labels = liste_des_labels
        self.copie = list(self.liste_des_boutons)
        #Ici, c'est la partie intelligence artificielle, on va devoir intégrer des listes pour faire le learning
        #Ici, c'est la partie intelligence artificielle, on va devoir intégrer des listes pour faire le learning
        self.liste_premier_choix = [self.liste_des_boutons[4],self.liste_des_boutons[0],self.liste_des_boutons[2],self.liste_des_boutons[6],self.liste_des_boutons[8]]
        self.liste_second_choix = [self.liste_des_boutons[1],self.liste_des_boutons[3],self.liste_des_boutons[5],self.liste_des_boutons[7]]
        self.liste_premier_choix_copie = self.liste_premier_choix.copy()

        self.liste_gagnant = [[self.liste_des_boutons[0],self.liste_des_boutons[1],self.liste_des_boutons[2]],
                              [self.liste_des_boutons[3],self.liste_des_boutons[4],self.liste_des_boutons[5]],
                              [self.liste_des_boutons[6],self.liste_des_boutons[7],self.liste_des_boutons[8]],
                              [self.liste_des_boutons[0],self.liste_des_boutons[3],self.liste_des_boutons[6]],
                              [self.liste_des_boutons[1],self.liste_des_boutons[4],self.liste_des_boutons[7]],
                              [self.liste_des_boutons[2],self.liste_des_boutons[5],self.liste_des_boutons[8]],
                              [self.liste_des_boutons[0],self.liste_des_boutons[4],self.liste_des_boutons[8]],
                              [self.liste_des_boutons[2],self.liste_des_boutons[4],self.liste_des_boutons[6]]]
        
        self.tour = 0 # C'est la variable  qui va nous renseigner sur le tour de l'ordinateur
        #Ici, on crée une liste pour les boutons déjà cliqués
        self.liste_cliquer = []
        #Ici, on initialise le repère temps
        self.temps = time.time()
        #Ici, on définit la variable jouer en premier, si c'est vrai la personne joue en premier
        self.status = True
        #Ici, on définit la variable qui va permettre de savoir le nombre de fois jouer
        self.compteur = len(self.liste_cliquer)
        #Ici, on va définir la variable qui va nous permettre de savoir si quelqu'un a gagné
        self.gagnant = False
        #Ici, on va créer une variable qui va nous permettre de ne plus répéter le messagebox plusieurs fois
        self.repete = True
    
        
        #Ici, on va initier un bind pour pouvoir faire le bind sur les paroles de max
        Thread(target = self.liste_des_labels[2].bind, args = ('<Button-1>',self.ask_recommencer_2),daemon = True).start()
        #Ici, on va initier un bind pour pouvoir faire le bind sur l'icône de max
        Thread(target = self.liste_des_labels[1].bind, args = ('<Button-1>',self.presentation),daemon = True).start()
        #Ici, on va initier le dictionnaire qui va permettre de faire le score de chaque joueur
        self.score = {'utilisateur':0,'max':0}
        self.liste_des_labels[3]['text'] = f'Score de Max : {self.score['max']}'
        self.liste_des_labels[4]['text'] = f'Ton Score : {self.score['utilisateur']}'
        #Ici, on initie une variable qui lui, sera comme un indicateur de ce que Max va dire à chaque partie
        self.indicateur = 0 #0 est le par défaut
        #Ici, on va initier un thread qui va nous permettre de faire la surveilance de Max
        Thread(target = self.liste_des_labels[2].after,args = (10,self.message_de_max),daemon = True).start()
        #Ici, on crée une variable pour le self.after de a ton tour maintenant ait une fin
        self.fin = True

        #Ici, on va mettre un bind sur le label 3 et 4
        Thread(target = self.liste_des_labels[3].bind,args = ('<Button-1>',self.reintialiser_score),daemon = True).start()
        Thread(target = self.liste_des_labels[4].bind,args = ('<Button-1>',self.reintialiser_score),daemon = True).start()
    def reintialiser_score(self,event):
        """Cette fonction va nous permettre de reintialiser le score"""
        message = messagebox.askyesno("Tic Tac Toe: Max te parle","Veux-tu Reintialiser le score ?")
        if message:
            self.score = {'utilisateur':0,'max':0}
            self.liste_des_labels[3]['text'] = f'Score de Max : {self.score['max']}'
            self.liste_des_labels[4]['text'] = f'Ton Score : {self.score['utilisateur']}'
        else:
            pass

    def appartenir(self,liste_tester:list):
        """"Cette fonction va nous permettre de connaître le nombre de boutons libres dans une liste"""
        self.liste_tester = liste_tester
        n = 0 # Le meilleur c'est 2,0, le suivant c'est 1,0, après c'est 1,1
        m = 0
        butt = []
        for i in self.liste_tester:
            if i.cget('text').upper().strip() == 'O':
                m +=1
            if i.cget('text').upper().strip() == 'X':
                n +=1
            if i.cget('text').upper().strip() == '' :
                butt.append(i)
        return n,m,butt
    def intelligencia_1(self) -> tk.Button:
        """Cette fonction va nous permettre de faire le choix de réponse de Max"""
        liste1 = []
        liste2 = []
        liste3 = []
        liste4 = []
        liste5 = []
        liste6 = []
        liste = []
        
        if self.tour <2:
            for element in self.liste_second_choix:
                if element.cget('text') == '':
                    liste6.append(element)
            return random.choice(liste6)
        # elif self.tour ==2 and :
        #     for element in self.liste_premier_choix:
        #         if element.cget('text') == '':
        #             liste.append(element)
        #     return random.choice(liste)
                    
        else:
            for liste in self.liste_gagnant:
                n , m, butt = self.appartenir(liste)
                
                if n == 2 and m == 0:
                    
                    liste1.insert(0,butt[0])
                    break
                if self.tour ==2 and m == 1 and len(butt) == 2:
                    for element in self.liste_premier_choix:
                        if element.cget('text').strip() == '':
                            liste1.append(element)
                  
                if n == 1 and m == 0:
                    
                    liste2.append(butt[0])
                    
                if n == 1 and m == 1:
                   
                    liste3.append(butt[0])
                    
                if n == 0 and m == 1:
                    
                    liste4.append(butt[0])
                    
                if n == 0 and m == 2:
                    
                    liste5.append(butt[0])

                if  m == 2 and n==0:
                    liste1.append(butt[0])

                if self.tour == 2 and m == 2 and n ==0:
                    liste1.insert(0,butt[0])
                    break
                
                # else:
                #     self.premier_choix = random.choice(self.liste_des_boutons)
        
        liste = [*liste1,*liste2,*liste3,*liste4,*liste5]
        return liste[0]  
    def intelligencia_2(self)->tk.Button:
        """Cette fonction va nous permettre de faire le choix adéquats pour le niveau difficile de notre jeu"""
        liste1 = []
        liste2 = []
        liste3 = []
        liste4 = []
        liste5 = []
        liste6 = []
        liste = []
        
        if self.tour <2:
            for element in self.liste_premier_choix:
                if element.cget('text') == '':
                    return element
        # elif self.tour ==2 and :
        #     for element in self.liste_premier_choix:
        #         if element.cget('text') == '':
        #             liste.append(element)
        #     return random.choice(liste)
                    
        else:
            for liste in self.liste_gagnant:
                n , m, butt = self.appartenir(liste)
                
                if n == 2 and m == 0:
                    
                    liste1.insert(0,butt[0])
                    break
                if self.tour ==2 and m == 1 and len(butt) == 2:
                    for element in self.liste_premier_choix:
                        if element.cget('text').strip() == '':
                            liste1.append(element)
                  
                if n == 1 and m == 0:
                    
                    liste2.append(butt[0])
                    
                if n == 1 and m == 1:
                   
                    liste3.append(butt[0])
                    
                if n == 0 and m == 1:
                    
                    liste4.append(butt[0])
                    
                if n == 0 and m == 2:
                    
                    liste5.append(butt[0])

                if  m == 2 and n==0:
                    liste1.append(butt[0])

                if self.tour == 2 and m == 2 and n ==0:
                    liste1.insert(0,butt[0])
                    break
                
                # else:
                #     self.premier_choix = random.choice(self.liste_des_boutons)
        
        liste = [*liste1,*liste2,*liste3,*liste4,*liste5]
        return liste[0]  
    def message_de_max(self):
        """Cet thread va nous permettre de faire parler à Max sans pour autant souffrit comme avant pour les thread"""
        if self.indicateur == 0:
            self.liste_des_labels[2].configure(text = "A ton tour maintenant ",fg = 'blue')
        if self.indicateur == 1 and self.gagnant == False and self.compteur < 9 and self.fin:
            x = self.liste_des_mots[self.compteur]
            self.liste_des_labels[2].configure(text = f"{x}",fg='blue')
            self.liste_des_labels[2].after(1500,lambda : self.liste_des_labels[2].configure(text = "A ton tour maintenant ",fg = 'blue'))
            self.fin = False
        if self.indicateur == 2:
            self.liste_des_labels[2].configure(text = "Tu as gagné, Félicitations 🥳🥳",fg='blue')
        if self.indicateur == 3:
            self.liste_des_labels[2].configure(text = "Désolé, tu as perdu et j'ai gagné 🥳🥳",fg='red')
        if self.indicateur == 4:
            self.liste_des_labels[2].configure(text = "Pas de veine, c'est un match nul 😑😫",fg = 'purple')
        if self.indicateur == 5:
            self.liste_des_labels[2].configure(text = "Si tu veux continuer,clique sur mon icône",fg = 'purple')
        if self.indicateur == 6:
            self.liste_des_labels[2].configure(text = "Je m'appelle Max, ia crée par N.Canisius. Prêt pour une partie ?",fg = 'blue')
        Thread(target = self.liste_des_labels[2].after,args = (10,self.message_de_max),daemon = True).start()
    def presentation(self,event):
        """Cette fonction va nous permettre de faire ma présentation"""  
        self.indicateur = 6
    def configuration(self):
        """Cette fonction va nous permettre de configurer les boutons , disons les commandes des boutons"""
        
        #Ici, on va configurer la fonction des boutons
        for button in self.liste_des_boutons:
            button.configure(command = lambda button = button: Thread(target = self.choix_de_la_personne,args = (button,),daemon = True ).start())
        

    def choix_de_max_facile(self):
        """Cette fonction va permettre à max de faire son choix """
        #Ici, on fait un peu d'animation, espérons que ça marche
        if self.compteur < 9 and self.status == False and self.gagnant == False:
            #Ici, on place self.repete pour qu'au cas où la personne l'avait supprimé, il revient après
            self.repete = True
            
            self.indicateur = 1 #Ici, pour montrer le mots d'encouragement
            self.choix = random.choice(self.liste_des_boutons) ########################################Ici, c'est pour attirer l'attention sur le fait que ici, on doit changer ca
            self.liste_des_boutons.remove(self.choix)
            self.liste_cliquer.append(self.choix)
            self.choix.configure(text = 'X',fg = 'red',cursor = 'arrow')
            self.status = True ; self.compteur = len(self.liste_cliquer)
            #Ici, on montre le text sur l'écran 
            #self.indicateur=0
        else:
            pass

    def choix_de_max_moyen(self):
        """Cette fonction va permettre à max de faire son choix """
        #Ici, on fait un peu d'animation, espérons que ça marche
        if self.compteur < 9 and self.status == False and self.gagnant == False:
            #Ici, on place self.repete pour qu'au cas où la personne l'avait supprimé, il revient après
            self.repete = True
            self.tour+=1
            self.indicateur = 1 #Ici, pour montrer le mots d'encouragement
            self.choix = self.intelligencia_1()
            self.liste_des_boutons.remove(self.choix)
            self.liste_cliquer.append(self.choix)
            self.choix.configure(text = 'X',fg = 'red',cursor = 'arrow')
            self.status = True ; self.compteur = len(self.liste_cliquer)
            #Ici, on montre le text sur l'écran 
            #self.indicateur=0
        else:
            pass

    def choix_de_max_difficile(self):
        """Cette fonction va permettre à max de faire son choix """
        #Ici, on fait un peu d'animation, espérons que ça marche
        if self.compteur < 9 and self.status == False and self.gagnant == False:
            #Ici, on place self.repete pour qu'au cas où la personne l'avait supprimé, il revient après
            self.repete = True
            self.tour+=1
            self.indicateur = 1 #Ici, pour montrer le mots d'encouragement
            self.choix = self.intelligencia_2()
            self.liste_des_boutons.remove(self.choix)
            self.liste_cliquer.append(self.choix)
            self.choix.configure(text = 'X',fg = 'red',cursor = 'arrow')
            self.status = True ; self.compteur = len(self.liste_cliquer)
            #Ici, on montre le text sur l'écran 
            #self.indicateur=0
        else:
            pass

    def choix_de_la_personne(self,bouton:tk.Button):
        """Cette fonction va nous permettre de faire le choix de l'utilisateur """
        self.bouton = bouton
        if self.compteur <9 and self.status == True and self.gagnant == False and self.bouton.cget('text')=='':
            #Ici, on va le supprimer et l'ajouter à la liste des boutons cliqués
            self.liste_cliquer.append(self.bouton)
            self.liste_des_boutons.remove(self.bouton)
            if self.bouton in self.liste_premier_choix:
                self.liste_premier_choix.remove(self.bouton)
            self.bouton.configure(text = 'O',fg = 'blue',cursor = 'arrow')
            self.status = False ; self.compteur = len(self.liste_cliquer)
            self.fin = True #Ici, on rétablir la valeur pour que ça soit correct
        else:
            pass

    def joue_ordi(self,level:str):
        """Cette fonction va nous permettre de faire jouer l'ordinateur suivant le niveau du jeu"""
        self.level = level
        if not self.status and self.level == 'Facile':
            self.choix_de_max_facile()
        elif not self.status and self.level == 'Moyen':
            self.choix_de_max_moyen()
        elif not self.status and self.level == 'Difficile':
            self.choix_de_max_difficile()
        else:
            pass
        self.liste_des_labels[2].after(500,lambda : self.joue_ordi(self.level))
    def ask_recommencer(self):
        """Cette fonction va permettre à l'utilisateur de recommencer"""
        message = messagebox.askyesno("Tic Tac Toe: Max te parle","       Max       : \n Veut tu recommencer une nouvelle partie ?")
        if message:
            self.compteur = 0
            self.liste_cliquer = []
            self.liste_des_boutons = list(self.copie)
            self.indicateur = 0
            for i in range(len(self.liste_des_boutons)):
                self.liste_des_boutons[i].configure(bg = 'white',text = '',cursor = 'hand2')
            self.gagnant = False
            self.repete = True
            self.tour = 0
            self.liste_premier_choix = list(self.liste_premier_choix_copie)
        else:
            self.repete = False # En fait, je fais ça parce que si je ne le fais pas, le message va toujours continuer à s'afficher
            self.liste_des_labels[2].after(3000,lambda : self.liste_des_labels[2].configure(bg = 'cyan'))
            #Ici, on le fait pour attirer l'attention de la personne sur cet widget
    def recommencer(self):
        """Cette fonction va nous permettre de recommencer la partie"""
        #Ce sera la première des choses à faire pour attirer l'attention de la personne sur le widget
        
        self.liste_des_labels[2].configure(bg = 'white')
        self.compteur = 0
        self.liste_cliquer = []
        self.liste_des_boutons = list(self.copie)
        self.indicateur = 0
        for i in range(len(self.liste_des_boutons)):
            self.liste_des_boutons[i].configure(bg = 'white',text = '',cursor = 'hand2')
        self.gagnant = False
        self.repete = True
        self.status = True
        self.tour = 0
        self.score = {'utilisateur':0,'max':0}
        self.liste_des_labels[3]['text'] = f'Score de Max : {self.score['max']}'
        self.liste_des_labels[4]['text'] = f'Ton Score : {self.score['utilisateur']}'
        
    def ask_recommencer_2(self,event):
        """Cette fonction va permettre à l'utilisateur de recommencer, c'est pour la partie bind , sur l'icone de max"""
        message = messagebox.askyesno("Tic Tac Toe: Max te parle","       Max       : \n Veut tu recommencer une nouvelle partie ?")
        if message:
            #Ce sera la première des choses à faire pour attirer l'attention de la personne sur le widget
            self.liste_des_labels[2].configure(bg = 'white')
            self.compteur = 0
            self.liste_cliquer = []
            self.liste_des_boutons = list(self.copie)
            self.indicateur = 0
            for i in range(len(self.liste_des_boutons)):
                self.liste_des_boutons[i].configure(bg = 'white',text = '',cursor = 'hand2')
            self.gagnant = False
            self.repete = True
            self.tour = 0
            
        else:
            self.repete = False # En fait, je fais ça parce que si je ne le fais pas, le message va toujours continuer à s'afficher
            
    def victoire_utilisateur(self):
        """Cette fonction va nous permettre de faire la cérémonie de la victoire pour l'utilisateur"""
        self.compteur = 10 #Ici, je mets le compteur à 10 pour que personne d'autre ne puisse jouer après
        self.indicateur = 2
        self.score['utilisateur'] +=10
        self.liste_des_labels[3]['text'] = f'Score de Max : {self.score['max']}'
        self.liste_des_labels[4]['text'] = f'Ton Score : {self.score['utilisateur']}'
        self.gagnant = True #Nous avons un gagnant
        self.status = True #Nécéssaire pour que le choix se fasse par l'utilisateur au début

    def victoire_ordi(self):
        """Cette fonction va nous permettre de faire la cérémonie de victoire de l'ordinateur"""
        self.compteur = 10 #Ici, je mets le compteur à 10 pour que personne d'autre ne puisse jouer après
        self.indicateur = 3
        self.score['max'] +=10
        self.liste_des_labels[3]['text'] = f'Score de Max : {self.score['max']}'
        self.liste_des_labels[4]['text'] = f'Ton Score : {self.score['utilisateur']}'
        self.gagnant = True #Nous avons un gagnant
        self.status = False # Alors l'ordinateur commence en premier
    def verifier(self):
        """Cette fonction va nous permettre de vérifier chaque fois si quelqu'un a gagné"""
        if not self.gagnant:
            if self.copie[0].cget('text') == "O" and self.copie[1].cget('text') == "O" and self.copie[2].cget('text') == 'O':
                self.copie[0].configure(bg = 'red') ; self.copie[1].configure(bg = 'red') ; self.copie[2].configure(bg = 'red')
                #Ici, on affiche que l'utilisateur a gagné, et on le félicite
                self.victoire_utilisateur()

            if self.copie[3].cget('text') == "O" and self.copie[4].cget('text') == "O" and self.copie[5].cget('text') == 'O':
                self.copie[3].configure(bg = 'red') ; self.copie[4].configure(bg = 'red') ; self.copie[5].configure(bg = 'red')
                #Ici, on affiche que l'utilisateur a gagné, et on le félicite
                self.victoire_utilisateur()

            if self.copie[6].cget('text') == "O" and self.copie[7].cget('text') == "O" and self.copie[8].cget('text') == 'O':
                self.copie[6].configure(bg = 'red') ; self.copie[7].configure(bg = 'red') ; self.copie[8].configure(bg = 'red')
                #Ici, on affiche que l'utilisateur a gagné, et on le félicite
                self.victoire_utilisateur()

            if self.copie[0].cget('text') == "O" and self.copie[3].cget('text') == "O" and self.copie[6].cget('text') == 'O':
                self.copie[0].configure(bg = 'red') ; self.copie[3].configure(bg = 'red') ; self.copie[6].configure(bg = 'red')
                #Ici, on affiche que l'utilisateur a gagné, et on le félicite
                self.victoire_utilisateur()

            if self.copie[1].cget('text') == "O" and self.copie[4].cget('text') == "O" and self.copie[7].cget('text') == 'O':
                self.copie[1].configure(bg = 'red') ; self.copie[4].configure(bg = 'red') ; self.copie[7].configure(bg = 'red')
                #Ici, on affiche que l'utilisateur a gagné, et on le félicite
                self.victoire_utilisateur()
            
            if self.copie[2].cget('text') == "O" and self.copie[5].cget('text') == "O" and self.copie[8].cget('text') == 'O':
                self.copie[2].configure(bg = 'red') ; self.copie[5].configure(bg = 'red') ; self.copie[8].configure(bg = 'red')
                #Ici, on affiche que l'utilisateur a gagné, et on le félicite
                self.victoire_utilisateur()

            if self.copie[0].cget('text') == "O" and self.copie[4].cget('text') == "O" and self.copie[8].cget('text') == 'O':
                self.copie[0].configure(bg = 'red') ; self.copie[4].configure(bg = 'red') ; self.copie[8].configure(bg = 'red')
                #Ici, on affiche que l'utilisateur a gagné, et on le félicite
                self.victoire_utilisateur()

            if self.copie[2].cget('text') == "O" and self.copie[4].cget('text') == "O" and self.copie[6].cget('text') == 'O':
                self.copie[2].configure(bg = 'red') ; self.copie[4].configure(bg = 'red') ; self.copie[6].configure(bg = 'red')
                #Ici, on affiche que l'utilisateur a gagné, et on le félicite
                self.victoire_utilisateur()

            #Maintenant , c'est l'heure de définir la même chose pour la victoire de l'ordinateur
            if self.copie[0].cget('text') == "X" and self.copie[1].cget('text') == "X" and self.copie[2].cget('text') == 'X':
                self.copie[0].configure(bg = 'blue') ; self.copie[1].configure(bg = 'blue') ; self.copie[2].configure(bg = 'blue')
                #Ici, on affiche que l'ordinateur a gagné, et on le félicite
                self.victoire_ordi()
            
            if self.copie[3].cget('text') == "X" and self.copie[4].cget('text') == "X" and self.copie[5].cget('text') == 'X':
                self.copie[3].configure(bg = 'blue') ; self.copie[4].configure(bg = 'blue') ; self.copie[5].configure(bg = 'blue')
                #Ici, on affiche que l'ordinateur a gagné, et on le félicite
                self.victoire_ordi()
            
            if self.copie[6].cget('text') == "X" and self.copie[7].cget('text') == "X" and self.copie[8].cget('text') == 'X':
                self.copie[6].configure(bg = 'blue') ; self.copie[7].configure(bg = 'blue') ; self.copie[8].configure(bg = 'blue')
                #Ici, on affiche que l'ordinateur a gagné, et on le félicite
                self.victoire_ordi()
            
            if self.copie[0].cget('text') == "X" and self.copie[3].cget('text') == "X" and self.copie[6].cget('text') == 'X':
                self.copie[0].configure(bg = 'blue') ; self.copie[3].configure(bg = 'blue') ; self.copie[6].configure(bg = 'blue')
                #Ici, on affiche que l'ordinateur a gagné, et on le félicite
                self.victoire_ordi()
            
            if self.copie[1].cget('text') == "X" and self.copie[4].cget('text') == "X" and self.copie[7].cget('text') == 'X':
                self.copie[1].configure(bg = 'blue') ; self.copie[4].configure(bg = 'blue') ; self.copie[7].configure(bg = 'blue')
                ##Ici, on affiche que l'ordinateur a gagné, et on le félicite
                self.victoire_ordi()
            
            if self.copie[2].cget('text') == "X" and self.copie[5].cget('text') == "X" and self.copie[8].cget('text') == 'X':
                self.copie[2].configure(bg = 'blue') ; self.copie[5].configure(bg = 'blue') ; self.copie[8].configure(bg = 'blue')
                #Ici, on affiche que l'ordinateur a gagné, et on le félicite
                self.victoire_ordi()
            
            if self.copie[0].cget('text') == "X" and self.copie[4].cget('text') == "X" and self.copie[8].cget('text') == 'X':
                self.copie[0].configure(bg = 'blue') ; self.copie[4].configure(bg = 'blue') ; self.copie[8].configure(bg = 'blue')
                #Ici, on affiche que l'ordinateur a gagné, et on le félicite
                self.victoire_ordi()
            
            if self.copie[2].cget('text') == "X" and self.copie[4].cget('text') == "X" and self.copie[6].cget('text') == 'X':
                self.copie[2].configure(bg = 'blue') ; self.copie[4].configure(bg = 'blue') ; self.copie[6].configure(bg = 'blue')
                #Ici, on affiche que l'ordinateur a gagné, et on le félicite
                self.victoire_ordi()
            if self.compteur == 9 and self.gagnant == False:
                #Ici, je mettrai le compteur à 10 pour que cette condition ne s'opère plus
                self.compteur = 10
                self.indicateur = 4
                self.ask_recommencer()
                
                self.status = True
        if self.gagnant and self.repete:
            self.ask_recommencer()
            #Ici, on va faire la demande de recommencer
        self.liste_des_labels[0].after(50,self.verifier)
    


class jeu(tk.Frame):
    """Cette fenêtre est pour le jeu principal"""
    def __init__(self,master,chemin):
        super().__init__(master)
        self.chemin = chemin
        #Ici, on va placer les widgets sur la frame
        self.widgets()
        #Ici, on met dans une liste tous les boutons disponibles pour pouvoir savoir celle qui ont été cliqués
        self.liste_de_boutons = [self.bouton_1,self.bouton_2,self.bouton_3,self.bouton_4,self.bouton_5,self.bouton_6,self.bouton_7,self.bouton_8,self.bouton_9]
        #Ici, on met la liste de tout les labels présents sur la fenêtre
        self.liste_de_labels = [self.label_1,self.label_2,self.label_3,self.label_4,self.label_5]
        #Ici, on aura la liste des mots de max
        self.mots = ['Incroyable 😊🤩 \t Hum ...','Formidable 🫡🤩 \t Une seconde ...','Jolie coup 🫡😎 \t Bon ...','Pas mal 😏 \t  ...',
                     "c'est Super....😎 \t Une seconde ...","Interressant....😏 \t Veillons voir ...","Waouh 😎🫡 \t Boon ...",
                     'Formidable 🫡🤩 \t Une seconde ...','Jolie coup 🫡😎 \t Bon ...',"Interressant....😏 \t Veillons voir ..."]

        #Ici, on va créer la classe concernant la partie façile
        self.Niveau = niveau(self.liste_de_boutons,self.mots,self.liste_de_labels)
 
        # Ici, on va initier un thread pour faire la vérification à chaque fois
        Thread(target = self.after,args = (50,self.Niveau.verifier),daemon = True).start()
        

    def widgets(self):
        """Cette fonction va nous permettre de placer les widgets sur l'ecran, je parle des cases pour le jeu""" 
        #Ici, on va placer deux widgets , autrement sur l'écran pour placer le score et le niveau , et celui qui joue maintenant   
        #Ensemble, on a six boutons qui vont représenter les boutons qu'on va packer sur l'écran
        self.bouton_1 = tk.Button(self,font = ('Verdana',90),bd= 2,cursor='hand2',bg = 'white')
        self.bouton_2 = tk.Button(self,font = ('Verdana',90),bd= 2,cursor='hand2',bg = 'white')
        self.bouton_3 = tk.Button(self,font = ('Verdana',90),bd= 2,cursor='hand2',bg = 'white')
        self.bouton_4 = tk.Button(self,font = ('Verdana',90),bd= 2,cursor='hand2',bg = 'white')
        self.bouton_5 = tk.Button(self,font = ('Verdana',90),bd= 2,cursor='hand2',bg = 'white')
        self.bouton_6 = tk.Button(self,font = ('Verdana',90),bd= 2,cursor='hand2',bg = 'white')
        self.bouton_7 = tk.Button(self,font = ('Verdana',90),bd= 2,cursor='hand2',bg = 'white')
        self.bouton_8 = tk.Button(self,font = ('Verdana',90),bd= 2,cursor='hand2',bg = 'white')
        self.bouton_9 = tk.Button(self,font = ('Verdana',90),bd= 2,cursor='hand2',bg = 'white')
        
        #Ici, on va placer le bouton qui va nous permettre de revenir en arrière,c'est-à-dire le menu
        self.bouton_10 = tk.Button(self,font = ('Verdana',20),bd = 2,fg = 'blue',text = 'Retour au menu',activeforeground='red',cursor='hand2',bg = 'white')
        #Définition de la photo qu'on va packer sur le label_3
        self.photo = ImageTk.PhotoImage(Image.open(self.chemin))
        #Ici, on place les labels qui vont afficher des informations sur l'écran
        self.label_1 = tk.Label(self,text ='Niveau : ',font = ("Verdana",20),fg = 'blue',anchor = 'w',bg = 'white')
        self.label_2 = tk.Label(self,image =self.photo ,bg = 'white',cursor='hand2')
        self.label_3 = tk.Label(self,font = ('Verdana',20),text = 'Max: ',fg = 'red',anchor = 'w',bg = 'white',wraplength=500,cursor = 'hand2')
        self.label_4 = tk.Label(self,font = ('Verdana',20),text = 'Score de Max: ',fg = 'red',relief = 'ridge',bg = 'white',cursor = 'hand2')
        self.label_5 = tk.Label(self,font = ("Verdana",20),text = 'Ton score :',fg = 'blue',anchor = 'w',relief = 'ridge',bg = 'white',cursor = 'hand2')

        #Placer les widgets sur l'écran selon l'ordre d'apparition
        self.label_1.place(relx = 0,rely = 0,relheight = 0.05,relwidth = 0.5)
        self.bouton_10.place(relx = 0.5,rely = 0,relheight = 0.05,relwidth = 0.5)
        #Placer les autres widgets
        self.bouton_1.place(relx = 0,rely = 0.05,relheight=(0.8/3),relwidth = (1/3))
        self.bouton_2.place(relx = (1/3),rely = 0.05,relheight=(0.8/3),relwidth = (1/3))
        self.bouton_3.place(relx = (2/3),rely = 0.05,relheight=(0.8/3),relwidth = (1/3))
        self.bouton_4.place(relx = 0,rely = 0.05+(0.8/3),relheight=(0.8/3),relwidth = (1/3))
        self.bouton_5.place(relx = (1/3),rely = 0.05+(0.8/3),relheight=(0.8/3),relwidth = (1/3))
        self.bouton_6.place(relx = (2/3),rely = 0.05+(0.8/3),relheight=(0.8/3),relwidth = (1/3))
        self.bouton_7.place(relx = 0,rely = 0.05+2*(0.8/3),relheight=(0.8/3),relwidth = (1/3))
        self.bouton_8.place(relx = (1/3),rely = 0.05+2*(0.8/3),relheight=(0.8/3),relwidth = (1/3))
        self.bouton_9.place(relx = (2/3),rely = 0.05+2*(0.8/3),relheight=(0.8/3),relwidth = (1/3))
        #Placement des autres labels pour l'affichage
        self.label_2.place(relx = 0, rely = 0.05+(3*(0.8/3)), relheight =0.1 ,relwidth = 1/3)
        self.label_3.place(relx = 1/3, rely = 0.05+(3*(0.8/3)) , relheight = 0.1,relwidth = 2/3)
        self.label_4.place(relx = 0, rely = 0.15+(3*(0.8/3)), relheight =0.05 ,relwidth =0.5 )
        self.label_5.place(relx = 0.5, rely = 0.15+(3*(0.8/3)), relheight =0.05 ,relwidth =0.5 )
   

#Ici, on a définir les chemins des fichiers dont on aura besoin

chemin_perso = ttt.chemin_fichier('photo.png')
chemin_mascotte = ttt.chemin_fichier('mascotte.png')
chemin_fond = ttt.chemin_fichier("fond.ico")
class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tic Tac Toe')
        self.geometry("800x600")
        self.iconbitmap(chemin_fond)
        #Définition de la page d'accueil
        self.page0 = page_1(self)

        # Placement de la fenêtre d'accueil
        self.page0.place(x = 0,y = 0,relwidth=1,relheight=1)
        
        #Définition de la page de jeu même
        self.page1 = jeu(self,chemin_mascotte)

        #Définition de la page de présentation de max
        self.page_presentation = page_2(self,chemin_perso)
        #Définition de la fonction du bouton de la page d'accueil
        self.page0.bouton.configure(command=lambda :Thread(target = self.fonction_du_bouton1,daemon = True).start())

        #Définition de la fonction du bouton retour de la page 1
        self.page1.bouton_10.configure(command = lambda : Thread(target = self.fonction_du_bouton10,daemon = True).start())

        #Ici, on définit l'évenement qui va faire que la frame va se détruite
        Thread(target = self.page_presentation.label_supp.bind,args = ('<Button-1>',self.fonction_bind ),daemon = True).start()
        
        #Ici, on établie ce qui va se passer si on ferme la fenêtre active
        self.wm_protocol("WM_DELETE_WINDOW",self.quitter)
        
        
    #Ici, nous établissons les fonctions dont nous aurons besoin dans la suite de notre développement

    def fonction_du_bouton1(self):
        """Cette fonction nous permet d'énumérer les fonctions du bouton 1 et de les mettre en un seul bloc"""
        self.page_presentation.place(relx = 0,rely = 0,relheight=1,relwidth=1)
        self.page0.place_forget()
        self.page1.label_1.configure(text = f"Niveau : {self.page0.var.get()}")
        Thread(target = self.page_presentation.alleger,daemon = True).start()
        #Ici, on va faire de tels sorte qu'il y aura ici quelque chose qui va vérifier à chaque fois si c'est l'ordinateur qui joue
        Thread(target = self.page1.Niveau.liste_des_labels[1].after,args = (500,self.page1.Niveau.joue_ordi(self.page0.var.get())),daemon = True).start()
        #Ici, nous allons faire l'initialisation de chaque niveau
        self.page1.Niveau.configuration()
    def fonction_du_bouton10(self):
        """Cette fonction nous permet d'énumérer les fonctions du bouton2"""
        self.voila = messagebox.askokcancel("Tic Tac Toe : Max te parle","Max :\n Retourner au menu")
        if self.voila:
            Thread(target = self.page1.Niveau.recommencer,daemon = True).start()
            self.page1.place_forget()
            self.page0.place(x = 0,y = 0,relheight = 1,relwidth=1)
        else:
            pass
        
    def fonction_bind(self,event):
        """Cette fonction va nous permettre de binder la page de présentation pour qu'il puisse afficher la frame de jeu"""
        self.page_presentation.place_forget()
        self.page1.place(relx = 0,rely = 0,relheight=1,relwidth=1)

    def quitter(self):
        """Cette fonction va nous permettre de quitter la fenêtre après une interrogation de max"""
        message = messagebox.askyesno("Tic Tac Toe: Max te parle","Max:\nVeux tu fermer la fenêtre active ?")
        if message:
            self.destroy()
        else:
            pass

#Exécution de l'app 
application = app() #Ici, c'est parce que la majorité des fonctions que nous utilisons sont dans l'initialisation

#Enfin, on a ceci en dernier position
application.mainloop()