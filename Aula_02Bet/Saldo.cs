using System;
using System.Collections.Generic;
using System.Dynamic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Threading.Tasks;

namespace Aula_02Bet
{
    public class Saldo
    {
        public static double Soma(double num1, double num2) //soma os depositos
        {
            double resultado = num1 + num2;
            return resultado;
        }

        public static double Saque(double num1, double num2) //duminui os depositos
        {
            double resultado = num1 - num2;
            return resultado;
        }
        public static double Teste(double num1)
        {

            double Saldo = num1, deposito, ValorSaque;
            bool Controle2 = true;
            int MainMenuOpt;

            System.Console.WriteLine("1 - Depositar saldo");
            System.Console.WriteLine("2 - Sacar saldo");
            System.Console.WriteLine("3 - Consultar saldo");
            System.Console.WriteLine("0 - Sair");
            while (Controle2) //faz o controle e manter o usuario aqui até que leve o controle a false
            {
                MainMenuOpt = int.Parse(Console.ReadLine()!);

                //System.Console.WriteLine($" sua opção foi {MainMenuOpt}");

                if (MainMenuOpt == 0)//escolheu 0 escolheu sair deste menu
                {
                    Controle2 = false;
                }
                else
                {
                    switch (MainMenuOpt)
                    {
                        case 1:
                            //Depositar
                            while (Controle2)
                            {
                                System.Console.WriteLine($"\nseu Saldo atual é de {Saldo}");
                                System.Console.WriteLine("Quanto deseja colocar?");
                                System.Console.WriteLine("Digite 0 para cancelar o deposito");
                                deposito = double.Parse(Console.ReadLine()!);
                                if (deposito > 100)// não vai jogar mais do que 100
                                {
                                    System.Console.WriteLine("Não se pode depositar mais que 100R$ por vez");
                                    Controle2 = false;//apos depositar a mais o comando quebra e sai do menu
                                }
                                else if (deposito == 0)
                                {
                                    Controle2 = false;
                                }
                                else
                                {
                                    Saldo = Soma(Saldo, deposito);
                                }//resultado final depois de um deposito
                                if (Saldo >= 1000) { Controle2 = false; }//serando o controle sai deste menu
                            }
                            System.Console.WriteLine("o deposito chegou ao fim");

                            break;

                        case 2:
                            //Sacar

                            System.Console.WriteLine($"Seu saldo atual é de {Saldo}");
                            System.Console.WriteLine("Quanto você quer sacar");
                            ValorSaque = double.Parse(Console.ReadLine()!);
                            if (ValorSaque > Saldo || ValorSaque <= 0)
                            {
                                System.Console.WriteLine($"Você tem {Saldo}, na conta, e não é possivel sacar {ValorSaque} \njogue mais, quem sabe você não ganha o valor que falta");
                            }
                            else
                            {
                                System.Console.WriteLine($"você sacou:{ValorSaque}R$\n");
                                Saldo = Saque(Saldo, ValorSaque);

                                System.Console.WriteLine($"Saldo atual é de {Saldo}");
                            }

                            Controle2 = false;
                            break;
                        case 3:
                            System.Console.WriteLine($"seu Saldo atualmente consultado é de: {Saldo}");
                            Controle2 = false;
                            break;
                    }
                }

            }
            return Saldo;
        }



    }

}
