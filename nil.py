#title-e-commerce website
#Nilay Pedram
#M-45



from easygui import *                                   #importing the library from easy gui
import sys                                              
while 1:                                                
    msgbox("Hello, customer")                           #using the tools boxes from gui library(msgbox,choice box,etc.)
    msg ="Choose your website"
    title = "Online shopping"
    choices = ["Amazon", "Flipkart", "Myntra"]
    choice = choicebox(msg, title, choices)
   # msgbox("You chose: " +str(choice),"Survey Result")
    if choice=="Amazon":
       msg1 ="Choose your preferance"
       title1 = "Amazon Shopping"
       choices1 = ["Electronics", "Sports"]
       choice1 = choicebox(msg1, title1, choices1)
      # msgbox("You chose: " +str(choice1),"Survey Result")
       if choice1=="Electronics":
          msg2 ="what would you like to purchase?"
          title2 ="Electronics Shopping"
          choices2 = ["TV", "Cameras"]
          choice2 = choicebox(msg2, title2, choices2)
         # msgbox("You chose: " +str(choice2),"Survey Result")
          if choice2=="TV":
             msg3 ="What company would you prefer?"
             title3 = "TV Shopping"
             choices3 = ["Sony", "Panasonic"]
             choice3 = choicebox(msg3, title3, choices3)
            # msgbox("You chose: " +str(choice3),"Survey Result")
             if choice3=="Sony":
                msg4 ="Choose your vendor"
                title4 = "Sony shopping"
                choices4 = ["dj=40000", "cj=45000"]
                choice4 = choicebox(msg4, title4, choices4)
               # msgbox("You chose: " +str(choice4),"Survey Result")
                msgx = "Do you want to continue?"
                titlex = "Please Confirm"
             else:
                msg4 ="Choose your vendor"
                title4 = "Panasonic shopping"
                choices4 = ["mj=30000", "kj=35000"]
                choice4 = choicebox(msg4, title4, choices4)
               # msgbox("You chose: " +str(choice4),"Survey Result")
                msgx1 = "Do you want to continue?"
                titlex1 = "Please Confirm"
          else:
             msg3 ="what company would you refer?"
             title3 = "camera shopping"
             choices3 = ["sony", "canon"]
             choice3 = choicebox(msg3, title3, choices3)
            # msgbox("You chose: " +str(choice3),"Survey Result")
             if choice3=="sony":
                msg5 ="Choose your vendor"
                title5 = "sony shopping"
                choices5 = ["rj=90000", "sj=100000"]
                choice5 = choicebox(msg5, title5, choices5)
               # msgbox("You chose: " +str(choice5),"Survey Result")
                msgx2 = "Do you want to continue?"
                titlex2 = "Please Confirm"
             else:
                msg5 ="Choose your vendor"
                title5 = "canon shopping"
                choices5 = ["nj=80000", "oj=85000"]
                choice5 = choicebox(msg5, title5, choices5)
               # msgbox("You chose: " +str(choice5),"Survey Result")
                msgx3 = "Do you want to continue?"
                titlex3 = "Please Confirm"
       else:
           msg2 ="what would you like to purchase?"
           title2 ="Sports Shopping"
           choices2 = ["football", "tt rackets"]
           choice2 = choicebox(msg2, title2, choices2)
          # msgbox("You chose: " +str(choice2),"Survey Result")
           if choice2=="football":
              msg3 ="What company would you prefer?"
              title3 = "football Shopping"
              choices3 = ["Nivea", "Nike"]
              choice3 = choicebox(msg3, title3, choices3)
             # msgbox("You chose: " +str(choice3),"Survey Result")
              if choice3=="Nivea":
                 msg4 ="Choose your vendor"
                 title4 = "football shopping"
                 choices4 = ["fb=4000", "kb=3700"]
                 choice4 = choicebox(msg4, title4, choices4)
                # msgbox("You chose: " +str(choice4),"Survey Result")
                 msgx = "Do you want to continue?"
                 titlex = "Please Confirm"
              else:
                 msg4 ="Choose your vendor"
                 title4 = "football shopping"
                 choices4 = ["jb=3000", "tb=3500"]
                 choice4 = choicebox(msg4, title4, choices4)
                # msgbox("You chose: " +str(choice4),"Survey Result")
                 msgx1 = "Do you want to continue?"
                 titlex1 = "Please Confirm"
           else:
               msg3 ="what company would you refer?"
               title3 = "tt rackets shopping"
               choices3 = ["silvers", "yonex"]
               choice3 = choicebox(msg3, title3, choices3)
              # msgbox("You chose: " +str(choice3),"Survey Result")
               if choice3=="silvers":
                  msg5 ="Choose your vendor"
                  title5 = "tt rackets shopping"
                  choices5 = ["ab=90000", "cb=100000"]
                  choice5 = choicebox(msg5, title5, choices5)
                 # msgbox("You chose: " +str(choice5),"Survey Result")
                  msgx2 = "Do you want to continue?"
                  titlex2 = "Please Confirm"
               else:
                  msg5 ="Choose your vendor"
                  title5 = "tt rackets shopping"
                  choices5 = ["db=80000", "eb=85000"]
                  choice5 = choicebox(msg5, title5, choices5)
                 # msgbox("You chose: " +str(choice5),"Survey Result")
                  msgx3 = "Do you want to continue?"
                  titlex3 = "Please Confirm"
    elif choice=="Flipkart":
       msg1 ="Choose your preferance"
       title1 = "Flipkart Shopping"
       choices1 = ["Electronics", "Sports"]
       choice1 = choicebox(msg1, title1, choices1)
      # msgbox("You chose: " +str(choice1),"Survey Result")
       if choice1=="Electronics":
          msg2 ="what would you like to purchase?"
          title2 ="Electronics Shopping"
          choices2 = ["TV", "Cameras"]
          choice2 = choicebox(msg2, title2, choices2)
         # msgbox("You chose: " +str(choice2),"Survey Result")
          if choice2=="TV":
             msg3 ="What company would you prefer?"
             title3 = "TV Shopping"
             choices3 = ["Sony", "Panasonic"]
             choice3 = choicebox(msg3, title3, choices3)
            # msgbox("You chose: " +str(choice3),"Survey Result")
             if choice3=="Sony":
                msg4 ="Choose your vendor"
                title4 = "Sony shopping"
                choices4 = ["dj=40000", "cj=45000"]
                choice4 = choicebox(msg4, title4, choices4)
               # msgbox("You chose: " +str(choice4),"Survey Result")
                msgx = "Do you want to continue?"
                titlex = "Please Confirm"
             else:
                msg4 ="Choose your vendor"
                title4 = "Panasonic shopping"
                choices4 = ["mj=30000", "kj=35000"]
                choice4 = choicebox(msg4, title4, choices4)
               # msgbox("You chose: " +str(choice4),"Survey Result")
                msgx1 = "Do you want to continue?"
                titlex1 = "Please Confirm"
          else:
             msg3 ="what company would you refer?"
             title3 = "camera shopping"
             choices3 = ["sony", "canon"]
             choice3 = choicebox(msg3, title3, choices3)
            # msgbox("You chose: " +str(choice3),"Survey Result")
             if choice3=="sony":
                msg5 ="Choose your vendor"
                title5 = "sony shopping"
                choices5 = ["rj=90000", "sj=100000"]
                choice5 = choicebox(msg5, title5, choices5)
               # msgbox("You chose: " +str(choice5),"Survey Result")
                msgx2 = "Do you want to continue?"
                titlex2 = "Please Confirm"
             else:
                msg5 ="Choose your vendor"
                title5 = "canon shopping"
                choices5 = ["nj=80000", "oj=85000"]
                choice5 = choicebox(msg5, title5, choices5)
               # msgbox("You chose: " +str(choice5),"Survey Result")
                msgx3 = "Do you want to continue?"
                titlex3 = "Please Confirm"
       else:
           msg2 ="what would you like to purchase?"
           title2 ="Sports Shopping"
           choices2 = ["football", "tt rackets"]
           choice2 = choicebox(msg2, title2, choices2)
          # msgbox("You chose: " +str(choice2),"Survey Result")
           if choice2=="football":
              msg3 ="What company would you prefer?"
              title3 = "football Shopping"
              choices3 = ["Nivea", "Nike"]
              choice3 = choicebox(msg3, title3, choices3)
             # msgbox("You chose: " +str(choice3),"Survey Result")
              if choice3=="Nivea":
                 msg4 ="Choose your vendor"
                 title4 = "football shopping"
                 choices4 = ["fb=4000", "kb=3700"]
                 choice4 = choicebox(msg4, title4, choices4)
                # msgbox("You chose: " +str(choice4),"Survey Result")
                 msgx = "Do you want to continue?"
                 titlex = "Please Confirm"
              else:
                 msg4 ="Choose your vendor"
                 title4 = "football shopping"
                 choices4 = ["jb=3000", "tb=3500"]
                 choice4 = choicebox(msg4, title4, choices4)
                # msgbox("You chose: " +str(choice4),"Survey Result")
                 msgx1 = "Do you want to continue?"
                 titlex1 = "Please Confirm"
           else:
               msg3 ="what company would you refer?"
               title3 = "tt rackets shopping"
               choices3 = ["silvers", "yonex"]
               choice3 = choicebox(msg3, title3, choices3)
              # msgbox("You chose: " +str(choice3),"Survey Result")
               if choice3=="silvers":
                  msg5 ="Choose your vendor"
                  title5 = "tt rackets shopping"
                  choices5 = ["ab=900", "cb=1000"]
                  choice5 = choicebox(msg5, title5, choices5)
                 # msgbox("You chose: " +str(choice5),"Survey Result")
                  msgx2 = "Do you want to continue?"
                  titlex2 = "Please Confirm"
               else:
                  msg5 ="Choose your vendor"
                  title5 = "tt rackets shopping"
                  choices5 = ["db=800", "eb=850"]
                  choice5 = choicebox(msg5, title5, choices5)
                 # msgbox("You chose: " +str(choice5),"Survey Result")
                  msgx3 = "Do you want to continue?"
                  titlex3 = "Please Confirm"
    else:
         msg1 ="Choose your preferance"
         title1 = "Myntra Shopping"
         choices1 = ["Electronics", "Sports"]
         choice1 = choicebox(msg1, title1, choices1)
        # msgbox("You chose: " +str(choice1),"Survey Result")
         if choice1=="Electronics":
            msg2 ="what would you like to purchase?"
            title2 ="Electronics Shopping"
            choices2 = ["TV", "Cameras"]
            choice2 = choicebox(msg2, title2, choices2)
           # msgbox("You chose: " +str(choice2),"Survey Result")
            if choice2=="TV":
               msg3 ="What company would you prefer?"
               title3 = "TV Shopping"
               choices3 = ["Sony", "Panasonic"]
               choice3 = choicebox(msg3, title3, choices3)
              # msgbox("You chose: " +str(choice3),"Survey Result")
               if choice3=="Sony":
                  msg4 ="Choose your vendor"
                  title4 = "Sony shopping"
                  choices4 = ["dj=40000", "cj=45000"]
                  choice4 = choicebox(msg4, title4, choices4)
                 # msgbox("You chose: " +str(choice4),"Survey Result")
                  msgx = "Do you want to continue?"
                  titlex = "Please Confirm"
               else:
                  msg4 ="Choose your vendor"
                  title4 = "Panasonic shopping"
                  choices4 = ["mj=30000", "kj=35000"]
                  choice4 = choicebox(msg4, title4, choices4)
                 # msgbox("You chose: " +str(choice4),"Survey Result")
                  msgx1 = "Do you want to continue?"
                  titlex1 = "Please Confirm"
            else:
               msg3 ="what company would you refer?"
               title3 = "camera shopping"
               choices3 = ["sony", "canon"]
               choice3 = choicebox(msg3, title3, choices3)
              # msgbox("You chose: " +str(choice3),"Survey Result")
               if choice3=="sony":
                  msg5 ="Choose your vendor"
                  title5 = "sony shopping"
                  choices5 = ["rj=90000", "sj=100000"]
                  choice5 = choicebox(msg5, title5, choices5)
                 # msgbox("You chose: " +str(choice5),"Survey Result")
                  msgx2 = "Do you want to continue?"
                  titlex2 = "Please Confirm"
               else:
                  msg5 ="Choose your vendor"
                  title5 = "canon shopping"
                  choices5 = ["nj=80000", "oj=85000"]
                  choice5 = choicebox(msg5, title5, choices5)
                 # msgbox("You chose: " +str(choice5),"Survey Result")
         else:
             msg2 ="what would you like to purchase?"
             title2 ="Sports Shopping"
             choices2 = ["football", "tt rackets"]
             choice2 = choicebox(msg2, title2, choices2)
            # msgbox("You chose: " +str(choice2),"Survey Result")
             if choice2=="football":
                msg3 ="What company would you prefer?"
                title3 = "football Shopping"
                choices3 = ["Nivea", "Nike"]
                choice3 = choicebox(msg3, title3, choices3)
               # msgbox("You chose: " +str(choice3),"Survey Result")
                if choice3=="Nivea":
                   msg4 ="Choose your vendor"
                   title4 = "football shopping"
                   choices4 = ["fb=4000", "kb=3700"]
                   choice4 = choicebox(msg4, title4, choices4)
                  # msgbox("You chose: " +str(choice4),"Survey Result")
                   msgx = "Do you want to continue?"
                   titlex = "Please Confirm"
                else:
                   msg4 ="Choose your vendor"
                   title4 = "football shopping"
                   choices4 = ["jb=3000", "tb=3500"]
                   choice4 = choicebox(msg4, title4, choices4)
                  # msgbox("You chose: " +str(choice4),"Survey Result")
                   msgx1 = "Do you want to continue?"
                   titlex1 = "Please Confirm"
             else:
                msg3 ="what company would you refer?"
                title3 = "tt rackets shopping"
                choices3 = ["silvers", "yonex"]
                choice3 = choicebox(msg3, title3, choices3)
               # msgbox("You chose: " +str(choice3),"Survey Result")
                if choice3=="silvers":
                   msg5 ="Choose your vendor"
                   title5 = "tt rackets shopping"
                   choices5 = ["ab=900", "cb=1000"]
                   choice5 = choicebox(msg5, title5, choices5)
                  # msgbox("You chose: " +str(choice5),"Survey Result")
                   msgx2 = "Do you want to continue?"
                   titlex2 = "Please Confirm"
                else:
                   msg5 ="Choose your vendor"
                   title5 = "tt rackets shopping"
                   choices5 = ["db=800", "eb=850"]
                   choice5 = choicebox(msg5, title5, choices5)
                  # msgbox("You chose: " +str(choice5),"Survey Result")
                   msgx3 = "Do you want to continue?"
                   titlex3 = "Please Confirm"

