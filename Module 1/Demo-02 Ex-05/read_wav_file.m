[x, Fs] = audioread('sine_8bit.wav');
whos x
Fs
%%soundsc(x, 0.01*Fs)
clf
N = length(x);
t = (1:N)/Fs;

figure(1)
plot(t,x)
xlabel('Time in seconds')

title('Signal')
xlim(0 +[0 0.015])
xs = sort(x);
%plot(xs)

SPV = min(x(x>0));
SPV_inverse = 1/SPV;
max_val = 2^7;

%%FFT
N = length(x);
fft_len = 2^ceil(2+log2(N));
FTransform = fft(x,fft_len);
k = 0:fft_len-1;
%+plot(k,abs(FTransform))
shifted_FFT = fftshift(FTransform);
k2 = -fft_len/2:fft_len/2-1;
plot(k2,abs(shifted_FFT))

%normalized_freq = (-fft_len/2:fft_len/2-1)/fft_len;
%%plot(normalized_freq,abs(FTransform))

