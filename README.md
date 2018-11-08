# Chat-P2P-SSL
2018.2 UFF Niteroi
Projeto desenvolvido por Leandro Schwab e Andre Felipe Tavares para aula de Seguranca da informação



**Sobre:** 
  Este programa foi desenvolvido com python 2.7, foi utilizado a biblioteca pycryptodome. 


**Objetivos:** 
  Desenvolver um Chat com encriptação que utilize chaves Assimétricas e chaves simétricas funcionando da seguinte forma. Ao iniciar o programa é gerado uma chave Publica e Privada. A Chave publica é disponibilizada aos outros membros da rede. 

Ao iniciar a conversa é criada uma chave simétrica, essa chave simétrica é então encriptada utilizando a chave publica do outro participante que por sua vez utiliza a sua privada para decrepitar a chave simétrica e assim iniciar a conversa utiliando a chave simétrica. Toda vez que a janela de chat for aberta é gerado uma nova chave simétrica. 

 

