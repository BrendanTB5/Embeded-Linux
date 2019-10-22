#!/usr/bin/env node
// Blinks various LEDs
const Blynk = require('blynk-library');
const b = require('bonescript');
const util = require('util');

const LED0 = 'USR3';
const button = 'P9_25';
const LED1 = 'P9_14';
b.pinMode(LED0, b.OUTPUT);
b.pinMode(button, b.INPUT);
b.pinMode(LED1, b.OUTPUT);

const AUTH = 'V4Cia5WUR0rTk3rV65kZ9PO24niIIPd5';


var blynk = new Blynk.Blynk(AUTH);

var v0 = new blynk.VirtualPin(0);
var v10 = new blynk.WidgetLED(10);
var v1 = new blynk.VirtualPin(1);

v0.on('write', function(param) {
    console.log('V0:', param[0]);
    b.digitalWrite(LED0, param[0]);
});

v10.setValue(0);    // Initiallly off

b.attachInterrupt(button, toggle, b.CHANGE);

function toggle(x) {
    console.log("V10: ", x.value);
    x.value ? v10.turnOn(): v10.turnOff();
}

v1.on('write', function(param) {
    var duty_cycle = param[0]/1023;
    console.log('V1:', param[0], '  Duty Cycle: ', duty_cycle);
    b.analogWrite('P9_14', duty_cycle);
});
