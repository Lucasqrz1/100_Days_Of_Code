def turn_right ():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        if wall_in_front():
            turn_left()
        move()
    turn_right()
    move()
    turn_right()
        
while front_is_clear():
    move()
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
