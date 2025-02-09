// объект = набор-пар ключ-значение
const developer = {
    name: 'Michail',
    surname: 'Petrov',
    age: 30,
    skiils: ['Javascript', 'Typescript', 'CSS', 'HTML'],
    is__married: false
};
console.log(developer.is__married);

developer.is__married = true;           // как добавить / изменить?
console.log(developer.is__married);

delete developer.is__married            // как удалить? (*не-используйте его)
console.log(developer.is__married);


// 3.2.2 2-способа как-получить значение из-объекта?
console.log(developer.skiils);
console.log(developer['skiils']);


// hw. Создание и изменение объекта. Создайте объект dog. Назначьте ему свойства со следующими ключами: name, age, color, weight. После создания объекта на отдельной строчке добавьте объекту дополнительное свойство с ключом breed.
const dog = {
    name: 'dog1',
    age: '31',
    color: 'gray',
    weight: 13,
}
dog.breed = false
console.log(dog)