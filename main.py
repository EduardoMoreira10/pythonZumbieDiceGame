import random
from time import sleep
from collections import namedtuple
print(f'{"PONTIFÍCIA UNIVERSIDADE CATÓLICA DO PARANÁ":^100}')
print(f'{"PROTÓTIPO ZUMBIE DICE":^100}')
print(f'{"ALUNO: EDUARDO MOREIRA":^100}')
print(f'{"CURSO: TECNÓLOGO EM ANÁLISE E DESEMVOLVIMENTO DE SISTEMAS":^100}')

class players:

    def __init__(self):
        self.__numero_de_jogadores = 0
        self.__cont_jogadores = list()

    def get_jogadores(self):
        return self.__numero_de_jogadores

    def lista_jogadores(self):
        return self.__cont_jogadores

    def set_jogadores(self, cont_jogadores):
        self.__cont_jogadores = cont_jogadores

    def definicao_jogadores(self):

        print(f'{"SEJA BEM VINDO AO ZOMBIE DICE!!!":^100}\n\n')

        print(f'{"O Zombie Dice Game vem com 13 dados representando as vítimas dos mortos-vivos,":^100}')
        print(f'{"O jogador deve tentar comer os miolos das vítimas antes de tomar um tiro de espingarda.":^100}')
        print(f'{"O jogador que comer 13 cérebros antes vence a partida.":^100}')
        print(f'{"Caso você tome 3 tiros seguidos você automaticamente passa a vez para o próximo jogador!":^100}\n')
        print('*'*100)
        print(f'{"VAMOS CONHECER OS JOGADORES!!!":^100}')
        print('*' * 100)

        while True:
            self.__numero_de_jogadores += 1
            self.__cont_jogadores.append([input(f'{cores.coloracao("azul")}'f'DIGITE O NOME DO JOGADOR {self.__numero_de_jogadores}º: \n'), 0])
            if self.__numero_de_jogadores >= 2:
                if not Contadores.quer_continuar(f'{cores.coloracao("verde")}''VOCÊ DESEJA ADICIONAR UM NOVO JOGADOR?'):
                    break
        print('\n')

    def mostra_cerebros_comidos(self):

        print('CHECKPOINT DE CÉREBROS')
        for k in range(len(self.__cont_jogadores)):
            print(f'{self.__cont_jogadores[k][0] + " ":.<36} {self.__cont_jogadores[k][1]}')
            sleep(0.5)

    @staticmethod
    def mostra_cerebros_do_player(cerebro_player, conta_cerebro):

        pintar = Cores()
        print(f'Total de cérebros devorados: {pintar.coloracao("azul")}de {cerebro_player} '
              f'para {cerebro_player + conta_cerebro}{pintar.stop_cor()}')

    def check_cerebros(self, cerebros_vitoriosos):

        aux = list()
        for x in self.__cont_jogadores:
            aux.append(x[1])
        maior_cerebro = max(aux)
        if maior_cerebro >= cerebros_vitoriosos:
            return True, maior_cerebro
        else:
            return False, maior_cerebro

    def empate(self, cerebro_max):

        campeao = []
        for a in self.__cont_jogadores:
            if a[1] == cerebro_max:
                campeao.append(a)
        if len(campeao) > 1:
            return True, campeao
        else:
            return False, campeao

    @staticmethod
    def tiros_tomados(lista_tiros, limite_tiros):

        if lista_tiros >= limite_tiros:
            return True
        else:
            return False


