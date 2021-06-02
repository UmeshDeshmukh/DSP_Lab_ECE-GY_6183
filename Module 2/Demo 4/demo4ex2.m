clear 
close all 

%function filter_gui_example
Fs = 8000;          % sampling frequency (sample/second)
F1 = 400;           % frequency (Hz)
f1 = F1/Fs          % normalized frequency (cycles/sample)
om1 = 2*pi * f1;    % normalized frequency (radians/sample)

Ta = 0.5;           % duration (seconds) [time till 1% amplitude]
r = 0.01^(1/(Ta*Fs))

a = [1 -2*r*cos(om1) r^2]   % recursive part
b = 1; 

N1 = 50;
n = 0:N1;

imp = [1 zeros(1, N1)];
h = filter(b, a, imp);

figure(1)
subplot(2,1,1)
line_handle = plot(n, h, 'o-', n, r.^n, '--')
legend('Impulse response', 'Amplitude envelope')
xlabel('Time (n)')
title('Impulse response')

[H, om] = freqz(b, a);
f = om / (2*pi) * Fs;
line_handle2 = plot(f, abs(H))
title('Frequency response')
xlabel('Frequency (Hz)')
drawnow;

uicontrol('Style', 'slider', ...
    'Min', 0.01, 'Max', 0.99,...
    'Value', 0.2, ...
    'SliderStep', [0.02 0.05], ...
    'Position', [5 5 200 20], ...           % [left, bottom, width, height]
    'Callback',  {@fun1, line_handle,line_handle2, x}    );

%end

function fun1(hObject, line_handle, line_handle2, x)
 fc = get(hObject, 'Value');
 fc = max(fc, 0.99);
 fc = min(fc, 0.01);
 
 [b, a] = butter(2, 2*fc);
%% Impulse response
% The amplitude envelope has the form r^n.

N = Fs;
n = 0:N;

imp = [1 zeros(1, N)];
h = filter(b, a, imp);
set(line_handle, 'ydata',  h); 
%% Frequency response
% The frequency response has a peak at f1

[H, om] = freqz(b2, a2);
f = om / (2*pi) * Fs;
set(line_handle2, 'ydata',  h);
end