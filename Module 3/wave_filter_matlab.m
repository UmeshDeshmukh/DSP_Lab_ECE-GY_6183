clear
close all

%[x, Fs] = audioread('Recorded_Audio_Clip_16b_PCM.wav')
[x, Fs] = audioread('author.wav')
soundsc(x, Fs)

N = length(x)
n = 1:N
t = n/Fs

clipped_audio = min(1, max(-1, 50*x));

figure(1)
k = [x,clipped_audio]
plot(t, clipped_audio, t, x)
%plot(t, k)
xlabel('time in seconds')
title('Speech Signal')
ylim([-2 2])
%soundsc(clipped_audio, Fs)
%soundsc(x, Fs)
zoom on

%% Filter Design
% band pass filter
[b, a] = butter(2, [500 1000]*2/Fs)

figure(2)
zplane(b, a)
title('Pole Zero diagram')
%% Frequency Response
[H, om] = freqz(b, a);
f = om*Fs/(2*pi);
plot(f,abs(H))

%% Impulse Response
Impulse_input = [1 zeros(1, 150)]
filtered_out = filter(b,a,Impulse_input)
stem(filtered_out)
%% Frequency Response continuous time
plot((0:150)/Fs,filtered_out)
%% filtered output
figure(3)
filtered_sound = filter(b,a,clipped_audio)
plot(t,filtered_sound, t, x)
soundsc(filtered_sound, Fs)