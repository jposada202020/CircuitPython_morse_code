from mc_emitter import Emitter
import board

internal_led = Emitter(board.D13)

internal_led.outmorse("Hugo AKA the Architect")
