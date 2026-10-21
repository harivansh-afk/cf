use std::collections::HashMap;
use std::io::{self,Read};

fn triple(arr: &[usize]) {
    let mut hm = HashMap::new();

    for &x in arr {
        *hm.entry(x).or_insert(0) += 1;
    }

    for(&key, &count) in &hm {
        if count >= 3 {
            println!("{}", key)
            return;
        }
    }

    print("-1");
}


fn main() {

}
