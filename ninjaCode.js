const f = (a, b) =>
    a.reduce((z, x, y) => ({
        ...z,
        [x]: b[y],
    }), {});

console.log(f(['a', 'b', 'c'], [1, 2, 3]))