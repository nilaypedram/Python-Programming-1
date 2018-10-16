from easygui import *
import sys
while 1:
    msgbox("Hello, customer")
    msg ="Choose your website"
    title = "Online shopping"
    choices = ["Amazon", "Flipkart", "Myntra", "Snapdeal"]
    choice = choicebox(msg, title, choices)
    msgbox("You chose: " +str(choice),"Survey Result")
    if choice=="Amazon":
      msg1 ="Choose your preferance"
      title1 = "Amazon Shopping"
      choices1 = ["Electronics", "Sports"]
      choice1 = choicebox(msg1, title1, choices1)
      msgbox("You chose: " +str(choice1),"Survey Result")
      if choices1=="Electronics":
        msg2 ="what would you like to purchase?"
        title2 ="Electronics Shopping"
        choices2 = ["TV", "Cameras"]
        choice2 = choicebox(msg2, title2, choices2)
        msgbox("You chose: " +str(choice2),"Survey Result")
        if choices2=="TV":
          msg3 ="What company would you prefer?"
          title3 = "TV Shopping"
          choices3 = ["Sony", "Panasonic"]
          choice3 = choicebox(msg3, title3, choices3)
          msgbox("You chose: " +str(choice3),"Survey Result")
          if choices3=="Sony":
            msg4 ="Choose your vendor"
            title4 = "Sony shopping"
            choices4 = ["dj", "cj"]
            choice4 = choicebox(msg4, title4, choices4)
            msgbox("You chose: " +str(choice4),"Survey Result")
            msgx = "Do you want to continue?"
            titlex = "Please Confirm"
          else:
            msg4 ="Choose your vendor"
            title4 = "Panasonic shopping"
            choices4 = ["mj", "kj"]
            choice4 = choicebox(msg4, title4, choices4)
            msgbox("You chose: " +str(choice4),"Survey Result")

       msgbox("You chose: " + str(choice), "Survey Result")


       msg = "Do you want to continue?"
       title = "Please Confirm"
       if ccbox(msg, title):
        pass
       else:
        sys.exit(0)


