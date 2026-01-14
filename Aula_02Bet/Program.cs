class Program
{
    public static void Main(string[] args)
    {
        Console.Clear();

        //System.Console.WriteLine("hello word");
        bool Controle1 = true;
        double Saldo = 0;
        int MainMenuOpt;



        while (Controle1)
        {
            System.Console.WriteLine("1 - Menu saldo");
            System.Console.WriteLine("2 - Jogar aposta de cartas");
            System.Console.WriteLine("0 - Sair");

            MainMenuOpt = int.Parse(Console.ReadLine()!);

            //System.Console.WriteLine($" sua opção foi {MainMenuOpt}");

            if (MainMenuOpt == 0)
            {
                Controle1 = false;
            }
            else
            {
                switch (MainMenuOpt)
                {
                    case 1://menu de modificação de saldo
                        //System.Console.WriteLine("teste");
                        Saldo = Aula_02Bet.Saldo.Teste(Saldo); //saldo1 recebe valor de saldo2 apos passar pelo menu saldo
                        System.Console.WriteLine("Vamos jogar?");

                        break;

                    case 2:
                        //Jogar
                        Saldo = Aula_02Bet.JogoBaralho.Cardgame(Saldo);
                        
                        break;
                }
            }

        }
        Console.Clear();

        System.Console.WriteLine($"o saldo Final foi de {Saldo}");

    }
}