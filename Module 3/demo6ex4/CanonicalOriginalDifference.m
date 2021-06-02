clear 
close all

[x Fs] = audioread('output_matlab.wav');
[x2 Fs2] = audioread('demo6ex4_canonical.wav');


y = x-x2;
max(abs(x-x2))