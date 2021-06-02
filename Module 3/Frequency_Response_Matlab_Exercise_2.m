
%Frequency Response Matlab Exercise ECE-GY 6113

% 2. Plot the magnitude of the frequency response H f (ω) of the system using the Matlab function
% freqz:
% >> [H,om] = freqz(b,a);
% >> plot(om,abs(H));
% where b and a are appropriately defined.

clear
close all

%% (2) Difference Equation
% y(n) = 0.1x(n) − 0.12x(n − 1) + 0.1x(n − 2) + 1.7y(n − 1) − 0.8y(n − 2)

b = [0.1 -0.12 0.1]
a = [1 -1.7 0.8]
figure(1)
[H,om] = freqz(b,a);
plot(om,abs(H));
title('(2)Magnitude of frequency response')

%% (3) Input x(n) = cos(0.1πn)u(n) 
n = -10:100;
u = (n >= 0)
input_signal = cos(0.1 * pi * n) .* u
filtered_out = filter(b,a,input_signal)
figure(2)
subplot(2,1,1)
stem(n, input_signal,'filled')
title('Input Signal')
ylim([-1.5 1.5])
subplot(2,1,2)
stem(n, filtered_out,'filled')
title('Filtered Signal Output')

%% (4) H f (ω) at ω = 0.1π
  % H^f (0.1π) = B(e^j0.1π )/A(e^j0.1π )
%figure(3) 
j = sqrt(-1)
z = exp(j*0.1*pi)
f = om/(2*pi)

h1 = polyval([0.1 -0.12 0.1],z)/polyval([0.8 -1.7 1],z)
% subplot(2,1,1)
% plot(f,abs(h1))
% subplot(2,1,2)
% plot(f,angle(h1))        

%% (5)
n1 = 0:100;
u1 = (n1 >= 0);
angle(h1)
figure(3)
in_signal = cos(0.1 * pi * n1).*u1;
s = abs(h1)*cos(0.1 * pi * n1 + angle(h1));
y = filter(b,a,in_signal);
subplot(2,1,1)
stem(n1,s)
title('stem plot of steay state signal')
subplot(2,1,2)
plot(n1,y,n1,s)
legend({'Filtered signal','Steady state signal'})
xlim([0,100])

%% (6)
% x(n) = cos(0.3πn)u(n)
n2 = -10:100;
u2 = (n2 >= 0);
z2 = exp(j*0.3*pi)
input_signal2 = cos(0.3 * pi * n2) .* u2;
y2 = filter(b,a,input_signal2);
figure(4)
plot(n2,y2)
title('(6)Output for input signal x(n) = cos(0.3πn)u(n)')
% h2 = polyval([0.1 -0.12 0.1],z2)/polyval([0.8 -1.7 1],z2)
% s2 = abs(h2)*cos(0.1 * pi * n2 + angle(h2));
% plot(n2,s2)
% ylim([-0.1 0.1])
%% (7) Pole Zero plot
figure(5)
zplane(b,a)
title('Pole Zero plot of the system')
zoom on
  
