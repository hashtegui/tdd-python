from dominio import Avaliador, Usuario, Lance, Leilao


gui = Usuario("Gui")
yuri = Usuario("Yuri")
felipe = Usuario('Felipe')

lance_do_felipe = Lance(felipe, 180.00)
lance_do_yuri = Lance(yuri, 120.00)
lance_do_gui = Lance(gui, 150.00)

leilao = Leilao('Celular')

leilao.lances.append(lance_do_yuri)
leilao.lances.append(lance_do_felipe)
leilao.lances.append(lance_do_gui)


for lance in leilao.lances:
    print(f'o Usuario {lance.usuario.nome} deu um lance de {lance.valor}')


avaliador = Avaliador()

avaliador.avalia(leilao)

print(f'o menor lance foi de {avaliador.menor_lance} e o maior lance foi de {avaliador.maior_lance}')
