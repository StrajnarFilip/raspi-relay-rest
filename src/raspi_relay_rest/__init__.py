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
    led = gpiozero.LED(number, active_high=False)
    if state == "on":
        led.on()
    if state == "off":
        led.off()
    
    led_value = led.value
    led.close()
    return str(led_value)

@app.route("/led-blink/<int:number>")
def led_blink(number: int):
    led = gpiozero.LED(number, active_high=False)
    blink_duration: int = int(request.args.get("duration", 1))
    led.blink(blink_duration, n = 1, background=False)
    led.close()
    return str(blink_duration)