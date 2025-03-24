function sum(a, b) {
    if (typeof a != 'number' || typeof b != 'number') {
        throw new Error('isn\'t number')
    }
    return a + b;
}
console.log(sum(1, 2));
console.log(sum(1, 'h'));   // error


try {
    sum();
} 
catch(err) {
    console.error(err.message)
}

console.log('КОНЕЦ-2');