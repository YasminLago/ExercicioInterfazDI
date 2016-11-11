import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk


# Compoñentes usados: Box, Grid, Entry, CheckButton, ComboBox
# print(dir(text1.props)) Ver propiedades dos compoñentes

# Creamos unha lista cos datos que queremos que aparezcan no ComboBox
combo = ["Ecoloxista"], \
        ["e"],\
        ["xa"],\
        ["está"]

# Creamos a clase e o constructor
class UserInterface(Gtk.Window):
    def __init__(self):
        # Creamos a ventana
        Gtk.Window.__init__(self, title = "Exercicio Interfaz")

        self.set_border_width(10)

        # Creamos a caixa que contendrá todos os elementos e a engadimos a ventana
        caixaV = Gtk.Box(orientation="GTK_ORIENTATION_VERTICAL", spacing=60)
        self.add(caixaV)

        # Creamos as pestañas e as engadimos na caixa creada anteriormente
        notebook = Gtk.Notebook()
        caixaV.add(notebook)

        grid = Gtk.Grid()# Crease o Grid para organizar os elementos


        # Se crea unha variable tipo ListStore no que se gardara o contido da lista
        lista = Gtk.ListStore(str)
        for i in range(len(combo)):
            lista.append(combo[i])


        # Creamos os compoñentes que queremos mostrar
        etiqueta1 = Gtk.Label("Cif")
        etiqueta2 = Gtk.Label("Denominación")
        etiqueta3 = Gtk.Label("Provincia")
        etiqueta4 = Gtk.Label("Finalidade")
        check1 = Gtk.CheckButton("Pública")

        text1 = Gtk.Entry()
        text2 = Gtk.Entry()
        text3 = Gtk.Entry()

        # Crease o ComboBox e mostranse os elementos cargados no ListStore
        cbox = Gtk.ComboBox(model=lista)

        renderer = Gtk.CellRendererText()
        cbox.pack_start(renderer, True)
        cbox.add_attribute(renderer, 'text', 0)
        cbox.set_active(0) # Inicia o ComboBox na primeira posición da lista

        boton1 = Gtk.Button("Anterior")
        boton2 = Gtk.Button("Seguinte")
        boton3 = Gtk.Button("Modificar")

        # Caixa que contén os elementos da primeira pestaña
        pestaña1 = Gtk.Box()
        pestaña1.set_border_width(10) #Margenes
        pestaña1.add(grid)
        grid.add(etiqueta1)

        # Posicionanse os compoñentes dentro da pestaña1
        grid.attach_next_to(text1, etiqueta1, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(etiqueta2, etiqueta1, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(text2, etiqueta2, Gtk.PositionType.RIGHT, 2, 1)
        grid.attach_next_to(etiqueta3, etiqueta2, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(text3, etiqueta3, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(etiqueta4, etiqueta3, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(cbox, etiqueta4, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(check1, etiqueta4, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(boton1, check1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(boton2, boton1, Gtk.PositionType.RIGHT, 1, 2)
        grid.attach_next_to(boton3, boton2, Gtk.PositionType.RIGHT, 1, 2)


        notebook.append_page(pestaña1, Gtk.Label("Editar"))


        pestaña2 = Gtk.Box()
        pestaña2.set_border_width(10)
        notebook.append_page(pestaña2, Gtk.Label("Visualizar"))


        self.connect("delete-event", Gtk.main_quit)
        self.show_all()

ejecucion = UserInterface()
Gtk.main()

