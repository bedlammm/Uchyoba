x = -5:0.1:5;
y = 4 .* x.^2 - 2 .* x + 6;
figure;
plot(x, y, 'y-.', 'LineWidth', 2);
set(gca, 'Color', [0.3 0.3 0.3]); 
grid on;
title('f(x) = 4x^2 - 2x + 6');
xlabel('X');
ylabel('Y');