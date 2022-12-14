import pygame
from random import choice


class Tecla:
    '''define velocidade, posição das teclas, condições de fim de jogo'''

    #cria conceitos de x, y e velocidade, utilizados no dicionário de assets
    #também define altura e imagem comum para teclas
    def __init__(self, x, y, vel):
        self.vel = vel 
        self.x = x
        self.y = y 
        self.altura = 187
        self.tecla = pygame.image.load('tecla comum.png')
    
    #fórmula que checa se as teclas colidiram, e retorna true ou false
    def colidiu(self, outra_t):
        if self.y + self.altura > outra_t.y and outra_t.y + outra_t.altura > self.y:
            return True
        else:
            return False


    def atualiza_estado_1(self, delta_t, state, assets):
        #define noção de posição
        self.y = self.y + self.vel*(delta_t/1000)
        #define velocidade que aumenta de acordo com os pontos
        self.vel = 95 + state['pontos']
        if self.y > 530:
            #gera teclas aleatoriamente e as posiciona no início da tela
            #checa colisão e troca a tecla por verde quando o momento chegar
            self.x = choice([1, 80, 155, 232]) 
            self.y = -100
            self.tecla = choice([assets['tecla comum'], assets['tecla preta']])
            colidindo = True
            while colidindo:
                colidindo = False
                for t in state['teclas']:
                    if t != self and self.colidiu(t):
                        self.y = t.y - self.altura - 10
                        colidindo = True
            if state['pontos'] > 400:
                self.tecla = assets['tecla verde']
        
            
    #desenha a tecla levando em conta x, y e a tecla padrão, que pode ser longa ou normal como definida acima
    def desenha(self, window):
        window.blit(self.tecla, (self.x, self.y)) 
         
    #confere os cliques em cada coluna
    #é considerado como erro quando um jogador aperta uma tecla correspondente à coluna errada. apenas deixar uma tecla passar não é considerado um erro.
    def confere_cliques(self, assets, ev, state):
        if self.tecla == assets['tecla preta']:
            if self.y > 335 and self.y < 540:
                if ev.type == pygame.KEYDOWN:
                    if self.x == 1:
                        if ev.key == pygame.K_d:
                            state['pontos'] +=1
                            pygame.mixer.Sound.play(assets['tecla_1'])
                            self.tecla = assets['tecla dourada']
        
                            
                    
                    if self.x == 80:
                        if ev.key == pygame.K_f:
                            state['pontos'] +=1
                            pygame.mixer.Sound.play(assets['tecla_2'])
                            self.tecla = assets['tecla dourada']
                        
                    if self.x == 155:
                        if ev.key == pygame.K_j: 
                            state['pontos'] +=1
                            pygame.mixer.Sound.play(assets['tecla_3'])
                            self.tecla = assets['tecla dourada']
                    
                        
                    if self.x == 232:
                        if ev.key == pygame.K_k:
                            state['pontos'] +=1
                            pygame.mixer.Sound.play(assets['tecla_4'])
                            self.tecla = assets['tecla dourada']

        if self.tecla == assets['tecla preta']:
            if self.y > 335 and self.y < 540:
                if ev.type == pygame.KEYUP:
                    if self.x == 1:
                        if ev.key != pygame.K_d:
                            state['erros'] +=1
    
                    if self.x == 80:
                        if ev.key != pygame.K_f:
                            state['erros'] +=1
                        
                    if self.x == 155:
                        if ev.key != pygame.K_j: 
                            state['erros'] +=1
                    
                        
                    if self.x == 232:
                        if ev.key != pygame.K_k:
                            state['erros'] +=1

        if self.tecla == assets['tecla dourada']:
            if self.y > 335 and self.y < 540:
                if ev.type == pygame.KEYDOWN:
                    if ev.key == pygame.K_d:
                        if self.x == 1:
                            state['pontos'] +=1
                            
                        

                    if ev.key == pygame.K_f:
                        if self.x == 80:
                            state['pontos'] +=1
                        
                    
                    if ev.key == pygame.K_j: 
                        if self.x == 155:
                            state['pontos'] +=1
                    
                        
                    
                    if ev.key == pygame.K_k:
                        if self.x == 232:
                            state['pontos'] +=1
                        
                        
                        
        if self.tecla == assets['tecla verde']:
            if self.y > 430 and self.y < 540:
                if ev.type == pygame.KEYUP:
                    if ev.key == pygame.K_d:
                        if self.x == 1:
                            state['pontos'] +=5
                            pygame.mixer.Sound.play(assets['diamante'])
                        else:
                            state['erros'] += 1
                            
                        

                    if ev.key == pygame.K_f:
                        if self.x == 80:
                            state['pontos'] +=5
                            pygame.mixer.Sound.play(assets['diamante'])
                        else:
                            state['erros'] += 1
                        
                    
                    if ev.key == pygame.K_j: 
                        if self.x == 155:
                            state['pontos'] +=5
                            pygame.mixer.Sound.play(assets['diamante'])
                        else:
                            state['erros'] += 1
                    
                        
                    
                    if ev.key == pygame.K_k:
                        if self.x == 232:
                            state['pontos'] +=5
                            pygame.mixer.Sound.play(assets['diamante'])
                        else:
                            state['erros'] += 1
                        
                        
        if self.tecla == assets['tecla comum']:
            if self.y > 430 and self.y < 540:
                    if ev.type == pygame.KEYUP:
                        if ev.key == pygame.K_d:
                            if self.x == 1:
                                state['pontos'] +=3
                                pygame.mixer.Sound.play(assets['tecla_1'])
                                self.tecla = assets['tecla dourada peq']
                            else:
                                state['erros'] += 1
                            
                        

                        if ev.key == pygame.K_f:
                            if self.x == 80:
                                state['pontos'] +=3
                                pygame.mixer.Sound.play(assets['tecla_2'])
                                self.tecla = assets['tecla dourada peq']
                            else:
                                state['erros'] += 1
                        
                    
                        if ev.key == pygame.K_j: 
                            if self.x == 155:
                                state['pontos'] +=3
                                pygame.mixer.Sound.play(assets['tecla_3'])
                                self.tecla = assets['tecla dourada peq']
                            else:
                                state['erros'] += 1
                    
                        
                    
                        if ev.key == pygame.K_k:
                            if self.x == 232:
                                state['pontos'] +=3
                                pygame.mixer.Sound.play(assets['tecla_4'])
                                self.tecla = assets['tecla dourada peq']
                            else:
                                state['erros'] += 1
            
                            
        return True


