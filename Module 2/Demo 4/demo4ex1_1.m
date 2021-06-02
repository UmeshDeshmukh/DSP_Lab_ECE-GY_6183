clear
close all

% info = audioinfo('Recorded_Audio_Clip_16b_PCM.wav');
% [x,Fs] = audioread('Recorded_Audio_Clip_16b_PCM.wav');
info = audioinfo('cat01.wav');
[x,Fs] = audioread('cat01.wav');
soundsc(x,Fs)

%% plotting speech signal time domain
t = [1:length(x)]/Fs;
figure(1)
plot(t,x)
xlabel('time in seconds')
title('Speech Signal')
%xlim([0.4 2.8])
xlim([0.2 0.6])
zoom on 

%% Fourier Transform

N_FFT = 2^ceil(log2(length(x)))
X = fft(x, N_FFT) % X is freq domain of x

f = [0:N_FFT-1]/N_FFT %normalized frequency
fn = f * Fs;

figure(2)
plot(fn,abs(X))
xlabel('Frequency in Hertz')
title('Fourier Transform')
xlim([0 Fs/2])
zoom on

%% Filter Design
f1 = 700;
f2 = 1500;

%difference equation coefficients for butterworth filter
%[b, a] = butter(2, [f1, f2]*2/Fs);
[b a] = butter(20, [f1, f2]*2/Fs); % (a)higher order BPF
%% Filter Frequency Response

[H, om] = freqz(b,a);
f_freqz = om*Fs/(2*pi);
figure(3)
plot(f_freqz, abs(H)) 
title('Frequency response of filter')
xlabel('Frequency (Hz)')

%% Pole zero plot of 
zplane(b,a)

y = filter(b,a,x);
figure(4)
plot(t,y)
xlabel('Time (sec)')
title('Filtered speech signal')
%xlim([0.4 2.8])
xlim([0.2 0.6])
zoom on

soundsc(y,Fs)








