// const numbers = [1, 2, 54, -1, 0.65, 'string', true];
// let index = 0;
// while (index < numbers.length) {
//     console.log(numbers[index]);
//     index++;
// };


// hw
// Дан массив чисел. 
// В цикле while обойдите массив и значения всех элементов с нечетным индексом умножьте на 2.
// Значения элементов с четным индексом должны остаться без изменения.
// let array1 = [1, 2, 3, 4, 5, 6, 7];
// let array2 = [];
// let i = 0;
// while (i < array1.length){
//     if (i % 2 != 0) {
//         array2.push(array1[i] * 2)
//     }
//     else {
//         array2.push(array1[i])
//     }
//     i++;
// }
// console.log(array2)


// way-2
let array3 = [1, 2, 3, 4, 5, 6, 7];
let i = 0;
while (i < array3.length) {
    if (i % 2 != 0) {
        array3[i] *= 2;
    }
    i++;
}
console.log(array3)
console.log(JSON.stringify(array3))