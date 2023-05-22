using System.Drawing;
using System.Text;

namespace Tools
{
    public class RandomString
    {
        private const string runes = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";

        private readonly Random _random = new Random();

        public string Generate(int length)
        {
            if (length <= 0)
                return string.Empty;

            var builder = new StringBuilder(length);

            for (int i = 0; i < length; i++) 
            {
                builder.Append(runes[_random.Next(runes.Length)]);
            }

            return builder.ToString();
        }
    }
}
