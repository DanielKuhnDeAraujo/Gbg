dlub=0
blib=0
blibsv=[]
globsv=[]
glob=0
blub=0
b=True
op=5
r=16
gleb=0
recursos=[100,100, 0]#comida, água,cristais
while b :
  for i in range(len(globsv)) :
    globsv[i-1]+=1
    if globsv[i-1]>30 :
      globsv[i-1]=1000
      glob-=1
  if 1000 in globsv :
    globsv.remove(1000)
  for i in range(len(blibsv)) :
    blibsv[i-1]+=1
    if blibsv[i-1]>45 :
      blibsv[i-1]=1000
      blib-=1
  if 1000 in blibsv :
    blibsv.remove(1000)
  for i in range(r) :
    print("")
  if gleb >0 :
    print(f"Globs : {glob}.\tBlubs : {blub}.   ")
  if dlub >0 :
    print(f"Vida dos globs: {globsv}  \nVida dos blibs : {blibsv}")
  print(f"Comida: {recursos[0]}\nÁgua: {recursos[1]}\nCristais: {recursos[2]}")
  print("Aqui estão suas opções de bichos para comprar")
  print("Opção 1: Ganhar mais um glob. Cada Glob tira uma água sua e te dá um cristal. Eles têm um limite de tempo de vida.")
  if recursos[2]>=15 :
    print("Opção 2 : Gaste 15 cristais e compre um Blub. Ele gera uma água por turno")
    r-=1
  if recursos[2]>=30 :
    print("Opção 3 : Gaste 30 cristais e compre um Gleb. Ele fala quantos blubs e globs vc tem.")
    r-=1
  if recursos[2]>=30 :
    print("Opção 4 : Gaste 30 cristais e compre um Blib. Ele fala quantos blubs e globs vc tem.")
    r-=1
  if recursos[2]>=50 :
    print("Opção 3 : Gaste 50 cristais e compre um Dlub. Ele fala a vida de seus globs e blubs.")
    r-=1
  for i in range(r) :
    print("")
  a=int(input("Digite o número da opção que você quer:"))
  if a<=op :
    if a==1 :
      glob+=1
      globsv.append(0)
    if a==2 and recursos[2]>=15 :
      blub+=1
      recursos[2]-=15
    if a==3 and recursos[2]>=30 :
      gleb+=1
      recursos[2]-=30
    if a==4 and recursos[2]>=30 :
      blib+=1
      recursos[2]-=30
      blibsv.append(0)
    if a==5 and recursos[2]>=50 :
      dlub+=1
      recursos[2]-=50
  else :
    print("Número fora do tamanho de opções")
  #glob i
  recursos[1]-=1*glob
  recursos[2]+=1*glob
  #glob f
  #blub i
  recursos[1]+=1*blub
  #blub f
  for i in recursos :
    if i < 0 :
      b=False
  r=16
  if gleb>0 :
    r-=1
  if dlub>0 :
    r-=2
  #blib i
  recursos[0]+=1*blib
  recursos[1]-=1*blib
  recursos[2]-=1*blib
  #blib f
print("Você perdeu")
