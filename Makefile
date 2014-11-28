make:
	rm -Rf dist
#	python ~/Documents/src/pyinstaller-2.0/utils/Makespec.py --onefile -p htdocs server.py
	python ~/Documents/src/pyinstaller-2.0/utils/Build.py server.spec
#	rm server.spec
#	rm -Rf build
	
clean:
	rm -Rf dist
	rm -Rf build
