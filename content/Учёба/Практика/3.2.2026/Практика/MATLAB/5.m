syms x_sym;
y_sym = log(cos(x_sym));

% Формула длины дуги: L = int( sqrt(1 + (dy/dx)^2) )

dy_dx = diff(y_sym, x_sym);
L_expr = sqrt(1 + dy_dx^2);

% Символьное интегрирование

L_sym = int(L_expr, x_sym, 0, pi/4);
L_val = double(L_sym);
disp('--- Результат вычисления длины дуги ---');
disp(['Аналитический вид интеграла длины: ', char(L_sym)]);
fprintf('Точное числовое значение: L = %.4f\n', L_val);
x_num = linspace(0, pi/4, 100);
y_num = log(cos(x_num));
figure;
plot(x_num, y_num, 'b-', 'LineWidth', 2);
hold on; % это чтобы было 2 графика на одном холсте

% Отметим границы интегрирования красными узлами

plot(0, log(cos(0)), 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r');
plot(pi/4, log(cos(pi/4)), 'ro', 'MarkerSize', 8, 'MarkerFaceColor', 'r');
grid on;
title(['Длина дуги y = ln(cos x) на [0, \pi/4]. L = ', num2str(L_val, '%.3f')]);
xlabel('Ось X');
ylabel('Ось Y');
legend('Кривая', 'Границы интегрирования', 'Location', 'southwest');