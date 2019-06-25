# Projeto Sistemas Embarcados
<p align="center"> 
  
![imagem_geral_estufa](https://user-images.githubusercontent.com/47900225/59558333-660dfc80-8fc6-11e9-849c-942839e9385e.jpeg)

</p>

<h3 align="center">Sistema de monitoramento de Estufa</h3>

Vídeo demonstrativo: https://youtu.be/ig8Omhb2YGI

## Sumário

- [Arquitetura do projeto](#arquitetura-do-projeto)
- [Software](#software)
- [Estrutura](#estrutura)
- [Hardwares utilizados](#hardwares-utilizados)
- [Bibliotecas utilizadas](#bibliotecas-utilizadas)
- [Integrantes do grupo](#integrantes-do-grupo)

## Arquitetura do projeto

O projeto foi desenvolvido sobre duas malhas fechadas de controle: a primeira relativa ao controle da temperatura interna da estufa e
a segunda, ao controle da umidade interna da estufa.

Para a primeira malha de controle (cooler), o valor de temperatura lido pelo sensor é comparado com o valor da temperatura de referência.Desse delta
de temperatura (DT) surgem as 3 condições que regem o funcionamento do cooler e da porta lateral. São elas

1 - Se DT >= 2 :cooler é acionado na velocidade máxima e servo acionado para levar a porta lateral à posição aberta

2 - Se DT < 2 e DT > 0,1 : cooler é acionado na velocidade máxima e a porta lateral mantida fechada

3 - Se DT <= 0,1 : cooler se mantém na velocidade mínima e a porta lateral mantida fechada

Para a segunda malha de controle (bomba d'água), o valor de umidade lido pelo sensor é colocado direto nas condições de controle dessa parte
do sistema. Tais condições são

1 - Se valor da umidade lido pelo sensor < 58 : bomba d'água é acionada

2 - Se valor da umidade lido pelo sensor > 58 : bomba d'água é desligada

Ambas as leituras do ambiente foram feitas pelo mesmo sensor.

Como sistema de operação central foi usada a placa BeagleBone Black a qual recebia do PC (via usb) tanto o código que deveria ser executado
quanto a alimentação para funcionamento da placa.

![circuito_geral](https://user-images.githubusercontent.com/47900225/59558378-2bf12a80-8fc7-11e9-93db-ea19e8a30da4.jpg)

A figura acima demonstra toda a ligação do circuito da estufa. Nessa imagem, faltou apenas a bomba d'água por limitação do software de desenho.
A ligação da bomba ocorre direto no relé que consta na figura acima.



## Software


Para trabalhar com a BeagleBone Black foi utilizado um cartão SD de 16 GB no qual foi escrito a imagem do firmware Debian 9.5 2018-10-07 4GB SD IoT.
Os passos para preparo da placa e seu uso são simples de se desenvolver e podem ser seguidos no tutorial que há no site do fornecedor.

Link para tutorial:

<http://beagleboard.org/getting-started#update>

## Estrutura

Os materiais utilizados para confecção da estufa foram: mdf para a estrutura, papel contact para cobrir a área central que recebe a planta,
plástico transparente para cobrir toda a área externa da estufa para, assim, criar um abiente controlável para temperatura/umidade e PLA
para a peça impressa em 3d (caíxa d'água - 80x80x80 mm com 3 mm de expessura).

Os CADs da estrutura principal estão listados abaixo e também uma vista geral desta.

- [Base.PDF](https://github.com/angelicabatassim/estufa/files/3293774/Base.PDF)
- [Tabua_comprida.PDF](https://github.com/angelicabatassim/estufa/files/3293775/Tabua_comprida.PDF)
- [Tabua_curta.PDF](https://github.com/angelicabatassim/estufa/files/3293776/Tabua_curta.PDF)

![vista_solid_works](https://user-images.githubusercontent.com/47900225/59558384-6a86e500-8fc7-11e9-908f-2119e0f0608c.jpeg)



## Hardwares utilizados

- Cooler 12v DC - datasheet: <https://www.sanyodenki.com/archive/document/product/cooling/catalog_E_pdf/San_Ace_E.pdf>

- Servo MG995 - datasheet: <https://www.electronicoscaldas.com/datasheet/MG995_Tower-Pro.pdf>

- BeagleBone Black - datasheet: <https://github.com/beagleboard/beaglebone-black/wiki>

- Driver L298n - datasheet: <https://www.alldatasheet.com/datasheet-pdf/pdf/22440/STMICROELECTRONICS/L298N.html>

- Fonte variável para alimentação do cooler

- PC

- Leds para verificação do funcionamento do cooler e da bomba d'água

- Sensor de temperatura e umidade - datasheet: <https://www.mouser.com/ds/2/758/DHT11-Technical-Data-Sheet-Translated-Version-1143054.pdf>

- Bomba d'água - datasheet: <https://www.blumaro.com.br/bomba-para-aquario/bomba-submersa-mini-c--p?gclid=Cj0KCQjwrpLoBRD_ARIsAJd0BIWRmQDsLXBza2fSZp8LtOZD8WXeT0q_NzzEfeartaD4zWnbQXlH7ToaAmHJEALw_wcB>

- Jumpers para conexões

- Protoboard

- Lâmpada incandescente 25W

- Cartão SD 16GB Sandisk

- 2 resistores 220 ohms

- 1 resistor 2k ohms

- 1 led vermelho

- 1 led verde

## Bibliotecas extras utilizadas

- Adafruit DHT Humidity & Temperature Sensor Library

<https://github.com/adafruit/DHT-sensor-library>

## Integrantes do grupo

1 - André Pereira Cavalcante

2 - Angélica Batassim Nunes

3 - Christian Michel Filgueiras Lacerda

4 - Davi Lotfi Lavor Navarro

5 - Thaís Mafra Navarro
