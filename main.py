import itertools
import random
from time import sleep
import os

class Player:
    '''
    Classe simples para um jogador

    Atributos:
        balance = Saldo do jogador
    '''
    def __init__(self, balence=0): 
        self.balance = balence

class CassaNiquel:
    '''
    Classe representando uma maquina

    Atributos:
        SIMBOLOS (dict): EMOJIS da maquina
        level (int): Dificuldade da maquina (quanto maior mais facil de ganhar)
        permutations (list): Lista com todas as possibilidade de resultado
        balance (float): Saldo da maquina
        initial_balance = Saldo inicial da maquina
    '''
    def __init__(self, level= 1, balance= 0):
        self.SIMBOLOS = {
            'money_mouth_face': '1F911',
            'cold_face': '1F976',
            'alien': '1F47D',
            'heart_on_fire': '2764',
            'collision': '1F4A5'
        }
        self.level = level
        self.permutations = self._gen_permutations()
        self.balance = balance
        self.initial_balance = self.balance


    def _gen_permutations(self):
        ''' Gera todas as possibilidades de resultados '''

        permutations = list(itertools.product(self.SIMBOLOS.keys(), repeat=3))
        for j in range(self.level):
            for i in self.SIMBOLOS.keys():
                permutations.append((i, i, i))
        return permutations
    
    def _get_final_result(self):
        ''' Retorna uma possibilidade '''
        if not hasattr(self, 'permutations'):
            self.permutations = self._gen_permutations()

        result = list(random.choice(self.permutations))
        # Manipulação para ter mais chance de cair 2 simbolos iguais, criando uma falsa esperança no jogador
        if len(set(result)) == 3 and random.randint(0,5) >= 2:
            result[1] = result[0]
        return result
    
    def _display(self, amout_bet, result, time=0.3):
        ''' Representa a tela da maquina, imprimindo os emojis '''
        seconds = 2
        for i in range(0, int(seconds/time)):
            print(self._emojize(random.choice(self.permutations)))
            sleep(time)
            os.system('cls')
        print(self._emojize(result))

        if self._check_result_user(result):
            print(f'Você venceu e recebeu: {amout_bet*3}')
        else:
            print('Foi quase, tente novamente.')

    def _emojize(self, emojis):
        ''' Converte os códigos em emojis '''
        return ''.join(tuple(chr(int(self.SIMBOLOS[code], 16)) for code in emojis))
    
    def _check_result_user(self, result):
        ''' Confere o resultado o final, retornando um booleano'''
        x = [result[0] == x for x in result]
        return True if all(x) else False
    
    def _update_balance(self, amout_bet, result, player: Player):
        ''' Altera o saldo (Maquina/Jogador) '''
        if self._check_result_user(result):
            self.balance -= (amout_bet * 3)
            player.balance += (amout_bet * 3)
        else:
            self.balance += amout_bet
            player.balance -= amout_bet
    
    def play(self, amout_bet, player: Player, display= True):
        '''
        Executa uma jogada no caça-níquel.

        Este método simula uma rodada de jogo, gira a máquina e atualiza os saldos
        do jogador e da máquina com base no resultado.

        Atributos:
            amout_bet (float): Valor da aposta.
            player (Player): O objeto do jogador.
            display (bool): Se True, mostra a animação de giro da máquina.
        '''

        result = self._get_final_result()
        if display:
            self._display(amout_bet, result)
        self._update_balance(amout_bet, result, player)

    @property
    def gain(self):
        ''' Ganho da maquina '''
        return self.initial_balance + self.balance
    