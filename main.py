def on_ir_datagram():
    basic.show_string(makerbit.ir_datagram())
makerbit.on_ir_datagram(on_ir_datagram)

makerbit.connect_ir_receiver(DigitalPin.P1, IrProtocol.NEC)
basic.show_number(0)

def on_forever():
    pass
basic.forever(on_forever)
