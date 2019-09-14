from graphics import *
import winsound
import random
import time
import sys


#Title Page Variables function call.#
def Title_Page():

    EX = 350
    WY = 250
    ZX = 350
    ZY = 320
    Q1 = 350
    Q2 = 380
    Text_Size = 14
    CLR = "yellow"
    Font = "times roman"
    
    return  EX , WY , ZX , ZY , Q1 , Q2 ,  CLR , Text_Size , Font


#Window Variables function call.#
def Window_Variables():

   
    TI_Name = "Text Invasion"
    TI_Height = 700
    TI_Width = 600

    return TI_Height , TI_Width , TI_Name


#Accumulation for score function call.#
def Accumulation():

    COUNT = 0
    ACC = 0
    Word_Collection = 0

    return COUNT , ACC, Word_Collection


# 5 lists for text boxes function call.#
def Lists_For_Game():

    lst = ["Tommy","Pappas","Alex","Helene","Lokuae","Frank","Lola","Froka","Doris","Friend","Parrot","Garlic","Train"]
    lst_2 = ["Greg","Eric","Matthew","Ron","Kayla","Window","Spencer","Carly","Emily","Smoke","Saibot","Yearly","Tear"]
    lst_3 = ["Run","Walk","Speed","Crawl","Annoy","Meat","Space","Python","Java","Dollar","Carrot","Cyclops","Cat"]
    lst_4 = ["Phone","Bus","Looney","Tunes","Ever","Script","Genius","Aliens","Wear","Poland","Italy","Venus","Dog"]
    lst_5 = ["Head","Nose","Shoulders","Knees","Toes","Doctor","Surgeon","Nurse","Level","Polar","Eating","Walking"]

    return lst , lst_2 , lst_3 , lst_4 , lst_5


#Random selected starting point for text boxes to fall down, function call.#
def Random_Movement():

    random_txt1 = random.randint(40,90)
    random_txt2 = random.randint(130,180)
    random_txt3 = random.randint(220,270)
    random_txt4 = random.randint(310,360)
    random_txt5 = random.randint(410,460)
    random_txt6 = random.randint(510,560)

    return random_txt1 , random_txt2 , random_txt3 , random_txt4 , random_txt5, random_txt6


# Variables for styling the text boxes function call.#
def Styling_Texts():

    Style_Size = 16
    Style_I = 'italic'
    Style_Font = 'courier'
    Style_Color = 'lightgreen'

    return Style_Size , Style_I , Style_Font , Style_Color
    

#Movement 1, initial speed of the text-boxes falling.#
def Movement_Variables():

       M_1 = 0
       M_2 = 1
       M_3 = 0
       M_4 = 1
       M_5 = 0
       M_6 = 1
       M_7 = 0
       M_8 = 1
       M_9 = 0
       M_10 = 1
       M_11 = 0
       M_12 = 1
       
       return M_1 , M_2 , M_3 , M_4 , M_5 , M_6 , M_7 , M_8 , M_9 , M_10 , M_11 , M_12


#Movement 2, speeding up the text-boxes falling.#
def Movement_2():

        V_1 = 0
        V_2 = 2
        V_3 = 0
        V_4 = 2
        V_5 = 0
        V_6 = 2
        V_7 = 0
        V_8 = 2
        V_9 = 0
        V_10 = 2
        V_11 = 0
        V_12 = 2

        return V_1 , V_2 , V_3 , V_4 , V_5 , V_6 , V_7 , V_8 , V_9 , V_10 , V_11 , V_12


#Movement 3, speeding up the text-boxes falling even more.
def Movement_3():

        E_1 = 0
        E_2 = 3
        E_3 = 0
        E_4 = 3
        E_5 = 0
        E_6 = 3
        E_7 = 0
        E_8 = 3
        E_9 = 0
        E_10 = 3
        E_11 = 0
        E_12 = 3

        return E_1 , E_2 , E_3 , E_4 , E_5 , E_6 , E_7 , E_8 , E_9 , E_10 , E_11 , E_12


