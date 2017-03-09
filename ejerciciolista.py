opcion=''
amigos=[]
while(opcion != 'salir'):
	opcion= input('ingrese un nombre:'+' ')
	if(opcion in amigos ):
		print('el nombre ya existe')
	if(opcion not in amigos ):
		 if(opcion != 'salir'):
		 	amigos.append(opcion)
		 	
		 	print(amigos)
