{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62b93235-879b-4fc8-84ef-90c4b627fbb1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Bem-vindo ao cálculo de fator de correção para contagem de parasitemia em sangue periférico\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Digite o valor do diametro da objetiva:  0.49\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Insira a seguir os valores da sua laminula (em milímetros):\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Comprimento: 22\n",
      "Largura: 22\n",
      "Objetiva: 40\n",
      "Campos a serem contados: 25\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fator de correcao = 20533.042553996464\n",
      "Deseja fazer mais alguma operação? S/N\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "\n",
    "print ('Bem-vindo ao cálculo de fator de correção para contagem de parasitemia em sangue periférico')\n",
    "\n",
    "while True:\n",
    "                \n",
    "    diametro = 0\n",
    "    diametro = float (input('Digite o valor do diametro da objetiva: '))\n",
    "    area_lamina = math.pi * ((diametro/2)**2)\n",
    "\n",
    "    laminula = 0\n",
    "    print ('Insira a seguir os valores da sua laminula (em milímetros):')\n",
    "    laminula_ladoA = float (input ('Comprimento:')) \n",
    "    laminula_ladoB =float (input ('Largura:'))\n",
    "    laminula = laminula_ladoA * laminula_ladoB\n",
    "\n",
    "    objetiva = 0\n",
    "    objetiva = float (input('Objetiva:'))\n",
    "    campos_totais = laminula / area_lamina\n",
    "\n",
    "    campos_contados = 0\n",
    "    campos_contados = float (input('Campos a serem contados:'))\n",
    "    contagem_5ul = campos_totais / campos_contados\n",
    "\n",
    "    contagem_1000ul = contagem_5ul * 200\n",
    "    print ('Fator de correcao = {}'.format(contagem_1000ul))\n",
    "\n",
    "    print ('Deseja fazer mais alguma operação? S/N')\n",
    "\n",
    "    yes = {'sim', 'S', 's', ''}\n",
    "    no = {'nao', 'não', 'Não', 'Nao', 'N' , 'n', 'sair', 'exit'}\n",
    "\n",
    "    choice = input().lower()\n",
    "    if choice in yes:\n",
    "        continue\n",
    "    elif choice in no:\n",
    "            print ('Até a próxima')\n",
    "            break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "054373aa-6fcd-47e1-b021-340f87e7fba6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
