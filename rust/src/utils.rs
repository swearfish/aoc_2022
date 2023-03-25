use std::fs::File;
use std::io::{BufRead, BufReader};
use std::path::Path;

pub fn read_lines(file_name: &str) -> Vec<String> {
    let file = File::open(file_name).unwrap();
    let lines = BufReader::new(file).lines();
    let result: Vec<_> = lines.collect::<Result<_, _>>().unwrap();
    return result;
}

pub fn get_res_name(day: &str, file_name: &str) -> String {
    let root = Path::new("res").join(day).join(file_name);
    return root.to_str().expect("Path shall be valid unicode string").to_string();
}