class Dados:

    def __init__(self):
        self.__definir_cor = namedtuple('dados_cor', 'verde amarelo vermelho')
        self.__dados_do_copo = self.__definir_cor(('cérebro', 'passo', 'cérebro', 'tiro', 'passo', 'cérebro'),
                                       ('tiro', 'passo', 'cérebro', 'tiro', 'passo', 'cérebro'),
                                       ('tiro', 'passo', 'tiro', 'cérebro', 'passo', 'tiro'))
        self.__recipiente = list()
        self.__definir_sorteio = {}

        self.__pintar_face = namedtuple('cor_face', 'cor face')

    def rever_copo(self):
        return self.__recipiente

    def definir_dado(self):
        return self.__dados_do_copo

    def listar_sorteio(self):
        return self.__definir_sorteio

    def mostrar_o_sorteio(self, i, cor, face):
        self.__definir_sorteio[i] = self.__pintar_face(cor, face)

    def formatar_copo(self):

        self.__recipiente = ['verde', 'verde', 'verde', 'verde', 'verde', 'verde',
                       'amarelo', 'amarelo', 'amarelo', 'amarelo',
                       'vermelho', 'vermelho', 'vermelho']

    def formata_dado(self):

        self.__definir_sorteio = {f'primeirodado': self.__pintar_face('', ''), 'segundodado': self.__pintar_face('', ''), 'terceirodado': self.__pintar_face('', '')}

    def qual_dado_escolhido(self):

        return self.__recipiente[random.randrange(len(self.__recipiente))]

    def tira_dado(self, cor_dado):

        self.__recipiente.remove(cor_dado)

    def escolhe_face(self, cor):

        return random.choice(self.definir_dado().__getattribute__(cor))


    @staticmethod
    def mostra_dado_sorteado(i, dado_sort):

        pintar = Cores()
        print(f' O dado {i + 1} '
              f'{pintar.coloracao(dado_sort.cor)}'
              f'{dado_sort.cor:^10}{pintar.stop_cor()} '
              f'caiu um {dado_sort.face.upper():^10}')

    @staticmethod
    def mostra_dados_elegiveis(mostraP, resto):

        print(f'Dados que podem ser sorteados: {mostraP + resto} - '
              f'{resto} dados que sobraram no copo + {mostraP} passos')

    @staticmethod
    def tem_dados_suficientes(conta_passos, num_dados_copo, qtd_dados_sortear):

        if conta_passos + num_dados_copo < qtd_dados_sortear:
            return False
        else:
            return True

class Cores:

    def __init__(self):
        self.__fg = {'branco': 30, 'vermelho': 31, 'verde': 32, 'amarelo': 33,
                     'azul': 34, 'magenta': 35, 'cyan': 36, 'cinza': 37, 'cinza escuro': 90,
                     'vermelho claro': 91, 'verde claro': 92, 'amarelo claro': 93,
                     'azul claro': 94, 'magenta claro': 95, 'cyan claro': 96}
        self.__bg = {'branco': 40, 'vermelho': 41, 'verde': 42, 'amarelo': 43,
                     'azul': 44, 'magenta': 45, 'cyan': 46, 'cinza': 47, 'cinza escuro': 100,
                     'vermelho claro': 101, 'verde claro': 102, 'amarelo claro': 103,
                     'azul claro': 104, 'magenta claro': 105, 'cyan claro': 106}

    def coloracao(self, cor_da_fonte, cor_do_fundo=''):
        fundo_cor = ''
        if cor_do_fundo:
            fundo_cor = f';{self.__bg[cor_do_fundo]}'
        return '\033[1;' + str(self.__fg[cor_da_fonte]) + fundo_cor + 'm'

    @staticmethod
    def stop_cor():
        return '\033[0;0m'


class Contadores:

    def __init__(self, tiros_tomados=3, cerebros_campeao=13, dados_para_sortear=3):
        self.__tiros_tomados = tiros_tomados
        self.__vitoria = cerebros_campeao
        self.__dados_para_sortear = dados_para_sortear
        self.__contagem_ = {}
        self.__turno = 0

    def tiros_tomados(self):
        return self.__tiros_tomados

    def cerebros_vencedor(self):
        return self.__vitoria

    def get_dados_para_sortear(self):
        return self.__dados_para_sortear

    def get_conts(self):
        return self.__contadores_ctp

    def set_conts(self, face_do_dado):

        if face_do_dado == 'cérebro':
            self.__contadores_ctp['contC'] += 1
        elif face_do_dado == 'tiro':
            self.__contadores_ctp['contT'] += 1
        else:
            self.__contadores_ctp['contP'] += 1

    def get_turno(self):
        return self.__turno

    def set_turno(self, turno):
        self.__turno = turno

    def inicializa_contadores(self):
        self.__contadores_ctp = {'contC': 0, 'contT': 0, 'contP': 0}

    def mostra_contadores_ctp(self):

        print(f'\033[1;35m----- Cérebros: {self.get_conts()["contC"]} ----- '
              f'Passos: {self.get_conts()["contP"]} ----- '
              f'Tiros: {self.get_conts()["contT"]} -----\033[0;0m')

    @staticmethod
    def quer_continuar(mensagem):

        pintar = Cores()
        posicao = str(input(f'{mensagem} (S/N) '))
        while posicao not in 'sSnN' or posicao == '':
            print(f'{pintar.coloracao("vermelho claro")}Opção inválida. '
                  f'Digite S para Sim ou N para Não. {pintar.stop_cor()}', end='')
            posicao = str(input(f'{mensagem} (S/N) ')).upper()
        if posicao in 'nN':
            return False
        else:
            return True

    @staticmethod
    def dormir(time, pontuacao):

        for _ in range(pontuacao):
            print('. ', end='')
            sleep(time)

dados = Dados()
cores = Cores()
contadores = Contadores(3, 13, 3)
jogadores = players()


