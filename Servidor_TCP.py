# -*- coding: utf-8 -*-
'''
Exemplo de um Servidor TCP

Artigo: https://www.linkedin.com/pulse/python-sockets-criando-aplicações-cliente-e-servidor-diego/

Diego Mendes Rodrigues
'''

import socket

HOST = '127.0.0.1'      # Endereco IP do Servidor
PORT = 5000             # Porta que o Servidor está

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
origem = (HOST, PORT)

# Colocando um endereço IP e uma porta no Socket
tcp.bind(origem)

# Colocando o Socket em modo passivo
tcp.listen(1)

print('\nServidor TCP iniciado no IP', HOST, 'na porta', PORT)

while True:
    # Aceitando uma nova conexão
    conexao, cliente = tcp.accept()
    print('\nConexão realizada por:', cliente)

    while True:
        # Recebendo as mensagens através da conexão
        mensagem = conexao.recv(1024)
        if not mensagem:
            break

        # Exibindo a mensagem recebida
        print('\nCliente..:', cliente)
        print('Mensagem.:', mensagem.decode())

    print('Finalizando conexão do cliente', cliente)

    # Fechando a conexão com o Socket
    conexao.close()