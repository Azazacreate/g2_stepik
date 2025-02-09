const obj = {
    message: {value: 'Hello from local obj'}
}

export default function Log() {
    console.log(obj && obj.message && obj.value);
    console.log(obj?.message?.value);
}