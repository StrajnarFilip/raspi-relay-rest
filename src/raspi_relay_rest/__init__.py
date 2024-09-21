# SPDX-FileCopyrightText: 2024-present Filip Strajnar <filip.strajnar@gmail.com>
#
# SPDX-License-Identifier: MIT

from flask import Flask
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