#coding=UTF-8

from gi.repository import Gtk

from simesc.interpreter import util

class MainWindow(object):
    def __init__(self):
        self.arrayCode = util.load_file("simesc.py")
        
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
        self.codeTextBuffer = self.builder.get_object("codeTextBuffer")
        self.textTag = self.codeTextBuffer.create_tag("codeFont", font="Mono 10")
        self.selectedLine = self.codeTextBuffer.create_tag("selectedLine")
        self.selectedLine.set_property("background-full-height", True)
        self.selectedLine.set_property("background", "yellow")

    def onOpenItem(self, *args):
        self.builder.get_object("filechooserdialog1").show_all()
        
        
    def lala(self, *args):
        print args
        self.builder.get_object("filechooserdialog1").hide_all()        
        self.codeTextBuffer.set_text(util.code_from_array(self.arrayCode, 3))
        self.codeTextBuffer.apply_tag(self.textTag, self.codeTextBuffer.get_start_iter(), self.codeTextBuffer.get_end_iter())
        self.codeTextBuffer.apply_tag(self.selectedLine, self.codeTextBuffer.get_iter_at_line(3), self.codeTextBuffer.get_iter_at_line(4))
        self.codeTextView.set_buffer(self.codeTextBuffer)
        
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def teste(self, widget):
        # Altera o número no campo
        self.clicks=self.clicks+1
        self.builder.get_object("entry1").set_text("%d"%self.clicks)
        
    def start_main_loop(self):
        Gtk.main()
        