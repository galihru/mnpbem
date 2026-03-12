use mnp_plasmon::*;

fn main() -> Result<(), String> {
    println!("=== MnpPlasmon Rust Example ===\n");

    // Get available materials
    let materials = material_list();
    println!("Available materials: {}", 
        materials.iter().map(|m| &m.name).cloned().collect::<Vec<_>>().join(", "));
    
    println!("\n=== Gold (Au) Sphere Response at 550 nm ===");
    let response = sphere_response(
        550.0,  // wavelength in nm
        25.0,   // radius in nm
        "Au",   // material
        1.0,    // medium refractive index (vacuum)
    )?;

    println!("Wavelength: {} nm", response.wavelength_nm);
    println!("Radius: {} nm", response.radius_nm);
    println!("Dielectric function: ε = {:.4} + {:.4}i", 
        response.eps_particle.re, response.eps_particle.im);
    println!("Polarizability: α = {:.4e} + {:.4e}i", 
        response.polarizability.re, response.polarizability.im);
    println!("Extinction cross-section: {:.4} nm²", response.c_ext);
    println!("Scattering cross-section: {:.4} nm²", response.c_sca);
    println!("Absorption cross-section: {:.4} nm²", response.c_abs);

    // Wavelength scan
    println!("\n=== Wavelength Scan (400-700 nm) ===");
    let responses = wavelength_scan(
        400.0,  // start wavelength
        700.0,  // end wavelength
        31,     // number of points
        25.0,   // radius
        "Au",   // material
        1.0,    // medium refractive index
    )?;

    for (i, resp) in responses.iter().enumerate().step_by(5) {
        println!("λ = {:.1} nm: σ_ext = {:.4} nm², σ_sca = {:.4} nm², σ_abs = {:.4} nm²",
            resp.wavelength_nm, resp.c_ext, resp.c_sca, resp.c_abs);
    }

    // Compare materials
    println!("\n=== Material Comparison at 550 nm (30 nm radius) ===");
    for mat in &["Au", "Ag", "Al"] {
        let resp = sphere_response(550.0, 30.0, mat, 1.0)?;
        println!("{}: σ_ext = {:.4} nm², σ_sca = {:.4} nm², σ_abs = {:.4} nm²",
            mat, resp.c_ext, resp.c_sca, resp.c_abs);
    }

    Ok(())
}
