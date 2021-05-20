from kivymd.app import MDApp
from kivy.lang import Builder



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
        icon: 'python.png'
        user_font_size: '64sp'            
    MDTextField:
        id: data
        hint_text: 'E-mail'
        icon_right: 'account'
        icon_right_color: [0,1,0,1]
        helper_text: 'example@gmail.com'
        helper_text_mode: 'on_focus'
        pos_hint: {'center_x': .5, 'center_y': .6} 
        size_hint_x: .5                 
    MDTextField:
        size_hint_x: .5
        hint_text: "Senha"        
        pos_hint: {'center_x': .5, 'center_y': .5}
        password: True
        password: '*'
    MDRaisedButton:        
        text: 'Login'        
        pos_hint: {'center_x': .5, 'center_y': .4}
        size_hint_x: .3
        on_press: app.get_data()
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
        print(self.root.ids.data.text)
        return Builder.load_string(kv)       
    


Team80App().run()