strip: neopixel.Strip = None

def on_button_pressed_ab():
    for index in range(4):
        music.play_melody("C A C5 E G D F A ", 200)
        maqueen.motor_run(maqueen.Motors.ALL, maqueen.Dir.CW, 255)
        strip.show_color(neopixel.colors(NeoPixelColors.GREEN))
        basic.pause(2000)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
        strip.show_color(neopixel.colors(NeoPixelColors.RED))
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_ON)
        basic.pause(2000)
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
        maqueen.motor_run(maqueen.Motors.M1, maqueen.Dir.CW, 255)
        strip.show_color(neopixel.colors(NeoPixelColors.BLUE))
        maqueen.write_led(maqueen.LED.LED_LEFT, maqueen.LEDswitch.TURN_OFF)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_ON)
        basic.pause(2000)
        maqueen.write_led(maqueen.LED.LED_RIGHT, maqueen.LEDswitch.TURN_OFF)
        music.play_melody("G F G A - F E D ", 200)
        maqueen.motor_run(maqueen.Motors.M2, maqueen.Dir.CW, 255)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_forever():
    global strip
    basic.show_icon(IconNames.HAPPY)
    strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
basic.forever(on_forever)
