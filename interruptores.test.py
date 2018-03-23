import unittest
from interruptores import aLampadaEstaAcesa

class InterruptoresTestCase(unittest.TestCase):
	def test_a_lampada_deve_estar_desligada_se_nenhum_interruptor_for_acionado(self):
		interruptorDaEntradaDaCasa = False
		interruptorProximoDoQuarto = False

		comoEstaALampada = aLampadaEstaAcesa(interruptorDaEntradaDaCasa, interruptorProximoDoQuarto)

		self.assertFalse(comoEstaALampada)
	
	def test_a_lampada_deve_estar_acesa_se_o_interruptor_da_entrada_da_casa_estiver_acionado(self):
		interruptorDaEntradaDaCasa = True
		interruptorProximoDoQuarto = False

		comoEstaALampada = aLampadaEstaAcesa(interruptorDaEntradaDaCasa, interruptorProximoDoQuarto)

		self.assertTrue(comoEstaALampada)

	def test_a_lampada_deve_estar_apagada_se_apos_acionar_o_interruptor_da_entrada_da_casa_e_acionar_tambem_o_interruptor_perto_do_quarto(self):
		interruptorDaEntradaDaCasa = True
		interruptorProximoDoQuarto = True

		comoEstaALampada = aLampadaEstaAcesa(interruptorDaEntradaDaCasa, interruptorProximoDoQuarto)

		self.assertFalse(comoEstaALampada)
	
	def test_a_lampada_deve_estar_acesa_se_o_interruptor_proximo_do_quarto_estiver_acionado(self):
		interruptorDaEntradaDaCasa = False
		interruptorProximoDoQuarto = True

		comoEstaALampada = aLampadaEstaAcesa(interruptorDaEntradaDaCasa, interruptorProximoDoQuarto)

		self.assertTrue(comoEstaALampada)

unittest.main()
