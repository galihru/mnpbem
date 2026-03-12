using System;
using System.Collections.Generic;

namespace MnpPlasmon.Demo;

class Program
{
    static void Main()
    {
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
}
