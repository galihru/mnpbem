using System;
using System.Collections.Generic;
using System.Globalization;
using System.IO;

namespace MnpPlasmon.Demo;

class Program
{
    static void Main(string[] args)
    {
        if (args.Length == 2 && args[0] == "--csv-out")
        {
            WriteCsv(args[1]);
            return;
        }

        Console.WriteLine("=== MNP Plasmon C# Demo ===\n");

        // List available materials
        var materials = MnpPlasmon.MaterialList();
        Console.WriteLine("Available materials:");
        foreach (var mat in materials)
        {
            Console.WriteLine($"  - {mat.Name}");
        }
        Console.WriteLine();

        // Simulate Au nanoparticle response at different wavelengths
        double[] wavelengths = { 400.0, 500.0, 550.0, 600.0, 700.0 };

        Console.WriteLine("Au nanoparticle (r=20nm) in water (n=1.33):");
        Console.WriteLine("{0,-15} {1,-15} {2,-15} {3,-15}",
            "Wavelength(nm)", "C_ext(nm²)", "C_sca(nm²)", "C_abs(nm²)");
        Console.WriteLine(new string('-', 60));

        foreach (double wl in wavelengths)
        {
            var response = MnpPlasmon.SimulateSphereResponse("Au", wl, 20.0, 1.33);
            Console.WriteLine("{0,-15:F1} {1,-15:E4} {2,-15:E4} {3,-15:E4}",
                wl, response.CExt, response.CSca, response.CAbs);
        }

        Console.WriteLine();

        // Detailed response at resonance
        var detailedResponse = MnpPlasmon.SimulateSphereResponse("Au", 550.0, 20.0, 1.33);
        MnpPlasmon.PrintResponse(detailedResponse);
    }

    static void WriteCsv(string outputPath)
    {
        Directory.CreateDirectory(Path.GetDirectoryName(outputPath) ?? ".");
        using var writer = new StreamWriter(outputPath);
        writer.WriteLine("wavelength_nm,c_ext,c_sca,c_abs");

        for (int wl = 400; wl <= 700; wl += 5)
        {
            var response = MnpPlasmon.SimulateSphereResponse("Au", wl, 25.0, 1.33);
            writer.WriteLine(string.Join(",",
                wl.ToString(CultureInfo.InvariantCulture),
                response.CExt.ToString("G17", CultureInfo.InvariantCulture),
                response.CSca.ToString("G17", CultureInfo.InvariantCulture),
                response.CAbs.ToString("G17", CultureInfo.InvariantCulture)));
        }
    }
}
