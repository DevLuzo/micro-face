def on_gesture_tilt_right():
    basic.show_icon(IconNames.GHOST)
input.on_gesture(Gesture.TILT_RIGHT, on_gesture_tilt_right)

def on_gesture_tilt_left():
    basic.show_icon(IconNames.MEH)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_screen_up():
    basic.show_icon(IconNames.ASLEEP)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_button_pressed_a():
    basic.show_icon(IconNames.PITCHFORK)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_six_g():
    basic.show_icon(IconNames.COW)
input.on_gesture(Gesture.SIX_G, on_gesture_six_g)

def on_gesture_free_fall():
    basic.show_icon(IconNames.SKULL)
input.on_gesture(Gesture.FREE_FALL, on_gesture_free_fall)

def on_gesture_logo_down():
    basic.show_icon(IconNames.BUTTERFLY)
input.on_gesture(Gesture.LOGO_DOWN, on_gesture_logo_down)

def on_gesture_shake():
    basic.show_icon(IconNames.ANGRY)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_gesture_screen_down():
    basic.show_icon(IconNames.HAPPY)
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

def on_gesture_three_g():
    basic.show_icon(IconNames.TORTOISE)
input.on_gesture(Gesture.THREE_G, on_gesture_three_g)

def on_gesture_eight_g():
    basic.show_icon(IconNames.LEFT_TRIANGLE)
input.on_gesture(Gesture.EIGHT_G, on_gesture_eight_g)

def on_button_pressed_ab():
    basic.show_icon(IconNames.GIRAFFE)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    basic.show_icon(IconNames.COW)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_logo_up():
    basic.show_icon(IconNames.HAPPY)
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

basic.show_icon(IconNames.HAPPY)
basic.pause(3000)
basic.clear_screen()