import unittest
from interruptores import aLampadaEstaAcesa

class InterruptoresTestCase(unittest.TestCase):
	def test_a_lampada_deve_estar_desligada_se_nenhum_interruptor_for_acionado(self):
		interruptorDaEntradaDaCasa = False
		interruptorProximoDoQuarto = False

		comoEstaALampada = aLampadaEstaAcesa(interruptorDaEntradaDaCasa, interruptorProximoDoQuarto)

		self.assertFalse(comoEstaALampada)

unittest.main()
