using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Threading.Tasks;

namespace Aula_02Bet
{
    public class JogoBaralho
    {
        public static int Aposta(int Opt, string N1, string N2, string L1, string L2)
        {
            //quero comparar o numero e o naipe
            int letra1 = int.Parse(L1);
            int letra2 = int.Parse(L2);
            int Aposta = Opt, resultado = 0;
            string naipe1 = N1, naipe2 = N2;

            switch (Aposta)
            {
                case 1:
                    if (naipe1 == naipe2)
                    {
                        resultado = 1;
                    }
                    else
                    {
                        resultado = 0;
                    }
                    break;
                case 2:
                    if (naipe1 != naipe2)
                    {
                        resultado = 1;
                    }
                    else
                    {
                        resultado = 0;
                    }
                    break;
                case 3:
                    if (letra1 != letra2)
                    {
                        resultado = 1;
                    }
                    else
                    {
                        resultado = 0;
                    }
                    break;
                case 4:

                    if (letra1 == letra2)
                    {
                        resultado = 1;
                    }
                    else
                    {
                        resultado = 0;
                    }
                    break;

            }



            return resultado;
        }
        public static double Cardgame(double num1)
        {
            bool Controle3 = true;
            double Saldo = num1, Valor = 0;
            int BarOpt, Result;
            string Pausa, letra1, letra2, naipe1, naipe2, carta1, carta2;


            System.Console.WriteLine("=====INSTRUÕES IMPORTANTES=====");
            System.Console.WriteLine("O jogo e até bem simples\nvocê deve analisar as opções de troca de numero \nJuntamente, se ela irá trocar de naipe ou não");
            System.Console.WriteLine("vamos começar a jogar?");
            System.Console.WriteLine("Aperte enter para começar");

            Pausa = Console.ReadLine()!;
            System.Console.WriteLine(Pausa);

            while (Controle3)
            {
                System.Console.WriteLine("as cartas estão sendo preparadas...");
                System.Console.WriteLine("Eai, quanto você irá apostar agora?");
                System.Console.WriteLine($"Lembrando que você ainda tem {Saldo}");
                Valor = double.Parse(Console.ReadLine()!);

                if (Valor > 0 && Valor <= Saldo)
                {
                    Saldo = Aula_02Bet.Saldo.Saque(Saldo, Valor);
                    System.Console.WriteLine("Embaralhando...");

                    naipe1 = Baralho.Naipe();
                    naipe2 = Baralho.Naipe();
                    letra1 = Baralho.Letra();
                    letra2 = Baralho.Letra();


                    System.Console.WriteLine("Aperte entre para ver a primeira carta");


                    Pausa = Console.ReadLine()!;
                    System.Console.WriteLine(Pausa);

                    carta1 = "[" + letra1 + naipe1 + "]";
                    System.Console.WriteLine($"E a primeira carta é...{carta1}");


                    System.Console.WriteLine("Agora que já conhece a primeira carta vamos ao jogo... \n ");
                    System.Console.WriteLine("O que você escolhe?\n ");
                    System.Console.WriteLine("1- Naipes iguais\n ");
                    System.Console.WriteLine("2- Naipes diferentes\n ");
                    System.Console.WriteLine("3- Numeros diferentes\n ");
                    System.Console.WriteLine("4- Numeros iguais [3x]\n ");
                    BarOpt = int.Parse(Console.ReadLine()!);

                    Result = Aposta(BarOpt, naipe1, naipe2, letra1, letra2);


                    System.Console.WriteLine("Aperte entre para ver a proxima carta");

                    Pausa = Console.ReadLine()!;
                    System.Console.WriteLine(Pausa);

                    carta2 = "[" + letra2 + naipe2 + "]";
                    System.Console.WriteLine($"E a carta gerada é...{carta2}");

                    if (Result == 0)
                    {
                        System.Console.WriteLine("Uma pena mesmo, quem sabe na proxima você não consegue...");

                    }
                    else if (Result == 1 && BarOpt == 4)
                    {
                        System.Console.WriteLine("=========PARABENS, VOCÊ ACERTOU NUMEROS IGUAIS=========");
                        Saldo += (Valor * 4);

                    }
                    else if (Result == 1)
                    {
                        System.Console.WriteLine("Olha só, se não é alguem muito sortudo por aqui não, é mesmo?\nOu será que foi pura analise tecnica?");
                        Saldo += (Valor * 2);
                    }
                    System.Console.WriteLine($"O saldo final após está rodada é de:{Saldo}");
                    System.Console.WriteLine("Aperte enter para fechar essa aposta");
                    Pausa = Console.ReadLine()!;
                    System.Console.WriteLine(Pausa);


                    Controle3 = false;
                }
                else
                {
                    System.Console.WriteLine("error");
                    Controle3 = false;
                }
            }

            return Saldo;
        }
    }
}