#!/usr/bin/env node
// Mark Procter
// ECE434
// Homework 7

const Blynk = require('blynk-library');
const b = require('bonescript');
const util = requrie('util');

const LED0 = 'USR3';
const LED1 = 'P9_14';
const button = 'P9_25';

b.pinMode(LED0, b.OUTPUT);
b.pinMode(LED1, b.OUTPUT)
b.pinMode(button, b.INPUT);

const AUTH = 'i3jBxz8982PuOvQPq9Es5rNBa__7OGXA';


var blynk = new Blynk.Blynk(AUTH);

var v0 = new blynk.VirtualPin(0);
var v10 = new blynk.WidgetLED(10);

v0.on('write', function(param) {
    console.log('V0:', param[0]);
    b.digitalWrite(LED0, param[0]);
});

v10.setValue(0);    // Initiallly off

b.attachInterrupt(button, toggle, b.CHANGE);

function toggle(x) {
    console.log("V10: ", x.value);
    x.value ? v10.turnOff() : v10.turnOn();