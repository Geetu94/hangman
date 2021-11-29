from wird import choose_word
from image import IMAGES
print("welcome to my game")
name=input("hello custmor aapka name dale yha par ")
print("Welcome",name,"!")
print("try to guess  right word ")
print("__________")
def hangman():
  secret_word=choose_word()
  guessmade=""
  turns=len(secret_word)
  print("aapko jo word decide krna h uski length",len(secret_word),"hai")
  while len(secret_word)>=0:
    main_word=""
    for i in secret_word:
      if i in guessmade:
        main_word+=i
      
      else:
        main_word+="_"
    if main_word==secret_word:
      print(main_word)
      print("finally aap jeet gye!","😅😅😅😅🥰")
      break
    print("guess the right word",main_word)
    guess=input("=")
    if guess in secret_word:
      guessmade+=guess
    else:
      print("enter valid letter")
      if guess not in secret_word:
        turns-=1
        if turns==len(secret_word)-1:
          print(len(secret_word)-1,"turns hi bchi h koi bat nhi try kre 😊😊😊😊")
          print("______________________________________________________________________")
          print(IMAGES[0])
        if turns==len(secret_word)-2:
          print(len(secret_word)-2,"turns hi bchi h koi bat nhi aap try kro jeet jaoge 😕😕😕😕")
          print("______________________________________________________________________")
          print(IMAGES[1])
        if turns==len(secret_word)-3:
          print(len(secret_word)-3,"turns hi bchi h ache se khelo 🤗🤗🤗🤗")
          print("______________________________________________________________________")
          print(IMAGES[2])
        if turns==len(secret_word)-4:
          print(len(secret_word)-4,"turns hi bchi h 😟😟😟😟")
          print("______________________________________________________________________")
          print(IMAGES[3])
        if turns==len(secret_word)-5:
          print(len(secret_word)-5,"turns hi bchi h 🙁🙁🙁🙁")
          print(IMAGES[4])
          print("_____________________________________________________________________")
        if turns==len(secret_word)-6:
          print(len(secret_word)-6,"turns hi bchi h 😔😔😔😔😔")
          print("_____________________________________________________________________")
          print(IMAGES[5])
        if turns==len(secret_word)-7:
          print(len(secret_word)-7,"turns hi bchi h agr ab nhi kiya to aap har jaoge 😧😧😧😧😧😧😧😧😧")
          print("____________________________________________________________________")
          print(IMAGES[6])
        if turns==len(secret_word)-8:
          print("aap har gye😰😰😰😰😰😰😰😰")
          print("____________________________________________________________________")
          print(IMAGES[7])
          print(secret_word,"word tha but aap har gye h hme bhot afsos h 😕😕😕 koi bat nhi aap dobara try kre")
          break        
hangman()