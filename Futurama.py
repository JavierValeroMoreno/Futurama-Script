# -*- coding: utf-8 -*-

from PIL import Image

dic_Alf_Fut = { 'a' : Image.open('./Alfabeto_Futurama/Trans_A.jpg'),
                'b' : Image.open('./Alfabeto_Futurama/Trans_B.jpg'),
                'c' : Image.open('./Alfabeto_Futurama/Trans_C.jpg'),
                'd' : Image.open('./Alfabeto_Futurama/Trans_D.jpg'),
                'e' : Image.open('./Alfabeto_Futurama/Trans_E.jpg'),
                'f' : Image.open('./Alfabeto_Futurama/Trans_F.jpg'),
                'g' : Image.open('./Alfabeto_Futurama/Trans_G.jpg'),
                'h' : Image.open('./Alfabeto_Futurama/Trans_H.jpg'),
                'i' : Image.open('./Alfabeto_Futurama/Trans_I.jpg'),
                'j' : Image.open('./Alfabeto_Futurama/Trans_J.jpg'),
                'k' : Image.open('./Alfabeto_Futurama/Trans_K.jpg'),
                'l' : Image.open('./Alfabeto_Futurama/Trans_L.jpg'),
                'm' : Image.open('./Alfabeto_Futurama/Trans_M.jpg'),
                'n' : Image.open('./Alfabeto_Futurama/Trans_N.jpg'),
                'o' : Image.open('./Alfabeto_Futurama/Trans_O.jpg'),
                'p' : Image.open('./Alfabeto_Futurama/Trans_P.jpg'),
                'q' : Image.open('./Alfabeto_Futurama/Trans_Q.jpg'),
                'r' : Image.open('./Alfabeto_Futurama/Trans_R.jpg'),
                's' : Image.open('./Alfabeto_Futurama/Trans_S.jpg'),
                't' : Image.open('./Alfabeto_Futurama/Trans_T.jpg'),
                'u' : Image.open('./Alfabeto_Futurama/Trans_U.jpg'),
                'v' : Image.open('./Alfabeto_Futurama/Trans_V.jpg'),
                'w' : Image.open('./Alfabeto_Futurama/Trans_W.jpg'),
                'x' : Image.open('./Alfabeto_Futurama/Trans_X.jpg'),
                'y' : Image.open('./Alfabeto_Futurama/Trans_Y.jpg'),
                'z' : Image.open('./Alfabeto_Futurama/Trans_Z.jpg'),
                '0' : Image.open('./Alfabeto_Futurama/Trans_0.jpg'),
                '1' : Image.open('./Alfabeto_Futurama/Trans_1.jpg'),
                '2' : Image.open('./Alfabeto_Futurama/Trans_2.jpg'),
                '3' : Image.open('./Alfabeto_Futurama/Trans_3.jpg'),
                '4' : Image.open('./Alfabeto_Futurama/Trans_4.jpg'),
                '5' : Image.open('./Alfabeto_Futurama/Trans_5.jpg'),
                '6' : Image.open('./Alfabeto_Futurama/Trans_6.jpg'),
                '7' : Image.open('./Alfabeto_Futurama/Trans_7.jpg'),
                '8' : Image.open('./Alfabeto_Futurama/Trans_8.jpg'),
                '9' : Image.open('./Alfabeto_Futurama/Trans_9.jpg'),
                ',' : Image.open('./Alfabeto_Futurama/Trans_COMA.jpg'),
                '.' : Image.open('./Alfabeto_Futurama/Trans_PUNTO.jpg'),
                ';' : Image.open('./Alfabeto_Futurama/Trans_PUNTO_COMA.jpg'),
                ':' : Image.open('./Alfabeto_Futurama/Trans_PUNTO_DOBLE.jpg'),
                '?' : Image.open('./Alfabeto_Futurama/Trans_INTERROGACION.jpg'),
                '!' : Image.open('./Alfabeto_Futurama/Trans_EXCLAMACION.jpg'),
                'o"' : Image.open('./Alfabeto_Futurama/Trans_OPEN_COMILLAS.jpg'),
                'c"' : Image.open('./Alfabeto_Futurama/Trans_CLOSE_COMILLAS.jpg'),
                "'" : Image.open('./Alfabeto_Futurama/Trans_COMILLA_SIMPLE.jpg'),
                '-' : Image.open('./Alfabeto_Futurama/Trans_GUION.jpg'),
                ' ' : Image.new('RGB', (50,50), "white")}

def Traductor( cadena ):
    if type( cadena ) != str:
        print("Necesario introducir una cadena")
        return
    it = 0
    aux = []
    while it*20 <= len(cadena):
        if (it+1)*20  > len(cadena):
            aux.append(cadena[it*20 :].lower())
        else:
            aux.append(cadena[it*20 : (it+1)*20])
        it = it+1
    
    imagen = Image.new('RGB',(len(aux[0])*50 + 50, len(aux)*50 +50), 'white')
    print("Tamaño de imagen: "+str(imagen.size))
    despX = 0
    despY = 25
    comillas_O = True
    for elm in aux:
        despX = 25
        for char in elm:
            if(char == '"'):
                if(comillas_O == True):
                    imagen_aux = dic_Alf_Fut['o"']
                else:
                    imagen_aux = dic_Alf_Fut['c"']
                comillas_O = not comillas_O
            else:
                imagen_aux = dic_Alf_Fut[char]

            imagen.paste(imagen_aux, (despX,despY))
            despX = despX + 50
        despY = despY +  50
    
    imagen.show()
    #imagen.save("Test1.jpg")
    imagen.save(cadena+".jpg")
    imagen.close()



#print(Traductor('"inutiles desgraciados  asdad "'))
#cadena_a_traducir = input("Introduce cadena a traducir: ")
#Traductor(cadena_a_traducir)
    
