const numberSecret = 5;
let tries = 0;
function guess__number(number) {
    if (tries >= 5) {return alert('game over! you died lol.')}
    if (number == 5) {
        alert('угадал! да это число = ' + number);
    }
    else {
        alert('не угадал');
    };
    tries++;
};