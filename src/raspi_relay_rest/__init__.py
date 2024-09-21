# SPDX-FileCopyrightText: 2024-present Filip Strajnar <filip.strajnar@gmail.com>
#
# SPDX-License-Identifier: MIT

from flask import Flask

app = Flask(__name__)

@app.route("/ping")
def hello_world():
    return "pong"