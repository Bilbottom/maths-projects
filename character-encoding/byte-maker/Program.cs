using System;
using System.IO;

namespace byte_maker
{
    class Program
    {
        static void Main(string[] args)
        {
            byte[] bytes = new byte[128];
            for (byte i = 0; i < 128; i++)
                bytes[i] = i;
            
            File.WriteAllBytes("128bytes.txt", bytes);
        }
    }
}

// PS:  Format-Text 128bytes.txt