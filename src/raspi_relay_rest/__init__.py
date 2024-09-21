# SPDX-FileCopyrightText: 2024-present Filip Strajnar <filip.strajnar@gmail.com>
#
# SPDX-License-Identifier: MIT

from flask import Flask, request
import gpiozero

app = Flask(__name__)

@app.route("/ping")
def hello_world():
    return "pong"

@app.route("/led/<int:number>/<state>")
def led_state(number: int, state: str):
    led = gpiozero.LED(number)
    if state == "on":
        led.on()
        return led.value
    if state == "off":
        led.off()
        return led.value
    
    return "State may only be 'on' or 'off'."

@app.route("/led-blink/<int:number>")
def led_blink(number: int):
    led = gpiozero.LED(number)
    blink_duration: int = int(request.args.get("duration", 1))
    led.blink(blink_duration, n = 1)
    return blink_duration