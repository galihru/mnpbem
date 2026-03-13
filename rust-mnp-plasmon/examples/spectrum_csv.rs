use std::fs::{self, File};
use std::io::Write;

fn main() {
    let mut output = String::from("wavelength_nm,c_ext,c_sca,c_abs\n");

    for wavelength in (400..=700).step_by(5) {
        let response = mnp_plasmon::sphere_response(wavelength as f64, 25.0, "Au", 1.33)
            .expect("sphere response should compute");
        output.push_str(&format!(
            "{},{},{},{}\n",
            wavelength,
            response.c_ext,
            response.c_sca,
            response.c_abs
        ));
    }

    fs::create_dir_all("docs/example-data").expect("create docs/example-data");
    let mut file = File::create("docs/example-data/rust.csv").expect("create rust.csv");
    file.write_all(output.as_bytes()).expect("write csv");
}