#aqui é coordenado o botão de restart
class Restart():
    '''define botões apresentados na tela'''
    #define o local do botão
    def __init__(self, imagem, pos_x, pos_y):
        self.imagem = imagem
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = self.imagem.get_rect(center = (self.pos_x, self.pos_y))
    
    #pinta o fundo da tela de restart
    def update(self, window, inicio, assets):
        if inicio:
            window.blit(assets['tela restart'], (0, 0))
            window.blit(self.imagem, self.rect)
        else:
            window.blit(self.imagem, self.rect)

    #checa clique no botão de tela e inicializa o botão
    def tela_home(self, pos, window):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            inicializa_botao(window)
            window.blit(assets['fundo'], (0, 0))
            return True
        else:
            return False

    def sair(self, pos): 
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            return True
        else:
            return False
    
    def reiniciar(self, pos, window, assets):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            inicializa_td(window)
            window.blit(assets['fundo'], (0, 0))
            return True
        else:
            return False

class Start():
    ''''define tela de start'''
    def __init__(self, imagem, pos_x, pos_y):
        self.imagem = imagem
        self.pos_x = pos_x
        self.pos_y = pos_y 
        self.rect = self.imagem.get_rect(center=(self.pos_x, self.pos_y))
    
    def update(self, window, inicio, assets):
        if inicio:
            window.blit(assets['imagem inicial'], (0, 0))
        else:
            window.blit(self.imagem, self.rect)

    def troca_tela(self, pos, window, assets):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            window.blit(assets['fundo'], (0, 0))
            pygame.display.update()
            return True
        return False

    def ajuda(self, pos, window, assets):
        if pos[0] in range(self.rect.left, self.rect.right) and pos[1] in range(self.rect.top, self.rect.bottom):
            window.blit(assets['tela ajuda'], (0,0))
            pygame.display.update()
            return True
            
        return False

class Ajuda():
    def __init__(self):
        pass

