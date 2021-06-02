clear
close all

n = -10:100;
d = (n == 0);
Fs = 16000;
f1 = 3000;
f2 = 5000;
f_bpf = [f1, f2];
[b, a] = butter(20,(f_bpf)*2/Fs,'bandpass')
freqz(b,a)
ylim([100 -600])
b
a
