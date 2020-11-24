import random
import os


 


def cls():
    os.system('cls' if os.name=='nt' else 'clear')




def crea_tablero(fil,col,val):                                 #funcion que crea el tablero 
  tablero=[]
  for i in range(fil):
    tablero.append([])
    for j in range(col):
      tablero[i].append(val)
  return tablero

def muestra_tablero(tablero):                                 #funcion que muestra el tablero
  for fila in tablero:
    for elem in fila:
      print(elem, end="")
    print()


def coloca_minas(tablero,minas,fil,col):                     #funcion para colocar las minas en el tablero
  minas_ocultas=[]                                           #en esta lista se guardarán las coordenadas de las minas 
  numero=0
  while numero<minas:                                        #condicion para que se coloquen todas las minas deseadas (por si hay repeticiones)
    y=random.randint(0,fil-1)                                #x e y : coordenadas de las minas
    x=random.randint(0,col-1)
    if tablero[y][x] != 9:
      tablero[y][x]=9                                        #el 9 va a representar a a las minas
      numero += 1                                   
      minas_ocultas.append((y,x))           
  return tablero, minas_ocultas

def coloca_pistas(tablero, fil, col):
  for y in range(fil):
    for x in range(col):
      if tablero[y][x]==9:
        for i in [-1,0,1]:
          for j in [-1,0,1]:
            if 0 <= y+i <= fil-1 and 0 <= x+j <= col-1:
             try:
               if tablero[y+i][x+j] != 9:
                 tablero[y+i][x+j] += 1
             except:
               continue
  return tablero   

def relleno_ceros(oculto,visible,y,x,fil,col,val):
  ceros=[(y,x)]
  while len(ceros)>0:
      y,x=ceros.pop()
      for i in [-1,0,1]:
          for j in [-1,0,1]:
            if 0 <= y+i <= fil-1 and 0 <= x+j <= col-1:
                if visible[y+i][x+j] == val and oculto[y+i][x+j]==0:
                    visible[y+i][x+j]=0
                    if ( y+i , x+j ) not in ceros:
                        ceros.append((y+i,x+j))
                else:
                    visible[y+i][x+j]=oculto[y+i][x+j]


            try:
              if tablero[y+i][x+j] != 9:
                tablero[y+i][x+j] += 1
            except:
              continue
  return visible        

def completo(tablero,fil,col,val):
    for y in range(fil):
        for x in range(col):
            if tablero[y][x]==val:
                return False
    return True            


def pres():
  cls()
  print("********************************************")
  print("*-------------BIENVENIDX-------------------*")
  print("*-----------------AL-----------------------*")
  print("*----------------GRAN----------------------*")
  print("*---------------......---------------------*")
  print("*-------------BUSCAMINAS-------------------*")
  print("*-----------------:O-----------------------*")
  print("*---------Paseate con 8/6/2/4---;)---------*")      
  print("*------------------------------------------*")
  print("*-----------Destapa pistas con m-----------*")
  print("*------------------------------------------*")
  print("*Pon tus banderitas con p y quitalas con o**")
  print()
  input("*---------'Enter' para empezar-------------*")
  print("********************************************")

def menu():
  print()
  opcion=input("8/2/4/6  -m-  p/o  ")
  return opcion
  
columnas=int(input("Numero de columnas: "))
filas=int(input("Numero de filas: "))
minas=int(input("Numero de minas: "))

visible=crea_tablero(filas,columnas,"-")

oculto=crea_tablero(filas,columnas,0)

oculto, minas_ocultas=coloca_minas(oculto, minas, filas, columnas)

oculto=coloca_pistas(oculto,filas,columnas)
pres()

y=random.randint(2, filas-3)                               #coordenadas ficha inicial
x=random.randint(2, columnas-3)

real=visible[y][x]                                         #valor casilla ficha inicial
visible[y][x]="x"                                          #la marcamos con un x


cls()                                                       #se borra la pantalla para mostrar el tablero
muestra_tablero(visible)

minas_marcadas= []

jugando=True

while jugando:
  
  
        
  mov = menu()
  if mov == "8":
    if y==0:
      y=0
    else:
      visible[y][x]=real
      y -= 1
      real=visible[y][x]
      visible[y][x]="x"

  elif mov=="2":
    if y==filas-1:
      y=filas-1
    else:
      visible[y][x]=real
      y+=1
      real=visible[y][x]
      visible[y][x]="x"
  elif mov=="4":
    if x==0:
      x=0
    else:
      visible[y][x]=real
      x-=1
      real=visible[y][x]
      visible[y][x]="x"
  elif mov=="6":
    if x==columnas-1:
      x=columnas-1
    else:
      visible[y][x]=real
      x+=1
      real=visible[y][x]
      visible[y][x]="x"
  elif mov=="p":
      if real=="-":
          visible[y][x]="P"
          real=visible[y][x]  
          if (y,x) not in minas_marcadas:
              minas_marcadas.append((y,x))  
  elif mov=="o":
      if  real=="P":
          visible[y][x]="-"
          real=visible[y][x]  
          if (y,x) in minas_marcadas:
              minas_marcadas.remove((y,x))
  elif mov=="m":
      if oculto[y][x]==9:
          visible[y][x]="B"
          jugando = False 
      elif oculto[y][x]!=0:
          visible[y][x]=oculto[y][x]
          real=visible[y][x]
      elif oculto[y][x]==0:
          visible[y][x]=0
          visible=relleno_ceros(oculto,visible,y,x,filas,columnas,"-")
          real=visible[y][x]                          


  cls()
  muestra_tablero(visible)


  ganador=False

  if completo(visible,filas,columnas,"-") and sorted(minas_ocultas)==sorted(minas_marcadas) and real!="-":
      ganador=True
      jugando=False

if ganador==False:
    muestra_tablero(oculto)
    print("**********************")
    print("******MUERTE**********")
    print("**********************")
else:
    print("**********************")
    print("***CRACK, GANASTE*****")
    print("**********************")




