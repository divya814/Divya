# SNAKE AND LADDER GAME
from PIL import Image
import random
end=100
def show_board():
    img=Image.open("snakes-and-ladders.jpg")
    img.show()

def check_ladder(points):
    if points==3:
        print("Wow! Ladder")
        return 20
    elif points==6:
        print("Wow! Ladder")
        return 14
    elif points==11:
        print("Wow! Ladder")
        return 28
    elif points==15:
        print("Wow! Ladder")
        return 34
    elif points==17:
        print("Wow! Ladder")
        return 74
    elif points==22:
        print("Wow! Ladder")
        return 37
    elif points==38:
        print("Wow! Ladder")
        return 59
    elif points==49:
        print("Wow! Ladder")
        return 67
    elif points==57:
        print("Wow! Ladder")
        return 76
    elif points==61:
        print("Wow! Ladder")
        return 78
    elif points==73:
        print("Wow! Ladder")
        return 86
    elif points==81:
        print("Wow! Ladder")
        return 98
    elif points==88:
        print("Wow! Ladder")
        return 91
    else:
        return points

def check_snake(points):
    if points==8:
        print("Oops! Snake")
        return 4
    elif points==18:
        print("Oops! Snake")
        return 1
    elif points==26:
        print("Oops! Snake")
        return 10
    elif points==39:
        print("Oops! Snake")
        return 5
    elif points==51:
        print("Oops! Snake")
        return 6
    elif points==54:
        print("Oops! Snake")
        return 36
    elif points==56:
        print("Oops! Snake")
        return 1
    elif points==60:
        print("Oops! Snake")
        return 23
    elif points==75:
        print("Oops! Snake")
        return 28
    elif points==83:
        print("Oops! Snake")
        return 45
    elif points==85:
        print("Oops! Snake")
        return 59
    elif points==90:
        print("Oops! Snake")
        return 48
    elif points==92:
        print("Oops! Snake")
        return 25
    elif points==70:
        print("Oops! Snake")
        return 87
    elif points==99:
        print("Oops! Snake")
        return 63
    else:
        return points
        
def reached_end(points):
    if points==end:
        return True
    else:
        return False

def play():
    # input each players name
    p1_name=input("Player1, Please enter your name:")
    p2_name=input("Player2, Please enter your name:")
    # intial points of both the players
    points_1=0
    points_2=0
    turn=0
    while(1):
        if turn%2==0:
            print(p1_name," your turn")
            # ask player's choice to continue
            c=int(input("Press 1 to continue and 0 to quit "))
            if c==0:
                print(p1_name, "scored ",points_1)
                print(p2_name, "scored ",points_2)
                print("Quited the game, Thanks for playing")
                break
            else:
                # dice rolls, generating a no. from 1 to 6
                dice=random.randint(1,6)
                print("Dice showed: ",dice)
                points_1 += dice
                points_1 = check_ladder(points_1)
                points_1= check_snake(points_1)
                if points_1>end:
                    points_1=end
                print(p1_name," Your score: ",points_1)
                if reached_end(points_1):
                    print(p1_name, "Won!!!")
                    break
        else:
            print(p2_name," your turn")
            # ask player's choice to continue
            c=int(input("Press 1 to continue and 0 to quit "))
            if c==0:
                print(p1_name, "scored ",points_1)
                print(p2_name, "scored ",points_2)
                print("Quited the game, Thanks for playing")
                break
            else:
                # dice rolls, generating a no. from 1 to 6
                dice=random.randint(1,6)
                print("Dice showed:",dice)
                points_2 += dice
                points_2 = check_ladder(points_2)
                points_2= check_snake(points_2)
                if points_2>end:
                    points_2=end
                print(p2_name,"Your score:",points_2)
                if reached_end(points_2):
                    print(p2_name, "Won!!!")
                    break
        turn += 1
            
            
show_board()
play()
