from unittest import TestCase
from leilao.dominio import *


class TestLeilao(TestCase):


    def setUp(self):

        self.gui = Usuario('Gui', 500.00)
        self.felipe = Usuario('Felipe', 500.00)
        self.lance_do_felipe = Lance(self.felipe, 180.00)
        self.lance_do_gui = Lance(self.gui, 150.00)
        self.leilao = Leilao('Celular')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente(self):
        
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_felipe)

        menor_valor_esperado = 150.0
        maior_valor_esperado = 180.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
   
        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_felipe)
            self.leilao.propoe(self.lance_do_gui)

    def test_deve_retornar_o_mesmo_valor_para_o_maior_e_o_menor_lance_quando_leilao_tiver_um_lance(self):
        
        self.leilao.propoe(self.lance_do_gui)

        self.assertEqual(150.0, self.leilao.menor_lance)
        self.assertEqual(150.0, self.leilao.maior_lance)


    
    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_leilao_com_tres_lances(self):
        yuri = Usuario('Yuri', 500.00)
        lance_do_yuri = Lance(yuri, 120.00)
        
        
        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(self.lance_do_felipe)
        

        menor_valor_esperado = 120.0
        maior_valor_esperado = 180.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)


    #se o leilao nao tiver lances, deve permitir propor um lance
    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        
        self.leilao.propoe(self.lance_do_gui)

        quantidade_lances_recebida = len(self.leilao.lances)

        self.assertEqual(1, quantidade_lances_recebida)

    #se o ultimo usuario for diferente, deve permitir propor o lance

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('Yuri', 500.00)
        lance_do_yuri = Lance(yuri, 200.0)

        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)
        quantidade_lances_recebido = len(self.leilao.lances)

        self.assertEqual(2, quantidade_lances_recebido)

    #se o usuario for o mesmo, nao deve permitir propor o lance

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_seja_o_mesmo(self):
        lance_do_gui200 = Lance(self.gui, 200.0)

        with self.assertRaises(ValueError):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(lance_do_gui200)


    