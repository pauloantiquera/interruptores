def aLampadaEstaAcesa(interruptorDaEntradaDaCasa, interruptorProximoDoQuarto):
	if (interruptorDaEntradaDaCasa and not interruptorProximoDoQuarto):
		return True

	return False
