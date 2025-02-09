// 2.9 массивы как хранилища данных
//     массив = набор-данных
    const array = [1, 2, 3, 4, 5];
    console.log(array[0]);
    console.log(array.length);
    console.log(array[array.length - 1]);
    
    // способ-1. как добавить в-массив ?
    const array2 = [1, 2];
    array2[2] = '3';
    console.log(array2);
    
    // способ-2. как добавить в-массив ?
    array3 = ['string1', 'string2']
    array3.push('string3')
    console.log(array3);
    
    // как удалить из-массива элемент:последний?
    console.log(array3.pop());
    console.log(array3);