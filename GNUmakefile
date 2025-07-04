# Miguel Angel Marcial Martinez - Fitorec 2025
#
#       (o_
#  (o_  //\
#  (/)_ V_/_
#

.PHONY: build clean

VENV_DIR := venv
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip
SVG := codigo_de_conducta.svg
PNG := codigo_de_conducta.png

build: $(PNG)

$(VENV_DIR)/bin/activate:
	python3 -m venv $(VENV_DIR)
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

$(PNG): svg2png.py $(SVG) $(VENV_DIR)/bin/activate
	$(PYTHON) svg2png.py -i $(SVG) -o $(PNG)

clean:
	rm -f $(PNG)
