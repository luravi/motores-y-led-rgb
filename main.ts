let strip: neopixel.Strip = null
input.onButtonPressed(Button.AB, function () {
    for (let index = 0; index < 4; index++) {
        music.playMelody("C A C5 E G D F A ", 200)
        maqueen.motorRun(maqueen.Motors.All, maqueen.Dir.CW, 255)
        strip.showColor(neopixel.colors(NeoPixelColors.Green))
        basic.pause(2000)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 255)
        strip.showColor(neopixel.colors(NeoPixelColors.Red))
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOn)
        basic.pause(2000)
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
        maqueen.motorRun(maqueen.Motors.M1, maqueen.Dir.CW, 255)
        strip.showColor(neopixel.colors(NeoPixelColors.Blue))
        maqueen.writeLED(maqueen.LED.LEDLeft, maqueen.LEDswitch.turnOff)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOn)
        basic.pause(2000)
        maqueen.writeLED(maqueen.LED.LEDRight, maqueen.LEDswitch.turnOff)
        music.playMelody("G F G A - F E D ", 200)
        maqueen.motorRun(maqueen.Motors.M2, maqueen.Dir.CW, 255)
    }
})
basic.forever(function () {
    basic.showIcon(IconNames.Happy)
    strip = neopixel.create(DigitalPin.P15, 4, NeoPixelMode.RGB)
})
