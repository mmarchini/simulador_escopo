#encoding=UTF-8
#!/usr/bin/env python

from gi.repository import Gtk

class  Teste:    
    def __init__(self):
        # Carrega o template feito no glade
        filename = "simesc/interface/templates/main.glade"
        builder = Gtk.Builder()
        builder.add_from_file(filename)
        self.builder=builder
        # Associa os eventos as suas respectivas funções
        self.builder.connect_signals(self)

#        Exibe o template na tela 
        self.builder.get_object("window1").show_all()
        self.codeTextView = self.builder.get_object("codeTextView")
        self.codeTextView.set_wrap_mode(Gtk.WrapMode.NONE)
        self.codeTextBuffer = self.builder.get_object("codeTextBuffer")
        self.codeTextBuffer.set_text("""
#encoding=UTF-8
#!/usr/bin/env python

from gi.repository import Gtk

class  Teste:    
    def __init__(self):
        # Carrega o template feito no glade
        filename = "simesc/interface/templates/main.glade"
        builder = Gtk.Builder()
        builder.add_from_file(filename)
        self.builder=builder
        # Associa os eventos as suas respectivas funções
        self.builder.connect_signals(self)

#        Exibe o template na tela 
        self.builder.get_object("window1").show_all()
        self.codeTextView = self.builder.get_object("codeTextView").show_all()
        self.text_buffer = Gtk.TextBuffer()
        self.codeTextView.set_buffer(self.text_buffer)
        

        # Altera o número no campo
#         self.clicks=0
#         self.builder.get_object("entry1").set_text("%d"%self.clicks)

    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def teste(self, widget):
        # Altera o número no campo
        self.clicks=self.clicks+1
        self.builder.get_object("entry1").set_text("%d"%self.clicks)

app = Teste()
# Inicia o main loop do GTK
Gtk.main()
        
        """)
        self.codeTextView.set_buffer(self.codeTextBuffer)
        

        # Altera o número no campo
#         self.clicks=0
#         self.builder.get_object("entry1").set_text("%d"%self.clicks)


    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def teste(self, widget):
        # Altera o número no campo
        self.clicks=self.clicks+1
        self.builder.get_object("entry1").set_text("%d"%self.clicks)

app = Teste()
# Inicia o main loop do GTK
Gtk.main()

