from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.list import OneLineAvatarIconListItem, ThreeLineAvatarIconListItem, TwoLineAvatarListItem
from kivy.properties import StringProperty
from kivymd.icon_definitions import md_icons
from kivy.network.urlrequest import UrlRequest
import json
import random

bloglist = []
class ListItemForPosts(TwoLineAvatarListItem):
    '''Custom list item.'''
    icon = StringProperty("android")

class blogApp(MDApp):
    
    def on_start(self):
       self.getPosts()

    def getPosts(self):
        UrlRequest('https://v1.nocodeapi.com/innoventorshq/google_sheets/WRPnrlmVPqPLNuNW?tabId=Sheet1', self.got_json)

    def got_json(self, request, posts):           
        #posts = json.loads(json.dumps(posts))
        #print ("Result: after success", posts)

        #print(posts['data'])
        #print(posts['total'])

        blogposts = posts['data']
        totalCount = posts['total']

        for i in blogposts:
            #print(i["message"])
            bloglist.append (i["message"])
            #print(bloglist)
            #value = posts[i]
            #print("Key and Value pair are {} : {}".format(i, value))

        self.showPosts(bloglist)

    def showPosts(self, postList):
        icons = list(md_icons.keys())
        for blog in bloglist:
            self.root.ids.scroll.add_widget(
                ListItemForPosts(text=blog, icon=icons[random.randint(0,100)])
            )

if __name__=="__main__":
    window = blogApp()
    window.run()
