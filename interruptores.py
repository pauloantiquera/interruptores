def aLampadaEstaAcesa(interruptorDaEntradaDaCasa, interruptorProximoDoQuarto):
	if (interruptorDaEntradaDaCasa and not interruptorProximoDoQuarto):
		return True
	
	if (not interruptorDaEntradaDaCasa and interruptorProximoDoQuarto):
		return True

	return False
