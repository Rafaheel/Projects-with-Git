from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.image import Image


kv = '''
Screen:
    BoxLayout:
        orientation: 'vertical'        
        MDToolbar:
            title: "Team 80"            
            left_action_items: [["menu", lambda x: app.callback()]]
            right_action_items: [["dots-vertical", lambda x: app.callback()]]
        FormLogin:

<FormLogin@FloatLayout>:          
    MDIconButton:
        pos_hint: {'center_x': .5, 'center_y': .8}        
        icon: 'language-python'
        user_font_size: '75sp'
    MDTextField:
        size_hint_x: .5
        hint_text: 'E-mail'
        pos_hint: {'center_x': .5, 'center_y': .6}                  
    MDTextField:
        size_hint_x: .5
        hint_text: "Senha"        
        pos_hint: {'center_x': .5, 'center_y': .5}
    MDRaisedButton:        
        text: 'Login'        
        pos_hint: {'center_x': .5, 'center_y': .4}
        size_hint_x: .3
    MDTextButton:
        text: "Cadastre?"
        pos_hint: {'center_x': .5, 'center_y': .2}
        halign: "center"
    MDTextButton:
        text: "Esqueceu sua senha?"
        pos_hint: {'center_x': .5, 'center_y': .1}
        halign: "center"           
'''


class Team80App(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "LightGreen"
        self.theme_cls.theme_style = "Dark"        
        return Builder.load_string(kv)


Team80App().run()