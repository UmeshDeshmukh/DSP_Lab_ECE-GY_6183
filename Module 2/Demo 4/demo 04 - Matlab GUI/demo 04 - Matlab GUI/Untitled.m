clear
close all

%%
n = -10:10;
f = (n == 0);
stem(n,f)
% Use stem to plot the discrete-time step function:
f = (n >= 0);
stem(n,f)

figure(1)

%% title('(1) f(n)= u(n)-u(n-4)')

subplot(5,1,1)
n = -5:10;
a = (n >= 0);
%stem(n,a)
%n = -10:10;
b = (n >= 4);
stem(n,a-b)
title('(1) f(n)= u(n)-u(n-4)')
%% title('(2) g(n)= r(n)-2r(n-5)+r(n-10)')
subplot(5,1,2)
n = -5:15;
a = (n >= 0).*n;
%stem(n,a)
%n = -10:10;
b = (n >= 5).*n.*2
%stem(n,a-b)
c = (n >= 10).*n
stem(n,a-b+c)
title('(2) g(n)= r(n)-2r(n-5)+r(n-10)')
%% title('(3) x(n)= d(n)-2d(n-4)')
subplot(5,1,3)
n = -5:15
a = (n == 0)
b = (n== 4).*2
stem(n,a-b)
title('(3) x(n)= d(n)-2d(n-4)')
%% title('(4) y(n)= (0.9)^n*(u(n)-u(n-20))')
subplot(5,1,4)
n = -5:25
a = (n >= 0)
b = (n >= 20)
c = (0.9).^n 
stem(n,c.*(a-b))
title('(4) y(n)= (0.9)^n*(u(n)-u(n-20))')
%% title('(5) v(n)= cos(0.12*pi*n)*u(n)')
subplot(5,1,5)
n = -5:25
a = cos(0.12*pi.*n)
b = (n >= 0) 
stem(n, a.*b)
title('(5) v(n)= cos(0.12*pi*n)*u(n)')
