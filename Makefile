all: build run

install:
	pip install pyinstaller

build:
	@which pyinstaller > /dev/null || { echo "PyInstaller not found, please install it."; exit 1; }
	pyinstaller -F -n virus main.py

run:
	chmod 777 ./dist/virus
	./dist/virus

clean:
	rm -rf dist build virus.spec
	find . -name "*.pyc" -delete
	find . -name "__pycache__" -delete
