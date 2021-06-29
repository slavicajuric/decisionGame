print("hello!")

name = input("whats your name? ")
print("hello,",name,"welcome to my new game!")

answer1= input("have you seen My Hero Academia? (yes/no)")
if answer1 == "yes":
  print("great,",name,"lets start")
  print(name,"today is the day you are born!")
  
  quirk = input("your quirk is Mind Reading.Do you like it?(yes/no)").lower()
  if quirk == "yes":
    print("im glad to hear that!")
    print("One day in kindergarten, some kid starts telling you how stupid and boring your quirk is.")
    
    answ3r= input(",what are you going to od? 1 tell them it doesnt matter or 2 go home and cry about it.(1/2)")
    if answ3r == "1":
      print("great job,now you are feeling great about yourself and your quirk ")

      print("after few years have passed, you got into UA and also made some friends!")
      baku_deku = input("who do you like spending your time with more, bakugou or izuku? (izuku/bakugou) ").lower()
      if baku_deku=="bakugou":
        print("great,me too! ")#znaci, ovdje nadodaji jos neka pitanja,inpute itd#

      else:
        print("aww, that wholsome!")

    else:
      print("aw damn,",name,",you now have lost all confidence in your quirk.")
  else:
    print(name,"that's not very polite... Well, you are Quirkless now! Ta-daa!")
    print("One day in kindergarten, some kid starts telling you how stupid and boring you are because you are quirkless.")

    answer2= input("what are you going to do? 1 tell them it doesnt matter or 2 ran home and cry about it. (1/2) ").lower()
    if answer2 == "1":
      print("great job",name,"!After few years have passed you finally got into UA")


    else:
      print("oh well, now you hav lost all confidence you had...And because you never had guts to stand up for yourself, you have never got into UA, but you became a doctor;-;")

else:
  print("oh too bad, you should come back when you watch it.")
