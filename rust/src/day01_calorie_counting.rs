use crate::utils;

pub fn find_max_calories(file_name: &str) -> i32 {
    let input = read_input_file(file_name);
    let max = input.iter().max();
    let result = *max.expect("Can't handle empty input");
    return result
}

fn find_top_3_calories(file_name: &str) -> i32 {
    let mut input = read_input_file(file_name);
    input.sort();
    input.reverse();
    input.truncate(3);
    let result = input.iter().sum();
    return result;
}

#[cfg(test)]
mod tests {
    use std::path::{Path, PathBuf};
    use crate::day01_calorie_counting::{find_max_calories, find_top_3_calories};
    use crate::utils::get_res_name;

    static RES_ROOT: &str = "day01_calorie_counting";
    static EXAMPLE_IN: &str = "example.in";
    static INPUT_IN: &str = "input.in";

    #[test]
    fn test_example_max_calories() {
        let res = get_res_name(RES_ROOT, EXAMPLE_IN);
        assert_eq!(24000, find_max_calories(&res));
    }

    #[test]
    fn test_example_top_3_calories() {
        let res = get_res_name(RES_ROOT, EXAMPLE_IN);
        assert_eq!(45000, find_top_3_calories(&res));
    }

    #[test]
    fn test_input_max_calories() {
        let res = get_res_name(RES_ROOT, INPUT_IN);
        assert_eq!(70374, find_max_calories(&res));
    }

    #[test]
    fn test_input_top_3_calories() {
        let res = get_res_name(RES_ROOT, INPUT_IN);
        assert_eq!(204610, find_top_3_calories(&res));
    }
}

fn read_input(lines: Vec<String>) -> Vec<i32> {
    let mut total_calories: i32 = 0;
    let mut calories_by_elf: Vec<i32> = Vec::new();
    for line in lines.iter() {
        if line.len() == 0 {
            calories_by_elf.push(total_calories);
            total_calories = 0;
        } else {
            let calories = line.parse::<i32>().unwrap();
            total_calories += calories;
        }
    }
    if 0 != total_calories {
        calories_by_elf.push(total_calories)
    }
    return calories_by_elf;
}

fn read_input_file(file_name: &str) -> Vec<i32> {
    let lines = utils::read_lines(file_name);
    let result = read_input(lines);
    return result;
}
