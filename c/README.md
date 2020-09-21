2º Exercício Prático - Fundamentos de Sistemas Embarcados 2020.2 - UnB - Gama
=========================
André Lucas de Sousa Pinto - 17/0068251

## Como rodar a Solução C

1. Faça o clone deste projeto com ```$ git clone https://github.com/andrelucax/2020-2-FSE-E2.git```
2. Entre na pasta da solução em C do projeto com ```$ cd 2020-2-FSE-E2/c/```
3. Compile o projeto com ```$ make```
4. Rode o programa com ```$ ./bin/bin /dev/i2c-1``` (/dev/i2c-1 é o dispositivo i2c na Raspberry)
5. As informações de temperatura, pressão e umidade irão ser mostradas no terminal a cada segundo e armazenada a média das mesmas em um arquivo CSV a cada 10 segundos. O arquivo de log CSV ficará na pasta inicial do projeto com o nome "dados.csv"
