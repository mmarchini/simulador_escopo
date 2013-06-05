#coding=UTF-8

from gi.repository import Gtk
from simesc.interpreter import util

class MainWindow(object):
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
        self.codeTextBuffer = self.builder.get_object("codeTextBuffer")
        self.textTag = self.codeTextBuffer.create_tag("codeFont", font="Mono 10")
        self.selectedLine = self.codeTextBuffer.create_tag("selectedLine")
        self.selectedLine.set_property("background-full-height", True)
        self.selectedLine.set_property("background", "yellow")
        self.builder.get_object("interpreterType").set_active(0)

    def onChangeType(self, *args):
        print args
        print args[0].get_active()

    def onOpenItem(self, *args):
        fileChooser = Gtk.FileChooserDialog("Escolha um Arquivo", 
                                            self.builder.get_object("window1"),
                                            action=Gtk.FileChooserAction.OPEN, 
                                            buttons=
                                            (Gtk.STOCK_CANCEL,Gtk.ResponseType.CANCEL,
                                             Gtk.STOCK_OPEN,Gtk.ResponseType.OK)
                                            )
        response = fileChooser.run()
        if response == Gtk.ResponseType.OK:
            self.openFile(fileChooser.get_filename())
        fileChooser.destroy()

    def openFile(self, filename):
        self.arrayCode = util.load_file(filename)
        self.currentLine = 0
        self.updateCode()
        
    def updateCode(self):
        self.codeTextBuffer.set_text(util.code_from_array(self.arrayCode, self.currentLine))
        self.codeTextBuffer.apply_tag(self.textTag, self.codeTextBuffer.get_start_iter(), self.codeTextBuffer.get_end_iter())
        self.codeTextBuffer.apply_tag(self.selectedLine, self.codeTextBuffer.get_iter_at_line(self.currentLine), self.codeTextBuffer.get_iter_at_line(self.currentLine+1))
        self.codeTextView.set_buffer(self.codeTextBuffer)
        
    def updateStack(self):
        pass
    
    def updateVariables(self):
        pass
    
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onStepClick(self, widget):
        #TODO vinculação com interpretador
        self.currentLine = self.currentLine+1
        self.updateCode()
        self.updateStack()
        self.updateVariables()
        
    def start_main_loop(self):
        Gtk.main()
        