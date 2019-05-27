import bpy

def ShowMessageBox(message = "", title = "Message Box", icon = 'INFO'):

    def draw(self, context):
        self.layout.label(message)

    bpy.context.window_manager.popup_menu(draw, title = title, icon = icon)


#Shows a message box with a specific message 
ShowMessageBox("This is text in game engine property: ") 

#player = sce.objects['atom model']
#moves = player.get('mainVar')
#print(moves)
player = bge.sce.objects['Lamp']
moves = player.get('lampProp')
ShowMessageBox(moves) 
