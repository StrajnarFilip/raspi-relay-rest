#!/bin/sh

python -m venv .
. ./bin/activate
pip install .
python src/raspi_relay_rest