

function filter_GUI_example
clear 
close all

N = 500
n = 1:N
x = sin(2*5*pi*n/N) + randn(1,N);
figure(1)
clf
line_handle = plot(n,x)
title('Noisy data')
xlabel('Time')
xlim([0, N])
drawnow;

uicontrol('Style','Slider', ...
    'Min',0.0,'Max',5.0, ...
    'Value', 0.2,...
    'SliderStep',[0.02 0.05],...
    'Position',[5 5 300 20],...
    'Callback',{@fun1, line_handle, x});

end

function fun1(hObject,eventdata, line_handle, x)
 fc = get(hObject,'Value')
 fc = min(fc,0.01)
 fc = max(fc,0.49)
 
 [b, a] = butter(2,2*fc);
 y = filtfilt(b, a, x);
 set(line_handle, 'ydata', y)
 title(sprintf('Output of LPF. Cut-off freq. = %.3f',fc));

end


