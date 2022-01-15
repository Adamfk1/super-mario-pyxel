from interface import Interface
import pyxel

interface = Interface(450,320)

pyxel.init(interface.width, interface.height, title="Super Mario")

pyxel.load("assets/paloma.pyxres")

pyxel.run(interface.update, interface.draw)