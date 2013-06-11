#coding=UTF-8

from gi.repository import Gtk
from simesc.interpreter import util
from simesc.interpreter import DynamicInterpreter, StaticInterpreter

class MainWindow(object):
    arrayCode = None
    interpreter = None
    
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

        self.variablesTextView = self.builder.get_object("variablesTextView")
        self.variablesTextBuffer = self.builder.get_object("variablesTextBuffer")
        self.varTextTag = self.variablesTextBuffer.create_tag("codeFont", font="Mono 10")

        self.stackTextView = self.builder.get_object("stackTextView")
        self.stackTextBuffer = self.builder.get_object("stackTextBuffer")
        self.stackTextTag = self.stackTextBuffer.create_tag("codeFont", font="Mono 10")

        self.textTag = self.codeTextBuffer.create_tag("codeFont", font="Mono 10")
        self.selectedLine = self.codeTextBuffer.create_tag("selectedLine")
        self.selectedLine.set_property("background-full-height", True)
        self.selectedLine.set_property("background", "yellow")
        self.interpreterType = self.builder.get_object("interpreterType")
        self.interpreterType.set_active(0)
        
        self.set_interpreter()

    def set_interpreter(self):
        if self.arrayCode:
            if self.interpreterType.get_active() == 0 and\
               (type(self.interpreter) == StaticInterpreter or self.interpreter == None):
                self.interpreter = DynamicInterpreter(self.arrayCode)
            elif self.interpreterType.get_active() == 1 and\
               (type(self.interpreter) == DynamicInterpreter or self.interpreter == None):
                self.interpreter = StaticInterpreter(self.arrayCode)


    def openFile(self, filename):
        self.arrayCode = util.load_file(filename)
        self.interpreter = None
        self.set_interpreter()
        self.currentLine = self.interpreter.position
        self.updateCode()
        
    def updateCode(self):
        self.codeTextBuffer.set_text(util.code_from_array(self.arrayCode, self.currentLine))
        self.codeTextBuffer.apply_tag(self.textTag, self.codeTextBuffer.get_start_iter(), self.codeTextBuffer.get_end_iter())
        self.codeTextBuffer.apply_tag(self.selectedLine, self.codeTextBuffer.get_iter_at_line(self.currentLine), self.codeTextBuffer.get_iter_at_line(self.currentLine+1))
        self.codeTextView.set_buffer(self.codeTextBuffer)
        
    def updateStack(self):
        stack = self.interpreter.stack
        a = "Stack:\n"
        for s in reversed(stack.stack):
            a = a + "----------------\n"
            a = a + "Funcao: %s\n"%s.function_name
            a = a + "Callback: %s\n"%s.callback
            a = a + "Parametros: %s\n"%s.parameters
        self.stackTextBuffer.set_text(a)
        self.stackTextView.set_buffer(self.stackTextBuffer)
    
    def updateVariables(self):
        self.variablesTextBuffer.set_text("Variaveis:\n%s"%"\n".join(["%s: %s"%(a,b) for a,b in self.interpreter.variables.iteritems()]))
        self.variablesTextView.set_buffer(self.variablesTextBuffer)

    ###########
    # Signals #
    ###########
    
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)

    def onStepClick(self, widget):
        self.interpreter.step()
        self.currentLine = self.interpreter.position 
        self.updateCode()
        self.updateStack()
        self.updateVariables()

    def onChangeType(self, *args):
        self.set_interpreter()
            
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

    def start_main_loop(self):
        Gtk.main()
        