print('#' *100)
print(f'{"Z  O  M  B  I  E     D  I  C  E":^100}')
print('#' * 100)
print('\n')

jogadores.definicao_jogadores()

while True:
    contadores.set_turno(contadores.get_turno() + 1)
    print(f'{cores.coloracao("cyan claro")}')
    print('*' * 100)
    print(f'{cores.coloracao("cyan claro")}'f'{"RODADA " + str(contadores.get_turno()):^100}')
    print('*' * 100)
    print('\n')

    for cont_jog in range(len(jogadores.lista_jogadores())):

        dados.formatar_copo()

        contadores.inicializa_contadores()

        dados.formata_dado()

        print(f'{cores.coloracao("magenta claro")}'
              f'{" TURNO DO JOGADOR " + jogadores.lista_jogadores()[cont_jog][0].upper() + " ":=^100}'
              f'{cores.stop_cor()}')
        print(f'{"TOTAL DE CÉREBROS: " + str(jogadores.lista_jogadores()[cont_jog][1]) + " cérebros.":^100}\n')

        while True:
            for indice, dado in enumerate(dados.listar_sorteio()):
                dado_sorteado_cor = ''

                if dados.listar_sorteio()[dado].face != 'passo':
                    dado_sorteado_cor = dados.qual_dado_escolhido()
                    dados.tira_dado(dado_sorteado_cor)

                else:
                    dado_sorteado_cor = dados.listar_sorteio()[dado].cor

                face_dado = dados.escolhe_face(dado_sorteado_cor)

                dados. mostrar_o_sorteio(dado, dado_sorteado_cor, face_dado)
                dados.mostra_dado_sorteado(indice, dados.listar_sorteio()[dado])

                contadores.set_conts(dados.listar_sorteio()[dado].face)

            contadores.mostra_contadores_ctp()

            dados.mostra_dados_elegiveis(contadores.get_conts()['contP'], len(dados.rever_copo()))
            jogadores. mostra_cerebros_do_player(jogadores.lista_jogadores()[cont_jog][1],
                                              contadores.get_conts()["contC"])

            if jogadores.tiros_tomados(contadores.get_conts()['contT'], contadores.tiros_tomados()):

                print(f'{cores.coloracao("vermelho claro")}Você recebeu muitos tiros, passando para o próximo jogar! '
                      f'[{contadores.get_conts()["contT"]}].{cores.stop_cor()} '
                      f'TURNO ACABADO, VOCÊ NÃO PONTUOU.')
                contadores.dormir(0.5, 7)
                print('\n')
                break
            elif not dados.tem_dados_suficientes(contadores.get_conts()['contP'],
                                                 len(dados.rever_copo()), contadores.get_dados_para_sortear()):

                print(f'{cores.coloracao("amarelo claro")}Número de dados insuficientes para uma nova rodada. '
                      f'[{contadores.get_conts()["contP"] + len(dados.rever_copo())}].{cores.stop_cor()}')
                print('Cérebros contabilizados e turno finalizado.')
                jogadores.lista_jogadores()[cont_jog][1] += contadores.get_conts()['contC']
                contadores.dormir(0.3, 5)
                print('\n')
                break
            else:
                if not contadores.quer_continuar('JOGAR NOVAMENTE? '):

                    jogadores.lista_jogadores()[cont_jog][1] += contadores.get_conts()['contC']
                    print('\n')
                    break
                else:
                    contadores.get_conts()['contP'] = 0
                    print('='*100)

    cerebros_final = jogadores.check_cerebros(contadores.cerebros_vencedor())
    if cerebros_final[0]:
        empatou = jogadores.empate(cerebros_final[1])
        if empatou[0]:
            jogadores.mostra_cerebros_comidos()
            print(f'\n{cores.coloracao("amarelo")}')
            print('#' * 30)
            print(f'{"JOGO EMPATADO":^30}')
            print('#' * 30)
            print(f'{cores.stop_cor()}', end='')
            print(f'CÉREBROS COMIDOS: {cerebros_final[1]}')
            print('' * 18)
            print('\nJOGADORES QUE JOGARAM O DESEMPATE:')
            jogadores.set_jogadores(empatou[1])
            jogadores.mostra_cerebros_comidos()
            contadores.dormir(0.3, 5)
            print('\n')
        else:
            print('#'*100)
            print(f'{"TEMOS UM VENCEDOR ZOMBIE DICE":^100}\n')
            print(f'PARABÉNS {empatou[1][0][0]}')
            print(f'VOCÊ COMEU {empatou[1][0][1]} CÉREBROS.\n')
            jogadores.mostra_cerebros_comidos()
            break

print('\n\nFIM DO JOGO')