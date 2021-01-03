
#Asigna la emoción que mayor probabilidad tiene en la
#distribución de probabilidades de esa imagen
print("hello world")


def get_emo(emo_info):
	idx=emo_info.index(max(emo_info))
	return idx

#Leemos el fichero faces2info txt
#Este fichero contiene la lista de los nombres de las imágenes
#Los nombres de cada fichero siguen el siguiente formato:
#persona, edad (young, middle, older), gender (male, female), 
#emotion (anger, disgust, fear, happiness, neutrality, sadness), 
#la última letra es picture_set, que sólo es "a" o "b" para dividir entre train y set. 
f = open("faces2info.txt", "r")
labels = f.readlines()
f.close()


split_keys={'a':"train",'b':"test"}
emo_labels={
"n":"Neutrality",
"f":"Fear",
"d": "Disgust",
"h":"Happiness",
"s":"Sadness",
"a" : "Anger"}


print("hello world")
for c in labels:
	d=c.strip()
	# print(d)
	splt_code=d[-5]
	train_valid=split_keys[splt_code]
	# print("trainval? ,",train_valid)
	
	emo=d[-7]
	emotion=emo_labels[emo]
	# print("emotion= ",emotion)
	if emotion=="Happiness":
		# 	#Generamos los comandos para guardar la imagen en la carpeta correspondiente:
		txt = "cp ./FACES2/{}  ./FACES_ordenat/{}/{}".format(d,train_valid,emotion)
		print(txt)



	# print(splt_code)
	
	# if splt_code=='a':
	# 	train_valid="train"
	
	# if splt_code=='b':
	# 	train_valid="test"




# for p,l in zip(partition,labels):
	
# 	tr_or_val = p.split()
# 	#nombre de la imagen:
# 	file=tr_or_val.pop(0)
# 	print("file ",file)

# 	#Asignamos la etiqueta correspondiente train or test
# 	train_valid=split_keys[int(tr_or_val[0])]

# 	emo = l.split()
# 	emo.pop(0)

# 	#Asignamos la etiqueta de emoción correspondiente:
# 	emotion=emo_labels[get_emo(emo)]

# 	#Generamos los comandos para guardar la imagen en la carpeta correspondiente:
# 	txt = "cp ./aligned/{}_aligned.jpg  ./dataset_ordenat/{}/{}".format(file[:-4],train_valid,emotion)
# 	print(txt)

#Instrucciones:
#1)Ejecutamos este archivo para generar un fichero .bat
#Ejecutar como python ./tidyData.py > ordenardataset.bat
#2)Ejecutar el fichero ordenardataset.bat