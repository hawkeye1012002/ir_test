makerbit.onIrDatagram(function () {
    basic.showString(makerbit.irDatagram())
})
makerbit.connectIrReceiver(DigitalPin.P1, IrProtocol.NEC)
basic.showNumber(0)
basic.forever(function () {
	
})
