# !/usr/bin/python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.ttk as ttk
import sqlite3
import tkinter.messagebox as msgb
from pathlib import Path

PATH = str((Path(__file__).resolve()).parent)
ICON=r"/imagen/ed.ico"
BD= r"/BD/Inscripciones.db"
class Inscripciones:
    def centrar(self):
        self.win.update_idletasks() #actualiza las dimensiones de la ventana
        ancho = self.win.winfo_width() 
        alto = self.win.winfo_height()
        x = (self.win.winfo_screenwidth() // 2) - (ancho // 2) #calcula la posicion de x
        y = (self.win.winfo_screenheight() // 2) - (alto // 2) #calcula la posicion de y
        self.win.geometry('{}x{}+{}+{}'.format(ancho, alto, x, y)) #ajusta la geometria de la ventana
    def __init__(self, master=None):
        # Ventana principal
        self.db_name = PATH + BD   
        self.win = tk.Tk(master)
        self.win.configure(background="#2B4D6F", height=600, width=800)
        self.win.geometry("800x600")
        self.win.iconbitmap(PATH +ICON)
        self.win.resizable(False, False)
        self.win.title("Inscripciones de Materias y Cursos")
        # Crea los frames
        self.centrar()
        self.frm_1 = tk.Frame(self.win, name="frm_1")
        self.frm_1.configure(background="#2B4D6F", height=600, width=800)
        self.lblNoInscripcion = ttk.Label(self.frm_1, name="lblnoinscripcion")
        self.lblNoInscripcion.configure(background="#2B4D6F",font="{Arial} 11 {bold}",
                                        justify="left",state="normal",
                                        takefocus=False,text='No.Inscripción',
                                        foreground="white")
        
        #Label No. Inscripción
        self.lblNoInscripcion.place(anchor="nw", x=670, y=20)
        #Entry No. Inscripción
        self.num_Inscripcion = ttk.Entry(self.frm_1, name="num_inscripcion")
        self.num_Inscripcion.configure(justify="right",state="readonly")
        self.num_Inscripcion.place(anchor="nw", width=100, x=672, y=50)
        #Funcion barras de fecha
        def fecha_barras(action, fecha, car): #agrega los slash a la fecha 
            if action == '0':
                if car == '/':
                    return False #no permite el ingreso de slash a mano propia
            if action == '1':
                if len(fecha) > 10:
                    return False #la fecha no pasa de 10 caracteres
                elif car.isalpha():
                    return False #no permite valores "str" al digitar los numeros
                elif car == '/':
                    return False
                elif len(fecha) == 3 or len(fecha) == 6:
                    if fecha.count('/') < 2: #agrega los slash
                        arreglo = self.fecha.get()
                        arreglo += '/'
                        self.fecha.delete(0,tk.END)
                        self.fecha.insert(0,arreglo)
                return True

        #Label Fecha
        self.lblFecha = ttk.Label(self.frm_1, name="lblfecha")
        self.lblFecha.configure(background="#2B4D6F", text='Fecha:',foreground="white")
        self.lblFecha.place(anchor="nw", x=630, y=85)
        #Entry Fecha
        self.fecha = ttk.Entry(self.frm_1, name="fecha", validate = "key", validatecommand=(self.win.register(fecha_barras),"%d","%P", "%S")) #valida la funcion anterior
        self.fecha.configure(justify="center",state= tk.DISABLED)
        self.fecha.place(anchor="nw", width=90, x=680, y=85)
        #self.fecha.insert(0,"DD/MM/AAAA")

        #Label Alumno
        self.lblIdAlumno = ttk.Label(self.frm_1, name="lblidalumno")
        self.lblIdAlumno.configure(background="#2B4D6F", text='Id Alumno:',foreground="white")
        self.lblIdAlumno.place(anchor="nw", x=30, y=85)
        #Combobox Alumno
        self.cmbx_Id_Alumno = ttk.Combobox(self.frm_1, name="cmbx_id_alumno")
        self.cmbx_Id_Alumno.place(anchor="nw", width=112, x=110, y=85)

        #Label Alumno
        self.lblNombres = ttk.Label(self.frm_1, name="lblnombres")
        self.lblNombres.configure(background="#2B4D6F",text='Nombre(s):',foreground="white")
        self.lblNombres.place(anchor="nw", x=30, y=140)
        #Entry Alumno
        self.nombres = ttk.Entry(self.frm_1, name="nombres")
        self.nombres.place(anchor="nw", width=200, x=110, y=140)

        #Label Apellidos
        self.lblApellidos = ttk.Label(self.frm_1, name="lblapellidos")
        self.lblApellidos.configure(background="#2B4D6F",text='Apellido(s):',foreground="white")
        self.lblApellidos.place(anchor="nw", x=400, y=140)
        #Entry Apellidos
        self.apellidos = ttk.Entry(self.frm_1, name="apellidos")
        self.apellidos.place(anchor="nw", width=200, x=485, y=140)

        #Label Id Curso
        self.lblIdCurso = ttk.Label(self.frm_1, name="lblidcurso")
        self.lblIdCurso.configure(background="#2B4D6F", text='Id Curso:',foreground="white")
        self.lblIdCurso.place(anchor="nw", x=30, y=180)
        #Entry Id Curso
        self.idCurso = ttk.Entry(self.frm_1, name="idcurso")
        self.idCurso.configure(justify="center")
        self.idCurso.place(anchor="nw", width=200, x=110, y=180)
        #Combobox Id Curso
        self.cmbx_Id_Curso = ttk.Combobox(self.frm_1, name="cmbx_id_curso")
        self.cmbx_Id_Curso.place(anchor="nw", width=200, x=110, y=180)
        self.cmbx_Id_Curso.configure(state= tk.DISABLED)

        #Label Curso
        self.lblCurso = ttk.Label(self.frm_1, name="lblcurso")
        self.lblCurso.configure(background="#2B4D6F", text='Curso:',foreground="white")
        self.lblCurso.place(anchor="nw", x=400, y=180)
        #Entry Curso
        self.curso = ttk.Entry(self.frm_1, name="curso")
        self.curso.configure(justify="center",state= tk.DISABLED, background="blue")
        self.curso.place(anchor="nw", width=200, x=485, y=180)


        ''' Botones  de la Aplicación'''
        estilo= ttk.Style()
        estilo.configure("TButton",foreground= "#2B4D6F", background="blue")
        estilo.map("TButton",foreground=[("pressed","green"), ("disabled", "white"),("active","red")])
        #Botón Guardar
        self.btnGuardar = ttk.Button(self.frm_1, name="btnguardar")
        self.btnGuardar.configure(text='Guardar',state= tk.DISABLED)
        self.btnGuardar.place(anchor="nw", x=200, y=220)
        #Botón Editar
        self.btnEditar = ttk.Button(self.frm_1, name="btneditar")
        self.btnEditar.configure(text='Editar',command=lambda: modo_editar())
        self.btnEditar.place(anchor="nw", x=300, y=220)
        #Botón Eliminar
        self.btnEliminar = ttk.Button(self.frm_1, name="btneliminar")
        self.btnEliminar.configure(text='Eliminar')
        self.btnEliminar.place(anchor="nw", x=400, y=220)
        #Botón Cancelar
        self.btnCancelar = ttk.Button(self.frm_1, name="btncancelar")
        self.btnCancelar.configure(text='Cancelar',state= tk.DISABLED)
        self.btnCancelar.place(anchor="nw", x=500, y=220)
        #Separador
        separator1 = ttk.Separator(self.frm_1)
        separator1.configure(orient="horizontal")
        separator1.place(anchor="nw", width=796, x=2, y=260)
        #Boton Info
        self.btnInfo = ttk.Button(self.frm_1, name="btnInfo")
        self.btnInfo.configure(text='Info')
        self.btnInfo.place(anchor="nw", x=230, y=82)

        ''' Treeview de la Aplicación'''
        #Treeview
        self.tView = ttk.Treeview(self.frm_1, style="estilo.Treeview") 
        #Columnas del Treeview
        self.tView["columns"]=("descripcion","horas","creditos","aula")
        self.tView.column ("#0", anchor="w", stretch=True,width=10)
        self.tView.column ("descripcion", anchor="w", stretch=True,width=200)
        self.tView.column ("horas", anchor="w", stretch=True,width=80)
        self.tView.column ("creditos", anchor="w", stretch=True,width=80)
        self.tView.column ("aula", anchor="w", stretch=True,width=80)
        
        #Cabeceras
        self.tView.heading("#0", anchor="center", text="Codigo")
        self.tView.heading("descripcion", anchor="center",  text="Descripción")
        self.tView.heading("horas", anchor="center",  text="Horas semanales")
        self.tView.heading("creditos", anchor="center", text="Creditos")
        self.tView.heading("aula", anchor="center", text="Aula")

        #Scrollbars
        self.scroll_H = ttk.Scrollbar(self.tView, orient="vertical", command=self.tView.yview)
        self.tView.configure(yscroll=self.scroll_H.set)
        self.scroll_H.place( height=325, x=778, y=25)
        self.tView.place(anchor="nw", height=300, width=790, x=4, y=300)
        self.frm_1.pack(side="top")
        self.frm_1.pack_propagate(0)

        # Main widget
        self.mainwindow = self.win
        def fechaValida(fecha):
             componentes = fecha.strip().split("/") #Elimina espacios y crea una lista separando por slash.
             if len(fecha)==10 and len(componentes[0]) == 2 and len(componentes[1]) == 2 and len(componentes[2]) == 4: #Formato valido "XX / XX / XXXX"
              pass
             else:
                return False
             componentes = [int(componente) for componente in componentes ] #Convierte cada componente a int
             if 0 < componentes[0] <= 31 and  0 < componentes[1] <= 12 and 2009 < componentes[2] < 2100: #intervalos validos del dia y mes
                pass
             else:
                 return False
             mesesCon30Dias = [2,4,6,9,11] 
             es_Bisiesto = lambda año : True if año%4 == 0 and not (año%100 and not año%400) else False #Verifica si el año es bisiesto
             if componentes[0] == 29 and componentes[1] == 2: #verifica el caso 29/02/"Año bisiesto"
                if es_Bisiesto(componentes[-1]):
                 return True
                else:
                 return False
             else:
                 if componentes[1] in mesesCon30Dias and componentes[0] == 31:
                    return False
                 elif componentes[1] == 2 and componentes[0] > 28:
                    return False
                 else:
                     return True
                     
        def SeleccionVacia(): #Selección del treeview vacia. Una selección vacia es una lista vacia.
            if len(seleccionLinea()) == 0 : 
                return True
            else:
                return False
            
        def seleccionLinea():
             #Al seleccionar un registro en el treeview, los valores se guardan en el objeto self.tview.selection(), self.tview.item retorna la lista con los codigos de los registros seleccionados
            lineas = self.tView.selection() #
            seleccion = []
            for item in lineas:
                seleccion.append(list(self.tView.item(item).values()))
            return seleccion # Retorna una lista de los valores de los registros seleccionados
            
        def mensajeError(codigo): #Mensajes de error
            if codigo == 1: 
                msgb.showerror(message="Seleccione un alumno.")
            elif codigo == 2: 
                msgb.showerror(message="La fecha no es valida.")
            elif codigo == 3:
                msgb.showerror(message="Seleccióne un registro.")
            elif codigo == 4:
                msgb.showerror(message="Seleccióne un curso.")
            elif codigo == 5:
                msgb.showerror(message="El curso seleccionado ya fue añadido.")
            elif codigo == 6:
                msgb.showerror(message="El alumno no existe.")
            elif codigo == 7:
                msgb.showerror(message="El curso no existe.")
            else: 
                msgb.showerror(message="Selección vacia.")
        
        def ventanaConfirmacion(texto):
            confirmacion = msgb.askyesno(message=texto, title="Confirmación", )
            return confirmacion
            
        def mensajeConfirmacion(int):
            if int == 1:
                msgb.showinfo(message="Cambios guardados con exito.")
            if int ==2:
                msgb.showinfo(message="No se realizó ningun cambio")
        
        def mensajeInfo(): #Crea una ventana emergente para mostrar la información del alumno.
            cmbx = getcmbx()
            if cmbx == "vacio": #Si el combobox del alumno esta vacio, al presionar el boton no dara error
                return mensajeError(1)
            else:
                datosAlumno = cur.execute("SELECT * FROM Alumnos WHERE id_Alumno = \"{}\"".format(cmbx)).fetchone() #Query de los datos obtenidos de del alumno en una lista
                carrera = cur.execute("SELECT Alumnos.id_Carrera, Carreras.Descripción FROM Alumnos INNER JOIN Carreras ON Alumnos.id_Carrera = Carreras.Código_Carrera WHERE id_Alumno = \"{}\"".format(cmbx)).fetchone() #Obtiene el nombre de la carrera segun el codigo en los datos del alumno
                #print(datosAlumno)
                info = tk.Toplevel(self.win) #Crea una ventana con master al programa principal
                info.title("Información del estudiante")
                info.iconbitmap(PATH + ICON)
                info.configure(background="#2B4D6F")
                #Crea un label con la informacion alineada a la izquierda, en un pack()
                tk.Label(info, text= "\
                        Nombre:\t{} \n \
                        Apellidos:\t{} \n \
                        Id:\t \t {} \n \
                        Carrera: \t {} \n \
                        Fecha de ingreso:\t{} \n \
                        Dirección:\t{} \n \
                        Telefono Celular:\t{} \n \
                        Telefono Fijo:\t{} \n \
                        Ciudad:\t \t{} \n \
                        Departamento:\t{} \n".format(datosAlumno[2],datosAlumno[3],datosAlumno[0],carrera[1],datosAlumno[4],datosAlumno[5],datosAlumno[6],datosAlumno[7],datosAlumno[8],datosAlumno[9]),justify="left",anchor= "w" , font="{TkDefaultFont} 11",background="#2B4D6F",foreground="white").pack(ipadx=20, pady=10)
                tk.Button(info, text = "Ok", command = info.destroy).pack(pady=10) #Cierra la ventana

        
        def getFecha(): #Toma de la Fecha por medio del insert
            fecha = self.fecha.get()
            return fecha
            
            
        def getcmbx(): #Selecciona el id del estudiante destacado en el combobox
            index = self.cmbx_Id_Alumno.current()
            if index == -1:
                return "vacio"
            else:
                cmbx = valsCmbxAl[index][0]
                return cmbx
        
        def getcmbxCur(): #Selecciona el id del Curso destacado en el combobox
            index = self.cmbx_Id_Curso.current()
            if index == -1:
                return "vacio"
            cmbxCur = valsCmbxCur[index][0]
            return cmbxCur
        
        def getinscripcion(): #Da el numero de inscripcion 
            busqueda = cur.execute( "SELECT No_Inscripción FROM Inscritos WHERE Id_Alumno =  \"{}\"".format(getcmbx())).fetchall() #Busca el numero de inscripcion si existe
            Encontrar = cur.execute("SELECT No_Inscripción FROM Inscritos ").fetchall() # Da la lista completa de los numeros de inscripcion
            max_num = max(Encontrar) # encuentra el valor mas alto de los numeros de inscripcion 
            if busqueda:
                z= busqueda[0] # Da la lista del diccionaro
                n=z[0]# Da valor de la lista
            else: 
                n= max_num[0]
                n=n+1 
            return n
        
        def getCurso():
            curso = self.curso.get()
            if curso == "":
                return -1
            return curso
        
        def insertarId(arg): #Agrega el contexto para actualizar la interfaz
            idValor = self.cmbx_Id_Alumno.get().replace(" ","") #Si el datos es insertado, elimina los espacios al inicio y al final
            idValor = idValor.upper() #Segun el formato de los codigos de los alumnos, los convierte en mayuscualas
            capValor = tk.StringVar(master, value=idValor.upper()) #Crea un StringVar para cambiar el texto del combobox
            self.cmbx_Id_Alumno.configure(textvariable = capValor) #Se remplaza el texto del combobox
            for id in valsCmbxAl: #Busca dentro de los valores del comobobox si el valor insertado esta dentro, y si lo esta retorna la acción para cambiar el aceptar el id insertado
                if idValor in id:
                    return actualizar("idAlumno:{}".format(idValor))
            return mensajeError(6)

        def insertarIdCurso(arg): #Inserta el curso por escritura
            valor = self.cmbx_Id_Curso.get() #Obtiene el curso escrito en el combobox
            for id in valsCmbxCur: #Si el curso estra dentro de los valores del combobox, se retorna la accion para actualizar con el id seleccionado
                if valor in id:
                    self.curso.configure(textvariable= tk.StringVar(value=""))
                    return actualizar("idCurso:{}".format(valor))
            return mensajeError(7)
        
        def insertarCurso(arg): #Inserta el nombre del curso por escritura
            lista = cur.execute("SELECT Descrip_Curso,Código_Curso FROM Cursos").fetchall() #Crea una lista de todos los cursos en la base de datos
            valor = self.curso.get().strip() #Se obtiene el curso escrito en el label
            valor = valor.upper() #Lo convierte en mayusculas
            for curso in lista: #Si el curso esta en los valores, retorna la accion para actualizar
                if valor in curso:
                    self.cmbx_Id_Curso.configure(textvariable= tk.StringVar(value=""))
                    return actualizar("Curso:{}".format(valor))       
            return mensajeError(7)
        
        def cursoCombobox(arg): #Retorna la seleccion del combobobox de los cursos
            return actualizar("CursoCombobox:{}".format(self.cmbx_Id_Curso.get()))
        
        def botonCancelar(): #Se retorna la accion cancelar
            return actualizar("cancelar:activar")
        
            
        def actualizar(call): #El argumento no se utiliza, pero por ser llamado por un bind, se le coloca argumento.
            #cada llamado que entra en actualizar debe estar acompañado de ("accion:contexto")
            #Refresca el Treeview si hay hay elementos en el Treeview
            if len(self.tView.get_children(""))!= 0:
                tViewActual = self.tView.get_children()
                for item in tViewActual:
                    self.tView.delete(item)
        
            call = call.split(":")  #Retorna una lista con las acciones 
            print(call)

            if call[0] == "idAlumno": #Si el llamado tiene accion idAlumno, se actualiza el idAlumno 
                self.capValor = tk.StringVar(master, value= call[1])
                self.cmbx_Id_Alumno.configure(textvariable = self.capValor)
            else:
                pass
            cmbx = getcmbx()

            if cmbx == "vacio":
                pass
            else:
                #Nombre y Apellidos, Para cambiar el label hay que crear un StringVar, Los nombres y apellidos se cambian segun el idALumno del combobox 
                valsNombreApellidos = cur.execute("SELECT Nombres, Apellidos FROM Alumnos WHERE Id_Alumno =  \"{}\"".format(cmbx)).fetchone()
                self.nombresvar = tk.StringVar(value = valsNombreApellidos[0])
                self.nombres.configure(textvariable = self.nombresvar)
                self.apellidosvar = tk.StringVar(value = valsNombreApellidos[1])
                self.apellidos.configure(textvariable=self.apellidosvar)
       
            cmbxCur = getcmbxCur()
            if call[0] == "Curso": #Si el llamado tiene "Curso", se cambia el curso de la interfaz
                self.varCurso = tk.StringVar(value = call[1])
                self.curso.configure(textvariable = self.varCurso) #Cambia el curso
                valCmbxCur = cur.execute("SELECT Código_Curso FROM Cursos WHERE Descrip_Curso = \"{}\"".format(self.curso.get())).fetchone() #Obtiene el codigo del Curso
                self.valCmbxCur = tk.StringVar(value = valCmbxCur) 
                self.cmbx_Id_Curso.configure(textvariable = self.valCmbxCur) #Cambia el codigo del curso del combobox de acuerdo al nombre del curso
            
            if call[0] == "idCurso": #Si el llamado tiene "idCurso", entonces se cambia el nombre del curso.
                valCur = cur.execute("SELECT Descrip_Curso FROM Cursos WHERE Código_Curso = \"{}\"".format(self.cmbx_Id_Curso.get())).fetchone()
                self.valCur = tk.StringVar(value = valCur[0]) 
                self.curso.configure(textvariable = self.valCur)

            if call[0] == "CursoCombobox": #Se actualiza con la selección del combobox de cursos
                valIdCurso = cur.execute("SELECT Descrip_Curso FROM Cursos WHERE Código_Curso =  \"{}\"".format(call[1])).fetchone()
                self.cursosvar = tk.StringVar(value = valIdCurso[0])
                self.curso.configure(textvariable = self.cursosvar)

            busqueda = cur.execute( "SELECT No_Inscripción FROM Inscritos WHERE Id_Alumno =  \"{}\"".format(cmbx)).fetchone()
            self.inscripcionvar = tk.StringVar(value = busqueda[0])
            self.num_Inscripcion.configure(textvariable = self.inscripcionvar)
            if call[0] == "cancelar": #Si el llamado es "Cancelar", Se borran todos los campos
                    self.cmbx_Id_Alumno.delete(0,100)
                    self.cmbx_Id_Curso.delete(0,100)
                    self.curso.delete(0,100)
                    self.fecha.delete(0,100)
                    self.nombres.delete(0,100)
                    self.apellidos.delete(0,100)
            
            
            #TreeView
            # Hace un INNER JOIN de 3 tabla (Alumnos, Inscritos, Cursos) y selecciona los registros donde el id_alumno coincide con la opcion del combobox
            #Retorna una lista de atributos de cada registro y los inserta en el treeview parent = "" 
            if call[0] == "cancelar": #Si la accion es cancelar, se vacia el treeview
                valsTreeview = ()
                self.tView.insert(parent = "",index = tk.END, text = valsTreeview, values = valsTreeview)
            else: #Si el alumno cambia, o se modifico la base de datos, se actualiza el treeview
                valsTreeview = cur.execute("SELECT Inscritos.Código_Curso, Cursos.Descrip_Curso ,Info_Cursos.Num_Horas,Info_Cursos.Creditos,Info_Cursos.Aula FROM ((Inscritos INNER JOIN Cursos ON Inscritos.Código_Curso = Cursos.Código_Curso) INNER JOIN Info_Cursos ON Inscritos.Código_Curso = Info_Cursos.Código_Curso) WHERE Inscritos.Id_Alumno = \"{}\"".format(cmbx)).fetchall()
                
                for Curso in range(len(valsTreeview)):
                    self.tView.insert(parent = "",index = tk.END, text = valsTreeview[Curso][0], values = valsTreeview[Curso][1:]) #Modificar si hay mas columnas a agregar(solo admite 2)
                

        

        def modo_editar():
            self.btnGuardar.configure(state= tk.NORMAL)
            self.btnCancelar.configure(state= tk.NORMAL)
            self.btnEditar.configure(state= tk.DISABLED)
            self.cmbx_Id_Curso.configure(state= tk.NORMAL)
            self.curso.configure(state= tk.NORMAL)
            self.fecha.configure(state=tk.NORMAL)
        
    
        def modo_No_Editar():
            self.btnGuardar.configure(state= tk.DISABLED)
            self.btnCancelar.configure(state= tk.DISABLED)
            self.btnEliminar.configure(state= tk.NORMAL)
            self.btnEditar.configure(state= tk.NORMAL)
            self.cmbx_Id_Curso.configure(state= tk.DISABLED)
            self.curso.configure(state= tk.DISABLED)
            self.fecha.configure(state=tk.DISABLED)

        def guardarInscripción(): 
            if getcmbx() == "vacio": #Si en la seleccion no hay nada
                return mensajeError(1)
            else:

                #Toma de datos de Combobox e Insert de fecha
                cmbx = getcmbx()
                cmbxCur = getcmbxCur()  
                fecha = getFecha()
                num_inscripcion= getinscripcion()
                cursos = cur.execute("SELECT Código_Curso FROM Inscritos where id_Alumno = \"{}\"".format(cmbx)).fetchall()
                if cmbxCur == "vacio":
                    return mensajeError(4)
                if fechaValida(fecha) == False:
                    return mensajeError(2)
                for curso in cursos:
                    if cmbxCur in curso:
                        return mensajeError(5)
                
                #Se crean dos tuplas, una de los nombres y apellidos del alumno a inscribir. Y otra del curso con su respectiva aula a inscribir 
                alumno = cur.execute("SELECT Nombres, Apellidos FROM Alumnos WHERE id_Alumno = \"{}\"".format(cmbx)).fetchone()
                curso = cur.execute("SELECT Descrip_Curso, Aula FROM Cursos WHERE Código_Curso = \"{}\"".format(cmbxCur)).fetchone()
                #Se crea un String el cual almacena el mensaje a monstrar en la ventana de confirmación
                textCon = "¿Esta segur@ de guardar la siguiente inscripción (" + str(curso[0]) + ") con aula (" + str(curso[1]) + ") para el alumno "  + str(alumno[0]) + " " + str(alumno[1]) + "?"
                #Confirmación previa de realización de cambios, se entiende 1 como mensaje de confirmación Si, además ingresamos el String textCon como parametro
                if ventanaConfirmacion(textCon) == 1:
                    #Se añade el registro a Inscritos tomando la información de cmbx para idCurso y idAluno.
                    guardar = cur.execute("INSERT INTO Inscritos (No_Inscripción, Id_Alumno, Fecha_Inscripción, Código_Curso) VALUES (\"{}\",\"{}\",\"{}\",\"{}\") ".format(num_inscripcion,cmbx,fecha,cmbxCur)) #Se realiza inserción de datos a la tabla inscritos
                    conexion.commit() #Confirma la inscripción.
                    actualizar("call") #Refresca el treeview.
                    self.cmbx_Id_Curso.delete(0,tk.END)
                    self.curso.delete(0,tk.END)
                    self.fecha.delete(0,tk.END)
                    mensajeConfirmacion(1)
                else:
                    mensajeConfirmacion(2)
                modo_No_Editar()

        def eliminarLinea():
            cmbx = getcmbx()
            if cmbx == "vacio": #Si no hay alumno seleccionado(y por ende no hay nada en el treeview), se retorna error 1
                return mensajeError(1)
            elif SeleccionVacia(): #Si hay alumno pero no se ha seleccionado algun registro, se retorna error 3
                return mensajeError(3)
            else:
                #Se crea una tupla para guardar los nombres y apellidos del alumno
                alumno = cur.execute("SELECT Nombres, Apellidos FROM Alumnos WHERE id_Alumno = \"{}\"".format(cmbx)).fetchone()
                #Por medio del metodo seleccionLinea, tomamos la cantidad de registros seleccionados en el treview
                cantSeleccion = len(seleccionLinea())  
                #Se crea un String el cual almacena el mensaje a monstrar en la ventana de confirmación
                textCon = "¿Esta segur@ de eliminar las siguientes (" + str(cantSeleccion) + ") inscripciones de " + str(alumno[0]) + " " + str(alumno[1]) + "?"
                #Confirmación previa de realización de cambios, se entiende 1 como mensaje de confirmación Si, además ingresamos el String textCon como parametro
                if ventanaConfirmacion(textCon) == 1:
                    #Se elimina el el registro donde coincida el id_alumno y el codigo curso(de la seleccion).
                    for linea in seleccionLinea():
                        eliminar = cur.execute("DELETE FROM Inscritos WHERE Id_Alumno = \"{}\" AND Código_Curso = \"{}\" ".format(cmbx, linea[0]))
                    conexion.commit() #Confirma la eliminación.
                    actualizar("call") #Refresca el treeview.
                    mensajeConfirmacion(1)
                else:
                    mensajeConfirmacion(2)

        def botonCancelar(): #bloque de codigo que se ejecuta si acciona el boton
            self.cmbx_Id_Curso.delete(0,tk.END)
            self.curso.delete(0,tk.END)
            modo_No_Editar()
            return actualizar("cancelar:activar")

        def mouse_move(event): # lee las cordenadas del mouse 
            y= event.y
            if y < 26:
                return "break" 
        

        self.cmbx_Id_Alumno.configure(values = valsCmbxAl) #Se colocan todas las opciones del combobox(los id_alumnos).
        self.cmbx_Id_Alumno.bind("<<ComboboxSelected>>", insertarId) #Al seleccionar una opción del combobox, lo que este dentro del combobox pasa como argumento a "Actualizar".
        self.cmbx_Id_Curso.configure(values = valsCmbxCur) #Se colocan todas las opciones del combobox(los id_cursos).
        self.cmbx_Id_Curso.bind("<<ComboboxSelected>>", cursoCombobox) #Al seleccionar una opción del combobox, lo que este dentro del combobox pasa como argumento a "Actualizar".    
        self.btnEliminar.configure(command = eliminarLinea) #Al presionar el boton, se ejecuta el comando.
        self.btnGuardar.configure(command=guardarInscripción) # Al presionar boton, se guarda la inscripción en base de datos
        self.btnCancelar.configure(command = botonCancelar) # Al presionar boton, se acciona cancelar
        self.btnInfo.configure(command = mensajeInfo) # Al presionar boton, aparece la ventana de info
        self.cmbx_Id_Alumno.bind("<Return>", insertarId) # Al presionar enter en el comobobox
        self.cmbx_Id_Curso.bind("<Return>", insertarIdCurso) # Al presionar enter en el comobobox de cursos
        self.curso.bind("<Return>", insertarCurso) # Al presionar enter en cursos
        self.btnCancelar.configure(command = botonCancelar)
        self.tView.bind("<Button-1 >", mouse_move)# desactiva la tabla para que el usuario no pueda cambiar el tamaño

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


