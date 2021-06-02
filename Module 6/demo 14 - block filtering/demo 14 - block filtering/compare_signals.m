
[x1, Fs] = audioread('author.wav');

[x2, Fs] = audioread('author_output.wav');

[x3, Fs] = audioread('author_output_blocks.wav');

N = length(x1);
n = 0:N-1;
t = n/Fs;

%%

N3 = length(x3);
OFFSET = 0.3;

figure(1)
clf
plot(t, x2+OFFSET, 'b', t(1:N3), x3, 'r')
GRAY = [1 1 1]*0.5;
line([0 t(end)], [0 0], 'color', GRAY)
line([0 t(end)], [OFFSET OFFSET], 'color', GRAY)
legend('Correct', 'Incorrect')
xlabel('Time (sec)')
zoom xon

%%

xlim([0.32 0.35])
ylim([-0.3 0.6])

orient landscape
print -dpdf compare_signals

