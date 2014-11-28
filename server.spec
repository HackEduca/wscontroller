# -*- mode: python -*-
a = Analysis(['server.py'],
             pathex=['/users/mb/Documents/src/wsController'],
             hiddenimports=[],
             hookspath=None)
pyz = PYZ(a.pure)

a.datas = [
("htdocs/index.html", "htdocs/index.html", 'DATA'),
("htdocs/touchpad.html", "htdocs/touchpad.html", 'DATA'),
("htdocs/touchControl.html", "htdocs/touchControl.html", 'DATA'),
("htdocs/js/Vector2.js", "htdocs/js/Vector2.js", 'DATA')
]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name=os.path.join('dist', 'server'),
          debug=False,
          strip=None,
          upx=True,
          console=True )
