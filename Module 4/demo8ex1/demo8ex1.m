clear
close all

%% y(n) = (1.0)* x(n) + (0.8) * x(n-800)
% Y(Z) =X(Z)+(0.8)*X(z)z^(-800)

b1 = [1 zeros(1,799)];
b2 = [0.8];
b = horzcat(b1, b2);
length(b)
a = [1];
n = -10:10000;
d = (n == 0);


y = filter(b,a,d);
figure(1)
plot(n,y);
ylim([0 1.1])
figure(2)
zplane(b,a)
