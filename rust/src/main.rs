// This is the first Rust code I've ever written, cut me some slack
use std::collections::HashMap;

#[derive(Hash, Eq, PartialEq, Debug)]
struct Pos {
    n: u64,
    m: u64
}

// o(2^n) or something silly
fn grid_traveler_naive(n: u64, m: u64) -> u64 {
    if n <= 1 || m <= 1 {
        return 1;
    }
    return grid_traveler_naive(n - 1, m) + grid_traveler_naive(n, m - 1);
}

// Hopefully a bit faster o(n) I think?
fn grid_traveler_memo(n: u64, m: u64, memo: &mut HashMap<Pos, u64>) -> u64 {
    if n <= 1 || m <= 1 {
        return 1;
    }

    let t = Pos { n, m };
    if memo.contains_key(&t) {
        return *memo.get(&t).unwrap();
    }

    let v = grid_traveler_memo(n - 1, m, memo) + grid_traveler_memo(n, m - 1, memo);
    memo.insert(t, v);

    return v;
}

fn main() {
    println!("{}", grid_traveler_naive(10, 10));

    let mut memo = HashMap::new();
    println!("{}", grid_traveler_memo(10, 10, &mut memo));
}
