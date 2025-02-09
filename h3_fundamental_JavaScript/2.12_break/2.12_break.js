/*
while (true) {
    let name = prompt('what is your name?');
    let age = +prompt('how old are you?');
    if (age >= 18) {
        alert('Welcome !')
        break;
    }
    alert('Вы младше 18-лет. покиньте сайт.')
}
console.log(name, age)
*/


let tries = 0;
while (tries < 3) {
    let age2 = +prompt('you age is = ?')
    if (age2 >= 18) {
        alert('Welcome !')
        break;
    }
    tries++;
    alert('уходи. тебе нет-18 !')
}