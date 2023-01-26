from tkinter import *
from tkinter import messagebox
import sqlite3

#--------------------------------------------------------Extension de bases de Datos---------------------------

def conexionBBDD():

	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()

	try:

		miCursor.execute('''
			CREATE TABLE DATOS_USUARIOS(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_DE_USUARIO VARCHAR(50),
			PASSWORD VARCHAR(50),
			APELLIDO VARCHAR(50),
			DIRECCION VARCHAR(50),
			COMENTARIOS VARCHAR(200))
			''')

		messagebox.showinfo("BBDD", "BBDD creada con exito")
	except: 
		messagebox.showwarning("¡Atencion!", "Esta base ya existe")

def escape():
	valor=messagebox.askquestion("Cerrar", "Desea cerrar la aplicacion")

	if valor=="yes":
		Root.destroy()


def limpiador():
	miNombre.set("")
	miId.set("")
	miApellido.set("")
	miDireccion.set("")
	miPass.set("")
	textocoment.delete(1.0, END)

def crear():
	miConexion=sqlite3.connect("Usuarios")
	miCursor=miConexion.cursor()

	datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textocoment.get("1.0", END)
	"""miCursor.execute("INSERT INTO DATOS_USUARIOS VALUES(NULL, ' " + miNombre.get() +
		"','" +miPass.get() +
		"','" + miApellido.get() +
		"','" + miDireccion.get() +
		"','" + textocoment.get("1.0", END) + "')")"""

	miConexion.commit()
	messagebox.showinfo("BBDD", "Registro insertado exitosamente")

def leer():
	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()

	miCursor.execute("SELECT * FROM DATOS_USUARIOS WHERE ID=" +  miId.get())

	elUsuario=miCursor.fetchall()	

	for usuario in elUsuario:
		
		miId.set(usuario[0])
		miNombre.set(usuario[1])
		miPass.set(usuario[2])
		miApellido.set(usuario[3])
		miDireccion.set(usuario[4])
		textocoment.insert(1.0, usuario[5])

	miConexion.commit() 

def actualizar():
	miConexion=sqlite3.connect("Usuarios")

	miCursor=miConexion.cursor()

	datos=miNombre.get(),miPass.get(),miApellido.get(),miDireccion.get(),textocoment.get("1.0", END)


	"""miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_DE_USUARIO='"+ miNombre.get() +
		 "', PASSWORD='" + miPass.get() + 
		 "', APELLIDO='" + miApellido.get() +
		 "', DIRECCION='" + miDireccion.get() + 
		 "', COMENTARIOS='" + textocoment.get("1.0", END) +
		 "' WHERE ID=" + miId.get())"""

	miCursor.execute("UPDATE DATOS_USUARIOS SET NOMBRE_DE_USUARIO=?,PASSWORD=?, APELLIDO=?, DIRECCION=?, COMENTARIOS=?" +
		"WHERE ID=" + miId.get(),(datos))

	miConexion.commit()

	messagebox.showinfo("BBDD", "Registro actualizado con exito")


def eliminar():
	miConexion=sqlite3.connect("usuarios")
	miCursor=miConexion.cursor()
	miCursor.execute("DELETE FROM DATOS_USUARIOS WHERE ID="+ miId.get())
	miConexion.commit()
	messagebox.showinfo("BBDD", "se ha eliminado exitosamente el registro")







Root= Tk()

#---------------------------------------------------------Barras de Menus--------------------------------------------------------
BarraMenu= Menu(Root)
Root.config(menu=BarraMenu, width=500, height=500)

BBDDmenu= Menu(BarraMenu, tearoff=False)
BBDDmenu.add_command(label="conectar", command=conexionBBDD)
BBDDmenu.add_command(label="Salir", command=escape)


Borrarmenu= Menu(BarraMenu, tearoff=False)
Borrarmenu.add_command(label="Borrar campos", command=limpiador)


CRUDmenu= Menu(BarraMenu, tearoff=False)
CRUDmenu.add_command(label="Crear", command=crear)
CRUDmenu.add_command(label="Leer", command=leer)
CRUDmenu.add_command(label="Actualizar", command= actualizar)
CRUDmenu.add_command(label="Eliminar", command=eliminar)


Ayudamenu= Menu(BarraMenu, tearoff=False)
Ayudamenu.add_command(label="Licencia")
Ayudamenu.add_command(label="Acerca de")





BarraMenu.add_cascade(label="BBDD", menu=BBDDmenu)

BarraMenu.add_cascade(label="Borrar", menu=Borrarmenu)


BarraMenu.add_cascade(label="CRUD", menu=CRUDmenu)


BarraMenu.add_cascade(label="Ayuda", menu=Ayudamenu)



miFrame= Frame(Root)
miFrame.pack()

miId=StringVar()
miNombre=StringVar()
miApellido=StringVar()
miPass=StringVar()
miDireccion=StringVar()

CuadroID= Entry(miFrame, textvariable=miId)
CuadroID.grid(row=0, column=1, padx=10, pady=10)

CuadroName= Entry(miFrame, textvariable=miNombre)
CuadroName.grid(row=1, column=1, padx=10, pady=10)
CuadroName.config(fg="red", justify="right")

CuadroApellido= Entry(miFrame, textvariable=miApellido)
CuadroApellido.grid(row=2, column=1, padx=10, pady=10)

CuadroContra= Entry(miFrame, textvariable=miPass)
CuadroContra.grid(row=3, column=1, padx=10, pady=10)
CuadroContra.config(show="?")

CuadroDirec= Entry(miFrame, textvariable=miDireccion)
CuadroDirec.grid(row=4, column=1, padx=10, pady=10)


textocoment= Text(miFrame, width=18, height=5)
textocoment.grid(row=5, column=1, padx=10, pady=10)

scrollVert= Scrollbar(miFrame, command=textocoment.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textocoment.config(yscrollcommand=scrollVert.set)


#---------------------------------------------------------Labels--------------------------------------------------------

IDLabel=Label(miFrame, text="ID:")
IDLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

NombreLabel=Label(miFrame, text="Nombre:")
NombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)


ApellidoLabel=Label(miFrame, text="Apellido:")
ApellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)


ContraseñaLabel=Label(miFrame, text="Contaseña:")
ContraseñaLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)


DireccionLabel=Label(miFrame, text="Direccion:")
DireccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)


ComentariosLabel=Label(miFrame, text="Comentarios:")
ComentariosLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

#---------------------------------------------------------Botones--------------------------------------------------------
Miframe2=Frame(Root)
Miframe2.pack()

BotonCreate= Button(Miframe2, text="Create", command= crear)
BotonCreate.grid(row=1, column=1, padx=10, pady=10)

BotonRead= Button(Miframe2, text="Read", command=leer)
BotonRead.grid(row=1, column=2, padx=10, pady=10)

BotonUpdate= Button(Miframe2, text="Update", command=actualizar)
BotonUpdate.grid(row=1, column=3, padx=10, pady=10)

BotonDelete= Button(Miframe2, text="Delete", command=eliminar)
BotonDelete.grid(row=1, column=4, padx=10, pady=10)


Root.mainloop()



















#teorias

#Label(Miframe, text="ID:", justify="right" ).pack()



#BotonCreate= Button(Miframe, text="Create", padx=10, pady=10).pack()
#BotonRead= Button(Miframe, text="Read").pack()
#BotonUpdate= Button(Miframe, text="Update").pack()
#BotonDelete= Button(Miframe, text="Delete").pack()