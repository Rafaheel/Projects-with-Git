from kivymd.app import MDApp
from kivymd.uix.card import MDCard 
from kivy.app import App
from kivymd.theming import ThemeManager





class Myapp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "LightGreen"
        self.theme_cls.theme_style = "Dark"        
        return
    def get_email(self):
        email = self.root.ids.email.text
        print(email.strip())
        #print("The data of text field is :: ",self.root.ids.email.text) 
    def get_senha(self):
        #print("The data of text field is :: ",self.root.ids.senha.text)
        senha = self.root.ids.senha.text
        print(senha)    
    def cadastrar(self):
        print("Ainda não deu certo, mas é por aqui")  
        teste = self.root.ids.cadastrar.text
        print(teste)           
    def validacao(self):
        email = str(self.root.ids.email.text)
        senha = str(self.root.ids.senha.text)
        if senha == "1234" and email == 'rafael@gmail.com':
            print("tudo certo")
        else:
            print("tudo errado igual a sua vida!")        

Myapp().run()