#encoding=UTF-8
#!/usr/bin/env python

import gtk

class  Teste:    
    def __init__(self):
        # Carrega o template feito no glade
        filename = "teste.glade"
        builder = gtk.Builder()
        builder.add_from_file(filename)
        self.builder=builder
        # Associa os eventos as suas respectivas funções
        self.builder.connect_signals(self)

        # Exibe o template na tela 
        self.builder.get_object("window1").show_all()

        # Altera o número no campo
        self.clicks=0
        self.builder.get_object("entry1").set_text("%d"%self.clicks)

    def teste(self, widget):
        # Altera o número no campo
        self.clicks=self.clicks+1
        self.builder.get_object("entry1").set_text("%d"%self.clicks)

app = Teste()
# Inicia o main loop do GTK
gtk.main()

