# !/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import tkinter.messagebox as msgb
from pathlib import Path

PATH = str((Path(__file__).resolve()).parent)

ICON=r"/imagen/ed.ico"
BD= r"/BD/database.db"
class Inscripciones:
    def __init__(self, master=None):
        # Ventana principal
        self.db_name = PATH + BD   
        self.win = tk.Tk(master)
        self.win.configure(background="#f7f9fd", height=600, width=800)
        self.win.geometry("800x600")
        self.win.iconbitmap(PATH +ICON)
        self.win.resizable(False, False)
        self.win.title("Inscripciones de Materias y Cursos")
        # Crea los frames
        self.frm_1 = tk.Frame(self.win, name="frm_1")
        self.frm_1.configure(background="#f7f9fd", height=600, width=800)
        self.lblNoInscripcion = ttk.Label(self.frm_1, name="lblnoinscripcion")
        self.lblNoInscripcion.configure(background="#f7f9fd",font="{Arial} 11 {bold}",
                                        justify="left",state="normal",
                                        takefocus=False,text='No.Inscripción')
        
        #Label No. Inscripción
        self.lblNoInscripcion.place(anchor="nw", x=670, y=20)
        #Entry No. Inscripción
        self.num_Inscripcion = ttk.Entry(self.frm_1, name="num_inscripcion")
        self.num_Inscripcion.configure(justify="right")
        self.num_Inscripcion.place(anchor="nw", width=100, x=672, y=50)
        
        #Label Fecha
        self.lblFecha = ttk.Label(self.frm_1, name="lblfecha")
        self.lblFecha.configure(background="#f7f9fd", text='Fecha:')
        self.lblFecha.place(anchor="nw", x=630, y=85)
        #Entry Fecha
        self.fecha = ttk.Entry(self.frm_1, name="fecha")
        self.fecha.configure(justify="center")
        self.fecha.place(anchor="nw", width=90, x=680, y=85)

        #Label Alumno
        self.lblIdAlumno = ttk.Label(self.frm_1, name="lblidalumno")
        self.lblIdAlumno.configure(background="#f7f9fd", text='Id Alumno:')
        self.lblIdAlumno.place(anchor="nw", x=30, y=85)
        #Combobox Alumno
        self.cmbx_Id_Alumno = ttk.Combobox(self.frm_1, name="cmbx_id_alumno")
        self.cmbx_Id_Alumno.place(anchor="nw", width=112, x=110, y=85)

        #Label Alumno
        self.lblNombres = ttk.Label(self.frm_1, name="lblnombres")
        self.lblNombres.configure(background="#f7f9fd",text='Nombre(s):')
        self.lblNombres.place(anchor="nw", x=30, y=140)
        #Entry Alumno
        self.nombres = ttk.Entry(self.frm_1, name="nombres")
        self.nombres.place(anchor="nw", width=200, x=110, y=140)

        #Label Apellidos
        self.lblApellidos = ttk.Label(self.frm_1, name="lblapellidos")
        self.lblApellidos.configure(background="#f7f9fd",text='Apellido(s):')
        self.lblApellidos.place(anchor="nw", x=400, y=140)
        #Entry Apellidos
        self.apellidos = ttk.Entry(self.frm_1, name="apellidos")
        self.apellidos.place(anchor="nw", width=200, x=485, y=140)

        #Label Id Curso
        self.lblIdCurso = ttk.Label(self.frm_1, name="lblidcurso")
        self.lblIdCurso.configure(background="#f7f9fd", text='Id Curso:')
        self.lblIdCurso.place(anchor="nw", x=30, y=180)
        #Entry Id Curso
        self.idCurso = ttk.Entry(self.frm_1, name="idcurso")
        self.idCurso.configure(justify="center")
        self.idCurso.place(anchor="nw", width=200, x=110, y=180)
        #Combobox Id Curso
        self.cmbx_Id_Curso = ttk.Combobox(self.frm_1, name="cmbx_id_curso")
        self.cmbx_Id_Curso.place(anchor="nw", width=200, x=110, y=180)

        #Label Curso
        self.lblCurso = ttk.Label(self.frm_1, name="lblcurso")
        self.lblCurso.configure(background="#f7f9fd", text='Curso:')
        self.lblCurso.place(anchor="nw", x=400, y=180)
        #Entry Curso
        self.curso = ttk.Entry(self.frm_1, name="curso")
        self.curso.configure(justify="center")
        self.curso.place(anchor="nw", width=200, x=485, y=180)


        ''' Botones  de la Aplicación'''
        #Botón Guardar
        self.btnGuardar = ttk.Button(self.frm_1, name="btnguardar")
        self.btnGuardar.configure(text='Guardar')
        self.btnGuardar.place(anchor="nw", x=200, y=220)
        #Botón Editar
        self.btnEditar = ttk.Button(self.frm_1, name="btneditar")
        self.btnEditar.configure(text='Editar')
        self.btnEditar.place(anchor="nw", x=300, y=220)
        #Botón Eliminar
        self.btnEliminar = ttk.Button(self.frm_1, name="btneliminar")
        self.btnEliminar.configure(text='Eliminar')
        self.btnEliminar.place(anchor="nw", x=400, y=220)
        #Botón Cancelar
        self.btnCancelar = ttk.Button(self.frm_1, name="btncancelar")
        self.btnCancelar.configure(text='Cancelar')
        self.btnCancelar.place(anchor="nw", x=500, y=220)
        #Separador
        separator1 = ttk.Separator(self.frm_1)
        separator1.configure(orient="horizontal")
        separator1.place(anchor="nw", width=796, x=2, y=260)

        ''' Treeview de la Aplicación'''
        #Treeview
        self.tView = ttk.Treeview(self.frm_1, style="estilo.Treeview") 
        self.tView.configure()
        #Columnas del Treeview
        self.tView["columns"]=("descripcion")
        self.tView.column ("#0", anchor="w", stretch=True,width=5)
        self.tView.column ("descripcion", anchor="w", stretch=True,width=100)
        #Cabeceras
        self.tView.heading("#0", anchor="center", text="Codigo")
        self.tView.heading("descripcion", anchor="center", text="Descripción")

        #Scrollbars
        self.scroll_H = ttk.Scrollbar(self.tView, orient="vertical", command=self.tView.yview)
        self.tView.configure(yscroll=self.scroll_H.set)
        self.scroll_H.place( height=325, x=778, y=25)
        self.tView.place(anchor="nw", height=300, width=790, x=4, y=300)
        self.frm_1.pack(side="top")
        self.frm_1.pack_propagate(0)

        # Main widget
        self.mainwindow = self.win

        def SeleccionVacia(): #Selección del treeview vacia (en realidad es ['', '', '', 0, ''] ), si la seleccion es vacia y se oprime el boton, no de error, se retorna un pass
            if seleccionLinea()[0] == "": 
                return True
            else:
                return False
            
        def actualizarNumInscripcion(): #Actualiza el numero de inscripcción.
            #Selecciona el ultimo registro de Inscritos, la columna en comillas por hacer escape al punto,
            num = cur.execute("SELECT \"No.Inscripción\" FROM Inscritos ORDER BY \"No.Inscripción\" DESC LIMIT 1").fetchone()
            self.nnuminscripciones = tk.StringVar(value = num)
            self.num_Inscripcion.configure(textvariable = self.nnuminscripciones)

        def mensaje():
             msgb.showerror(title='Dato invalido', message="El Dato no es valido")

        #Toma de la Fecha por medio del insert
        def getFecha():
            fecha = self.fecha.get()
            return fecha
            
        def getcmbx(): #Selecciona el id del estudiante destacado en el combobox
            index = self.cmbx_Id_Alumno.current()
            cmbx = valsCmbxAl[index][0]
            return cmbx
        
        def getcmbxCur(): #Selecciona el id del Curso destacado en el combobox
            index = self.cmbx_Id_Curso.current()
            cmbxCur = valsCmbxCur[index][0]
            return cmbxCur
            
        def actualizar(call): #El argumento no se utiliza, pero por ser llamado por un bind, se le coloca argumento.
            #Refresca el Treeview si hay hay elementos en el Treeview
            if len(self.tView.get_children(""))!= 0:
                tViewActual = self.tView.get_children()
                for item in tViewActual:
                    self.tView.delete(item)

            cmbx = getcmbx()

            #Nombre y Apellidos, Para cambiar el label hay que crear un StringVar
            valsNombreApellidos = cur.execute("SELECT Nombres, Apellidos FROM Alumnos WHERE id_Alumno =  \"{}\"".format(cmbx)).fetchone()
            self.nombresvar = tk.StringVar(value = valsNombreApellidos[0])
            self.nombres.configure(textvariable = self.nombresvar)
            self.apellidosvar = tk.StringVar(value = valsNombreApellidos[1])
            self.apellidos.configure(textvariable=self.apellidosvar)
       
            cmbxCur = getcmbxCur()
            #Curso, Para cambiar el label hay que crear un StringVar
            valIdCurso = cur.execute("SELECT Descrip_Curso FROM Cursos WHERE Código_Curso =  \"{}\"".format(cmbxCur)).fetchone()
            self.cursosvar = tk.StringVar(value = valIdCurso[0])
            self.curso.configure(textvariable = self.cursosvar)
               

            #TreeView
            # Hace un INNER JOIN de 3 tabla (Alumnos, Inscritos, Cursos) y selecciona los registros donde el id_alumno coincide con la opcion del combobox
            #Retorna una lista de atributos de cada registro y los inserta en el treeview parent = "" 
            valsTreeview = cur.execute("SELECT Inscritos.Código_Curso, Cursos.Descrip_Curso FROM (Alumnos INNER JOIN Inscritos ON Alumnos.Id_Alumno = Inscritos.Id_Alumno) INNER JOIN Cursos ON Cursos.Código_Curso = Inscritos.Código_Curso WHERE Inscritos.Id_Alumno = \"{}\"".format(cmbx)).fetchall()
            for Curso in range(len(valsTreeview)):
                self.tView.insert(parent = "",index = tk.END, text = valsTreeview[Curso][0], values = valsTreeview[Curso][1:]) #Modificar si hay mas columnas a agregar(solo admite 2)

            actualizarNumInscripcion() #Actualiza el número de inscripción si hay un cambio(no se ha probado)
            #print(seleccionLinea())

        def seleccionLinea(): #Al seleccionar un registro en el treeview, los valores se guardan en el objeto self.tview.selection(), self.tview.item retorna una lista de los valores
            linea = self.tView.selection()
            seleccion = list(self.tView.item(linea).values())
            print(seleccion)
            return seleccion # Retorna una lista de los valores del registro.
        
        def guardarInscripción(): 
            #Toma de datos de Combobox e Insert de fecha
            cmbx = getcmbx()
            cmbxCur = getcmbxCur()  
            fecha = getFecha()
            #Se añade el registro a Inscritos tomando la información de cmbx para idCurso y idAluno.
            guardar = cur.execute("INSERT INTO Inscritos (\"No.Inscripción\", Id_Alumno, Fecha_Inscripción, Código_Curso) VALUES (\"{}\",\"{}\",\"{}\",\"{}\") ".format(cmbxCur,cmbx,fecha,cmbxCur)) #Se realiza inserción de datos a la tabla inscritos
            conexion.commit() #Confirma la inscripción.
            actualizar("call") #Refresca el treeview.

        def eliminarLinea():
            if SeleccionVacia(): #Si en la seleccion no hay nada, se retorna pass.
                pass
            else:
                cmbx = getcmbx()
                #Se elimina el el registro donde coincida el id_alumno y el codigo curso(de la seleccion).
                eliminar = cur.execute("DELETE FROM Inscritos WHERE Id_Alumno = \"{}\" AND Código_Curso = \"{}\" ".format(cmbx, seleccionLinea()[0]))
                conexion.commit() #Confirma la eliminación.
                actualizar("call") #Refresca el treeview.

        self.cmbx_Id_Alumno.configure(values = valsCmbxAl) #Se colocan todas las opciones del combobox(los id_alumnos).
        self.cmbx_Id_Alumno.bind("<<ComboboxSelected>>", actualizar) #Al seleccionar una opción del combobox, lo que este dentro del combobox pasa como argumento a "Actualizar".
        self.cmbx_Id_Curso.configure(values = valsCmbxCur) #Se colocan todas las opciones del combobox(los id_cursos).
        self.cmbx_Id_Curso.bind("<<ComboboxSelected>>", actualizar) #Al seleccionar una opción del combobox, lo que este dentro del combobox pasa como argumento a "Actualizar".        
        self.btnEliminar.configure(command = eliminarLinea) #Al presionar el boton, se ejecuta el comando.
        self.btnGuardar.configure(command=guardarInscripción) # Al presionar boton, se guarda la inscripción en base de datos
   
    def run(self):
        self.mainwindow.mainloop()

    ''' A partir de este punto se deben incluir las funciones
     para el manejo de la base de datos '''

seleccion = []
conexion = sqlite3.connect(PATH + BD)
cur = conexion.cursor()
valsCmbxAl = cur.execute("SELECT Id_Alumno FROM Alumnos").fetchall() #Opciones del Combobox Alumno
valsCmbxCur = cur.execute("SELECT Código_Curso FROM Cursos").fetchall() #Opciones del Combobox Curso


if __name__ == "__main__":
    app = Inscripciones()
    app.run()