def desenha_ajuda(window, assets):
    window.blit(assets['tela ajuda'], (0,0))
    pygame.display.update()

def recebe_eventos_ajuda(state):
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            return False

        if ev.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if colisao_ponto_retangulo(pos[0], pos[1], 12, 16, 57, 55):
                state['voltou'] = True
                return False
    return True

#checa se houve colisão entre retangulo e ponto, usada para checar botões
def colisao_ponto_retangulo (ponto_x, ponto_y, rect_x, rect_y, rect_w, rect_h) :
    if (ponto_x  > rect_x and ponto_x < (rect_x + rect_w)) and (ponto_y > rect_y and ponto_y < (rect_y + rect_h)) :
        return True
    return False

def inicializa():
    '''aqui são carregadas mídias utilizadas pelo jogo'''
    pygame.init()
    window = pygame.display.set_mode((300, 530))
    pygame.display.set_caption('Fox Tiles')
    pygame.key.set_repeat(50)
    pygame.mixer.init()
    
    fonte = pygame.font.SysFont('corbel', 17, True, False)
    botao_ajuda = pygame.image.load('botao ajuda.png')
    botao_ajuda = pygame.transform.scale(botao_ajuda, (48,48))
    
    assets = {
        'tecla comum': pygame.image.load('tecla comum.png'),    
        'tecla verde': pygame.image.load('tecla verde.png'),
        'tecla preta': pygame.image.load('tecla arrastar preta.png'),
        'tecla dourada': pygame.image.load('tecla dourada.png'),
        'tecla dourada peq': pygame.image.load('dourada pequena.png'),
        'estrela': pygame.image.load('estrela.png'),   
        'imagem_botao': pygame.image.load('botao.png'),
        'imagem inicial': pygame.image.load('tela_start_redimensionada.png'),
        'fonte': fonte,
        'fundo': pygame.image.load('fundo.png'),
        'tecla_1': pygame.mixer.Sound('tecla 5.mp3'),
        'tecla_2': pygame.mixer.Sound('tecla 10.mp3'),
        'tecla_3': pygame.mixer.Sound('tecla 15.mp3'),
        'tecla_4':pygame.mixer.Sound('tecla 24.mp3'),
        'diamante': pygame.mixer.Sound('diamante.mp3'),
        'tela restart': pygame.image.load('game over.png'),
        'botao home': pygame.image.load('botao home.png'),
        'botao_quit': pygame.image.load('botao quit.png'),
        'botao restart': pygame.image.load('botao restart.png'),
        'botao ajuda': botao_ajuda,
        'tela ajuda': pygame.image.load('help1.png')
    }
    state = {
        'quit': Restart(assets['botao_quit'], 242, 460),
        'restart': Restart(assets['botao restart'], 150, 460), 
        'home': Restart(assets['botao home'], 59, 460), 
        'ajuda': Start(assets['botao ajuda'], 35, 35),
        'last_updated': 0,
        'pontos': 0,
        'erros': 0,
        'teclas':  [Tecla(1, 570, 95), # x, y, vel
                     Tecla(80, 570, 95 ), 
                     Tecla(155, 570, 95),
                     Tecla(232, 570, 95) 
                    ],
        'voltou': False

    }

    return assets, state, window


def finaliza():
    '''encerra o programa quando desejado'''
    pygame.quit()


def desenha_jogo(window, state, assets):
    '''desenha alguns itens na tela, como as estrelas e os pontos'''
    window.blit(assets['fundo'], (0, 0))
    texto_pontos = assets['fonte'].render(f'PONTOS: {state["pontos"]}', True, (100, 100, 100))
    window.blit(texto_pontos, (10, 20))
    texto_erros = assets['fonte'].render(f'ERROS RESTANTES: {3 - state["erros"]}', True, (100, 100, 100))
    window.blit(texto_erros, (120, 20))
    if state['pontos'] >= 200 and state['pontos'] < 300:
        window.blit(assets['estrela'], (129, 40))
    if state['pontos'] >= 300 and state['pontos'] < 400:
        window.blit(assets['estrela'], (70,40))
        window.blit(assets['estrela'], (186,40))
    if state['pontos'] >=400:
        window.blit(assets['estrela'], (129, 40))
        window.blit(assets['estrela'], (70,40))
        window.blit(assets['estrela'], (186,40))
    for tecla in state['teclas']:
        tecla.desenha(window)
    pygame.display.update()

