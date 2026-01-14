using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Threading.Tasks;

namespace Aula_02Bet
{
    public static partial class Baralho
    {
        
        public static string Naipe() //vai sortear o naipe a depender do numero que cair no "identificador"
        {
            int Identificador = Random.Shared.Next(1, 4);
            string resultado = "inicio";
            if (Identificador == 4)
            {
                resultado = "♥";
            }
            else if (Identificador == 1)
            {
                resultado = "♣";
            }
            else if (Identificador == 2)
            {
                resultado = "♦";
            }
            else if (Identificador == 3)
            {
                resultado = "♠";
            }
            return resultado;
        }

        public static string Letra() //sortear se vai ser numero ou letra, proporcionalmente*
        {

            string Identificador = "inicio";
            int carta = Random.Shared.Next(1, 13);

            if(carta == 1)
            {
                Identificador = "A";
            }

            if(carta >= 2 && carta <=10)
            {
                Identificador = carta.ToString();
            }

            if(carta == 11)
            {
                Identificador = "j";
            }

            if(carta == 12)
            {
                Identificador = "Q";
            }

            if(carta == 13)
            {
                Identificador = "K";
            }
            return Identificador;
        }

        public static string CartaBaralho()
        {
            string CartaFinal, letra, naipe;

            letra = Letra();
            naipe = Naipe();
            CartaFinal = "["+letra+naipe+"]";

            return CartaFinal;

        }
    }
}