#Movement 4, fastest speed that the text-boxes will fall.#
def Movement_4():

        R_1 = 0
        R_2 = 4
        R_3 = 0
        R_4 = 4
        R_5 = 0
        R_6 = 4
        R_7 = 0
        R_8 = 4
        R_9 = 0
        R_10 = 4
        R_11 = 0
        R_12 = 4

        return R_1 , R_2 , R_3 , R_4 , R_5 , R_6 , R_7 , R_8 , R_9 , R_10 , R_11 , R_12


class Text_Invasion():

    #Main Game with if, elif, breaks, loop, and score capturing.#
    def Main_Game():


        #Calling back window variables from function.#
        TI_Width , TI_Height , TI_Name = Window_Variables()
        ##

        #The window(game).#
        Window = GraphWin( TI_Name , TI_Width, TI_Height )
        Window.setBackground("white")
        ##

        #Music for the game!
        winsound.PlaySound('TI.wav', winsound.SND_LOOP + winsound.SND_ASYNC)
        ##
        
        #Accumulator and Counter for the Score Collection of Words successfully typed.#
        COUNT , ACC, Word_Collection = Accumulation()
        ##
        
        #Background Image for the window.#
        background = Image(Point(250,88),"nightsky.png")
        background.draw(Window)
        ##

        #Title Page Text "Text Invasion".#
        EX , WY , ZX , ZY , Q1 , Q2 , CLR , Text_Size , Font = Title_Page()
        Title_Text = Image (Point( EX , WY ) , "Title.png")
        Title_Text.draw(Window)


        #Title page text, secondary, tertiary.#
        Secondary_Text = Text (Point( ZX , ZY ) , "Welcome, To start playing, enter your name into the shell and the game will begin.")
        Secondary_Text.setFill(CLR)
        Secondary_Text.setSize(Text_Size)
        Secondary_Text.setFace(Font)
        Secondary_Text.draw(Window)

        Third_Text = Text (Point( Q1 , Q2 ) , "Rules: Finish the words from left to right then type in 'End!' to finish the line!")
        Third_Text.setFill(CLR)
        Third_Text.setSize(Text_Size)
        Third_Text.setFace(Font)
        Third_Text.draw(Window)
        ##

        #Ending Display.#
        Final_Text = Text(Point( TI_Width / 2 , TI_Height / 2 ), "You didn't tag all the words. Better luck next time!")
        Final_Text .setFill(CLR)
        Final_Text.setSize(Text_Size)
        Final_Text.setFace(Font)
        ##
    
        #Making the variables to record the score through a txt.file.#
        Input_Name = input("What is your Name, Typist?\n")
        File_1 = open('Score.txt','a')
        Name_Future = Input_Name
        Score = COUNT
        ##

        #Undraws the Title page texts when user inputs his name & the game starts.#
        Title_Text.undraw()
        Secondary_Text.undraw()
        Third_Text.undraw()
        ##
        
        #Loop to start the process of the game.#
        for a in range(sys.maxsize):
        ##

            #Movement variables from returning function.#
            M_1 , M_2 , M_3 , M_4 , M_5 , M_6 , M_7 , M_8 , M_9 , M_10 , M_11 , M_12 = Movement_Variables()
            ##

            #Creating a set of lists to make a word bank for the text to flow downwards later.#
            #List Variables from returning function.#
            lst , lst_2 , lst_3 , lst_4 , lst_5 = Lists_For_Game()
            ##

            
            #Random coordinate axis's for the textbox to appear (without them overlapping each other).#
            random_txt1 , random_txt2 , random_txt3 , random_txt4 , random_txt5 , random_txt6 = Random_Movement()
            ##

            
            #Visual Representation of the lists in the graphics.py window.#

            Style_Size , Style_I , Style_Font , Style_Color = Styling_Texts()
            
            Text_1 = Text(Point(random_txt1,20),random.choice(lst))
            Text_1.setSize(Style_Size)
            Text_1.setFill(Style_Color)
            Text_1.setStyle(Style_I)
            Text_1.setFace(Style_Font)
            Text_1.draw(Window)
            #
            Text_2 = Text(Point(random_txt2,20),random.choice(lst_2))
            Text_2.setSize(Style_Size)
            Text_2.setFill(Style_Color)
            Text_2.setStyle(Style_I)
            Text_2.setFace(Style_Font)
            Text_2.draw(Window)
            #
            Text_3 = Text(Point(random_txt3,20),random.choice(lst_3))
            Text_3.setSize(Style_Size)
            Text_3.setFill(Style_Color)
            Text_3.setStyle(Style_I)
            Text_3.setFace(Style_Font)
            Text_3.draw(Window)
            #
            Text_4 = Text(Point(random_txt4,20),random.choice(lst_4))
            Text_4.setSize(Style_Size)
            Text_4.setFill(Style_Color)
            Text_4.setStyle(Style_I)
            Text_4.setFace(Style_Font)
            Text_4.draw(Window)
            #
            Text_5 = Text(Point(random_txt5,20),random.choice(lst_5))
            Text_5.setSize(Style_Size)
            Text_5.setFill(Style_Color)
            Text_5.setStyle(Style_I)
            Text_5.setFace(Style_Font)
            Text_5.draw(Window)
            #
            Text_6 = Text(Point(random_txt6,20),"End!")
            Text_6.setSize(16)
            Text_6.setFill("red")
            Text_6.setFace(Style_Font)
            Text_6.draw(Window)
            #
            Text_Name = Text(Point(250,500),Input_Name)
            Text_Name.setSize(Text_Size)
            Text_Name.setFace(Font)
            Text_Name.setFill(CLR)
            Text_Name.draw(Window)
            ##
            
            
            #Entry box that the user will be typing into.#
            ENTRY = Entry(Point(350,500),10)
            ENTRY.setFill('lightblue')
            ENTRY.draw(Window)
            ##

            #Textbox that shows the user outputting the words in real-time.#
            VAR_3 = Text(Point(350,400),"")
            VAR_3.setFace(Style_Font)
            VAR_3.setSize(16)
            VAR_3.setFill(Style_Color)
            VAR_3.draw(Window)
            ##
            
            #Visual textbox to see the score collection of words.#
            SCORE = Text(Point(425,400),COUNT+ACC)
            SCORE.setFace('courier')
            SCORE.setSize(Text_Size)
            SCORE.setFill(Style_Color)
            SCORE.draw(Window)
            ##

            Score_2 = Text(Point( 500,500), Word_Collection + ACC)
            Score_2.setFill(Style_Color)
            Score_2.draw(Window)

            #Getting the X & Y's of the textboxes so they can reach a certain point on the y-axis to break the loop.#
            P_1 = Text_1.getAnchor()
            P_1X = P_1.getX()
            P_2 = Text_1.getAnchor()
            P_2X = P_2.getY()

            P_3 = Text_2.getAnchor()
            P_3X = P_3.getX()
            P_4 = Text_2.getAnchor()
            P_4X = P_4.getY()
            
            P_5 = Text_3.getAnchor()
            P_5X = P_5.getX()
            P_6 = Text_3.getAnchor()
            P_6X = P_6.getY()

            P_7 = Text_4.getAnchor()
            P_7X = P_7.getX()
            P_8 = Text_4.getAnchor()
            P_8X = P_8.getY()

            P_9 = Text_5.getAnchor()
            P_9X = P_9.getX()
            P_10 = Text_5.getAnchor()
            P_10X = P_10.getY()

            P_11 = Text_6.getAnchor()
            P_11X = P_11.getX()
            P_12 = Text_6.getAnchor()
            P_12X = P_12.getY()
            ##


            #while loop to match the strings from entry and the randomized list text.#
            while True:
                Text_1.move( M_1 , M_2 )
                Text_2.move( M_3 , M_4 )
                Text_3.move( M_5 , M_6 )
                Text_4.move( M_7 , M_8 )
                Text_5.move( M_9 , M_10 )
                Text_6.move( M_11, M_12 )
                time.sleep(0.04)
                VAR_3.setText(ENTRY.getText())
            ##
                
                    
                #Matching the text you input to the randomly selected string from list 1.#
                if ENTRY.getText() == random.choice(lst):
                    Word_Collection + 1
                    M_1 = 0
                    M_2 = 0
                    #
                    Text_1.setFill(CLR)
                    Text_1.setSize(Text_Size)
                    Text_1.undraw()
                    VAR_3.setFill(CLR)
                    VAR_3.setSize(20)
                    VAR_3.setFill(Style_Color)
                    VAR_3.setSize(16)
                    
                ##
                    

                   
                #Matching the text you input to the randomly selected string from list 2.#   
                elif ENTRY.getText() == random.choice(lst_2):                   
                    Word_Collection + 1
                    M_3 = 0
                    M_4 = 0
                    #
                    Text_2.setFill(CLR)
                    Text_2.setSize(Text_Size)
                    Text_2.undraw()
                    Text_2.move(0,0)
                    VAR_3.setFill(CLR)
                    VAR_3.setSize(20)
                    VAR_3.setFill(Style_Color)
                    VAR_3.setSize(16)
                    
                ##
                    

                    
                #Matching the text you input to the randomly selected string from list 3.#   
                elif ENTRY.getText() == random.choice(lst_3):
                    Word_Collection + 1
                    M_5 = 0
                    M_6 = 0
                    #
                    Text_3.setFill(CLR)
                    Text_3.setSize(Text_Size)
                    Text_3.undraw()
                    Text_3.move(0,0)
                    VAR_3.setFill(CLR)
                    VAR_3.setSize(Text_Size)
                    VAR_3.setFill(Style_Color)
                    VAR_3.setSize(16)
                    
                ##
                    
                    
                #Matching the text you input to the randomly selected string from list 4.#   
                elif ENTRY.getText() == random.choice(lst_4):
                    Word_Collection + 1
                    M_7 = 0
                    M_8 = 0
                    #
                    Text_4.setFill(CLR)
                    Text_4.setSize(Text_Size)
                    Text_4.undraw()
                    Text_4.move(0,0)
                    VAR_3.setFill(CLR)
                    VAR_3.setSize(Text_Size)
                    VAR_3.setFill(Style_Color)
                    VAR_3.setSize(16)
                    
                ##

               
                  
                #Matching the text you input to the randomly selected string from list 5.#
                elif ENTRY.getText() == random.choice(lst_5):
                    Word_Collection + 1
                    M_9 = 0
                    M_10 = 0
                    #
                    Text_5.setFill(CLR)
                    Text_5.setSize(Text_Size)
                    Text_5.undraw()
                    Text_5.move(0,0)
                    VAR_3.setFill(CLR)
                    VAR_3.setSize(Text_Size)
                    VAR_3.setFill(Style_Color)
                    VAR_3.setSize(16)
                    
                ##
                    

                #Matching the text you input to the string 'End!' will break the loop to go onto the next set of lists.#
                elif ENTRY.getText() == "End!":
                    M_11 = 0
                    M_12 = 0
                    #
                    COUNT = COUNT + 5
                    Text_1.undraw()
                    Text_2.undraw()
                    Text_3.undraw()
                    Text_4.undraw()
                    Text_5.undraw()
                    Text_6.undraw()
                    Text_Name.undraw()
                    SCORE.undraw()
                    VAR_3.undraw()
                    break
                    ##

                elif Word_Collection == 5:
                    Word_Collection = 0
                    COUNT += 5
                    Text_1.undraw()
                    Text_2.undraw()
                    Text_3.undraw()
                    Text_4.undraw()
                    Text_5.undraw()
                    Text_6.undraw()
                    Text_Name.undraw()
                    SCORE.undraw()
                    VAR_3.undraw()
                    break
                    
                    
                        
              
                #Increaing the speed that the text falls when counter is getting to a certain integer.#
                if COUNT > 50:
                    #
                    V_1 , V_2 , V_3 , V_4 , V_5 , V_6 , V_7 , V_8 , V_9 , V_10 , V_11 , V_12 = Movement_2()
                    #
                    time.sleep(0.02)
                    Text_1.move ( V_1 , V_2 )
                    Text_2.move ( V_3 , V_4 )
                    Text_3.move ( V_5 , V_6 )
                    Text_4.move ( V_7 , V_8 )
                    Text_5.move ( V_9 , V_10 )
                    Text_6.move ( V_11 , V_12 )

                if COUNT > 100:
                    #
                    E_1 , E_2 , E_3 , E_4 , E_5 , E_6 , E_7 , E_8 , E_9 , E_10 , E_11 , E_12 = Movement_3() 
                    #
                    time.sleep(0.02)
                    Text_1.move ( E_1 , E_2 )
                    Text_2.move ( E_3 , E_4 )
                    Text_3.move ( E_5 , E_6 )
                    Text_4.move ( E_7 , E_8 )
                    Text_5.move ( E_9 , E_10 )
                    Text_6.move ( E_11 , E_12 )

                if COUNT > 150:
                    #
                    R_1 , R_2 , R_3 , R_4 , R_5 , R_6 , R_7 , R_8 , R_9 , R_10 , R_11 , R_12 = Movement_4()
                    #
                    time.sleep(0.02)
                    Text_1.move( R_1 , R_2 )
                    Text_2.move( R_3 , R_4 )
                    Text_3.move( R_5 , R_6 )
                    Text_4.move( R_7 , R_8 )
                    Text_5.move( R_9 , R_10 )
                    Text_6.move( R_11 , R_12 )
                ##
                    

                #If Text_1 reaches a certain point on the y-axis (600) , elif statement activates.#
                elif Text_1.getAnchor().getY() > 600:
                    Text_1.undraw()
                    Text_2.undraw()
                    Text_3.undraw()
                    Text_4.undraw()
                    Text_5.undraw()
                    Text_6.undraw()
                    Text_Name.undraw()
                    VAR_3.undraw()
                    SCORE.undraw()
                    ENTRY.undraw()
                    Final_Text.draw( Window )
                    #Restarts the game if 'yes' , Records the score and exits the sys if 'no'.#
                    Input_Finish = input("Would you like to play again? Type 'yes' or 'no'!\n")
                    if Input_Finish == 'yes':
                        COUNT = 0
                        break
                    
                    if Input_Finish == 'no':
                        Score = COUNT
                        WPM_Times = int(Score)* 60
                        File_1.write(Name_Future + " , " + str(Score) + " " + "Words Per Minute!" +"\n")
                        File_1.write( str(WPM_Times) )
                        File_1.write( " " + "WPH! Good Job!\n" )
                        File_1.close()
                        sys.exit()
                        Window.close()
                    ##
                ##
                        
                    
                #If Text_2 reaches a certain point on the y-axis (600) , elif statement activates.#
                elif Text_2.getAnchor().getY() > 600:
                    Text_1.undraw()
                    Text_2.undraw()
                    Text_3.undraw()
                    Text_4.undraw()
                    Text_5.undraw()
                    Text_6.undraw()
                    Text_Name.undraw()
                    VAR_3.undraw()
                    SCORE.undraw()
                    ENTRY.undraw()
                    Final_Text.draw( Window )
                    #Restarts the game if 'yes' , Records the score and exits the sys if 'no'.#
                    Input_Finish = input("Would you like to play again? Type 'yes' or 'no'!\n")
                    if Input_Finish == 'yes':
                        COUNT = 0
                        break
                    
                    if Input_Finish == 'no':
                        Score = COUNT
                        WPM_Times = int(Score) * 60
                        File_1.write(Name_Future + " , " + str(Score) + " " + "Words Per Minute!" +"\n")
                        File_1.write( str(WPM_Times) )
                        File_1.write( " " + "WPH! Good Job!\n" )
                        File_1.close()
                        sys.exit()
                        Window.close()
                    ##
                ##
                        
                    
                #If Text_3 reaches a certain point on the y-axis (600), elif statement activates.#
                elif Text_3.getAnchor().getY() > 600:
                    Text_1.undraw()
                    Text_2.undraw()
                    Text_3.undraw()
                    Text_4.undraw()
                    Text_5.undraw()
                    Text_6.undraw()
                    Text_Name.undraw()
                    VAR_3.undraw()
                    SCORE.undraw()
                    ENTRY.undraw()
                    Final_Text.draw( Window )
                    #Restarts the game if 'yes' , Records the score and exits the sys if 'no'.#
                    Input_Finish = input("Would you like to play again? Type 'yes' or 'no'!\n")
                    if Input_Finish == 'yes':
                        COUNT = 0
                        break
                    
                    if Input_Finish == 'no':
                        Score = COUNT
                        WPM_Times = int(Score) * 60
                        File_1.write(Name_Future + " , " + str(Score) + " " + "Words Per Minute!"+ "\n")
                        File_1.write( str(WPM_Times) )
                        File_1.write( " " + "WPH! Good Job!\n" )
                        File_1.close()
                        sys.exit()
                        Window.close()
                    ##
                ##
                        
                    
                #If Text_4 reaches a certain point on the y-axis (600), elif statement activates.#  
                elif Text_4.getAnchor().getY() > 600:
                    Text_1.undraw()
                    Text_2.undraw()
                    Text_3.undraw()
                    Text_4.undraw()
                    Text_5.undraw()
                    Text_6.undraw()
                    Text_Name.undraw()
                    VAR_3.undraw()
                    SCORE.undraw()
                    ENTRY.undraw()
                    Final_Text.draw( Window )
                    #Restarts the game if 'yes' , Records the score and exits the sys if 'no'.#
                    Input_Finish = input("Would you like to play again? Type 'yes' or 'no'!\n")
                    if Input_Finish == 'yes':
                        COUNT = 0
                        break
                    
                    if Input_Finish == 'no':
                        Score = COUNT
                        WPM_Times = int(Score) * 60
                        File_1.write(Name_Future + " , " + str(Score) + " " + "Words Per Minute!" + "\n")
                        File_1.write( str(WPM_Times) )
                        File_1.write( " " + "WPH! Good Job!\n" )
                        File_1.close()
                        sys.exit()
                        Window.close()
                    ##
                ##


                #If Text_5 reaches a certain point on the y-axis (600), elif statement activates.#
                elif Text_5.getAnchor().getY() > 600:
                    Text_1.undraw()
                    Text_2.undraw()
                    Text_3.undraw()
                    Text_4.undraw()
                    Text_5.undraw()
                    Text_6.undraw()
                    Text_Name.undraw()
                    VAR_3.undraw()
                    SCORE.undraw()
                    ENTRY.undraw()
                    Final_Text.draw( Window )
                    #Restarts the game if 'yes' , Records the score and exits the sys if 'no'.#
                    Input_Finish = input("Would you like to play again? Type 'yes' or 'no'!\n")
                    if Input_Finish == 'yes':
                        COUNT = 0
                        break
                    
                    if Input_Finish == 'no':
                        Score = COUNT
                        WPM_Times = int(Score) * 60
                        File_1.write(Name_Future + " , " + " " + str(Score) + " " + "Words Per Minute!" +"\n")
                        File_1.write( str(WPM_Times) )
                        File_1.write( " " + "WPH! Good Job!\n" )
                        File_1.close()
                        sys.exit()
                        Window.close()
                    ##
                ##
        
                #If graphics window is closed prematurely, this if statement kills the process of the code when exited.#
                elif Window.isClosed():
                    sys.exit()
                ##

    Main_Game()