def desenha_restart(window, assets):
    '''desenha a tela de restart'''
    window.blit(assets['tela restart'], (0, 0))
    pygame.display.update

#desenha os botões na tela
def desenha_start(window, assets):
    ''''desenha a tela de fim de jogo'''
    window.blit(assets['imagem inicial'], (0, 0))
    botao = Start(assets['imagem_botao'], 148, 445)
    botao.update(window, True, assets)

    state['ajuda'].update(window, False, assets)
    pygame.display.update()
    return botao

#chama a função criada na classe das teclas para cada tecla do dicionário
def atualiza_posicao_teclas(state, delta_t, assets):
    '''atualiza posição das teclas'''
    for t in state['teclas']:
        t.atualiza_estado_1(delta_t, state, assets)


#aplica a fórmula de conferir cliques para cada tecla
def recebe_eventos_jogo(state, assets):
    '''checa interações do usuário com o jogo'''
    now = pygame.time.get_ticks()
    delta_t = now - state["last_updated"]
    pygame.display.update()
  
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT: 
            return False

        for tecla in state['teclas']:
            if tecla.confere_cliques(assets, ev, state) == False:
                return False

    if state['erros'] >= 3:
                inicializa_gameover(state['pontos'])
                return False
    
    state['last_updated'] = now
    atualiza_posicao_teclas(state, delta_t, assets)
    return True


def recebe_eventos_reiniciar(state, window, assets):
    '''checa interações do usuário com a tela de reiniciar'''
    state['quit'].update(window, True, assets)
    state['restart'].update(window, True, assets)
    state['home'].update(window, True, assets)
    pygame.display.update()
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if state['quit'].sair(pygame.mouse.get_pos()):
                    return False
                if state['home'].tela_home(pygame.mouse.get_pos(), window):
                    return False
                if state['restart'].reiniciar(pygame.mouse.get_pos(), window, assets):
                    return False

def recebe_eventos_start(assets, window):
    '''checa interações do usuário com a tela de start'''

    botao = desenha_start(window, assets)
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                return False
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if botao.troca_tela(pygame.mouse.get_pos(), window, assets):
                    botao.update(window, False, assets)
                    inicializa_td(window)
                    return False
                if state['ajuda'].ajuda(pygame.mouse.get_pos(), window, assets):
                    desenha_ajuda(window,assets) 
                    while recebe_eventos_ajuda(state):
                        desenha_ajuda(window, assets)
                    if state['voltou'] == False:
                        return False
                    else:
                        desenha_start(window, assets)

            pygame.display.update()

def gameloop_jogo(window, assets, state):
    '''cria a sequência de jogo'''
    while recebe_eventos_jogo(state, assets):
        window.blit(assets['fundo'], (0, 0))
        desenha_jogo(window, state, assets)

def gameloop_reiniciar(window, assets, state):
    '''cria a sequência de jogo a partir da tela reiniciar'''
    while recebe_eventos_reiniciar(state, window, assets):
        window.blit(assets['fundo'], (0, 0))
        desenha_restart(window, state, assets)

def gameloop_start(assets, window):
    '''cria a sequência de jogo a partir da tela start'''
    while recebe_eventos_start(assets, window):
        window.blit(assets['fundo'], (0, 0))
        desenha_start(state, assets, window)


def inicializa_td(window):
    '''junta todas as funções relacionadas ao jogo'''
    assets, state, window = inicializa()
    gameloop_jogo(window, assets, state)


def inicializa_gameover(pontos):
    '''junta todas as funções relacionadas a tela fim de jogo'''
    print (f'Game Over. Sua pontuação foi {pontos}.')
    assets, state, window= inicializa()
    gameloop_reiniciar(window, assets, state)

def inicializa_botao(window):
    '''junta todas as funções relacionadas ao botão start'''
    assets, state, window = inicializa()
    gameloop_start(assets, window)

if __name__ == '__main__': 
    '''faz o jogo rodar sem problemas'''
    assets, state, window = inicializa()
    gameloop_start(assets, window)
    finaliza()

