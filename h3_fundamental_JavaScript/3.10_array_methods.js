const numbers = [1, 2, 3];

// numbers.pop()            // удалить элемент:последний
// numbers.push()           //   добавить в-конец_массива
// numbers.shift()          //  удалить элемент:первый
// numbers.unshift()        // добавить несколько-элементов в-начало_массива
// numbers.includes()       // проверить наличие элемента
// numbers.indexOf(2)       // получить индекс_элемента-2  OR если нет-элемента -1
// numbers.slice(0, 2)      // получить срез       *массивНовый
// numbers.concat([6, 7, 8])   // соединить 2-массива
// console.log(
//     numbers.slice(0, 2)
//     ,numbers.concat([6, 7, 8])
// )


// hw 1
const fruits = ['apple', 'banana', 'melon', 'orange'];
const hasOrange = fruits.includes('orange')
console.log(hasOrange)


// 2
const cars = ['BMW', 'Nissan', 'VW', 'Skoda', 'Audi', 'Kia'];
const favoriteCars = cars.slice(0, 3);

// 3
const otherCars = cars.slice(3, 7) // TODO: сохраните в эту константу три последних значения из массива cars
console.log(otherCars)