syms x_sym;
y_upper = x_sym;      % Прямая проходит выше параболы на [0, 1]
y_lower = x_sym^2;    % Парабола 
% 1. Точки пересечения (границы интегрирования)
limits = solve(y_upper == y_lower, x_sym);
a = double(min(limits)); % 0
b = double(max(limits)); % 1
% 2. Формула объема тела вращения с отверстием внутри (шайбы):
% V = pi * int( R_upper^2 - r_lower^2 ) dx
V_expr = pi * (y_upper^2 - y_lower^2);
V_sym = int(V_expr, x_sym, a, b);
fprintf('Границы интегрирования: от x = %d до x = %d\n', a, b);
disp(['Точное значение объема: V = ', char(V_sym)]);
fprintf('Численное значение: V = %.4f\n', double(V_sym));
figure;
% Двумерная площадь, которая вращается
subplot(1, 2, 1);
x_num = linspace(-0.2, 1.2, 100);
plot(x_num, x_num, 'b-', 'LineWidth', 1.5); hold on;
plot(x_num, x_num.^2, 'r-', 'LineWidth', 1.5);
% Заливка области
fill([linspace(0,1,50) linspace(1,0,50)], ...
     [linspace(0,1,50) linspace(1,0,50).^2], 'g', 'FaceAlpha', 0.3);
grid on;
title('Вращаемая область (2D)');
xlabel('Ось X'); ylabel('Ось Y');
legend('y = x', 'y = x^2', 'Площадь сечения');
% Трехмерная визуализация самого тела вращения
subplot(1, 2, 2);
theta = linspace(0, 2*pi, 40);
x_3d = linspace(0, 1, 40);
[T, X_grid] = meshgrid(theta, x_3d);
% Поверхность от прямой y = x (внешний конус)
R_out = X_grid; 
Y_out = R_out .* cos(T);
Z_out = R_out .* sin(T);
surf(X_grid, Y_out, Z_out, 'FaceColor', 'b', 'FaceAlpha', 0.5, 'EdgeColor', 'none'); hold on;
% Поверхность от параболы y = x^2 (внутренняя воронка)
R_in = X_grid.^2; 
Y_in = R_in .* cos(T);
Z_in = R_in .* sin(T);
surf(X_grid, Y_in, Z_in, 'FaceColor', 'r', 'FaceAlpha', 0.8, 'EdgeColor', 'none');
view(30, 30);
camlight; lighting gouraud;
title('Полученное тело вращения (3D)');
xlabel('Ось X'); ylabel('Ось Y'); zlabel('Ось Z');
axis equal;