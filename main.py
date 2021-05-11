from gi.repository import Gtk

class MainWindow(Gtk.Window):
    #self init function
    def __init__(self):
        Gtk.Window.__init__(self,title="Gnome gtk app")

        # Button
        self.button = Gtk.Button(label="Click me!")
        self.button.connect("clicked",self.button_clicked)
        self.add(self.button)

    # User clicks button
    def button_clicked(self,widget):
        print("This Works!")



# initial window setup
window = MainWindow()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()




