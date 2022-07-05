from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivy.uix.boxlayout import BoxLayout
import sqlite3

class Content(BoxLayout):
    pass

class login(MDApp):
    pass

    def showDialog(self):
        print(self.root.ids)
        self.user = self.root.ids.username.text

        #self.dialog = MDDialog(
        #    title="What would you like to do " + self.user ,
        #    text="Ready to login?",
        #    radius=[20, 7, 20, 7],
        #    buttons=[
        #        MDFlatButton(text="CANCEL"), MDRaisedButton(text="DISCARD"),
        #    ],
        #)

        self.dialog = MDDialog(
                text="Discard draft?",
                type="custom",
                content_cls=Content(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="DISCARD",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )

        self.dialog.open()

    def loginBtnClick(self):       
       #check if username = admin and password = jumpjump
       #would be if the username of password is incorrect show a different dialog 
       self.showDialog();

    def signUpBtnClick(self):       
        # Create Database Or Connect To One
        conn = sqlite3.connect('myappdb.db')

        # Create A Cursor
        c = conn.cursor()

        # Create A Table
        c.execute("""CREATE TABLE if not exists users(
            username text, password text)
            """)

        # insert user info
        c.execute("""insert into 
            users (username, password) 
            values ('""" + self.root.ids.username.text + "','" +  self.root.ids.password.text + """')
            """)


        # Commit our changes
        conn.commit()

        # Close our connection
        conn.close()

if __name__=="__main__":
    window = login()
    window.run()
