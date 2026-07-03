syms m l g k h t A B phi1 phi2 real

% 1. Синфазные колебания (маятники отклоняются вместе, пружина не деформируется)
% Работает только гравитация. Уравнение: I*alpha = M_mg
omega1 = sqrt(g / l);

% 2. Противофазные колебания (маятники отклоняются в разные стороны на угол theta)
% Пружина растягивается на 2*x, где x = h*theta. Сила F = k*2*h*theta.
% Момент силы пружины: M_k = F * h = 2*k*h^2*theta.
% Уравнение: m*l^2 * theta_ddot = -m*g*l*theta - 2*k*h^2*theta
omega2 = sqrt((m*g*l + 2*k*h^2) / (m*l^2));
disp('Частота синфазных колебаний (w1):'); disp(omega1);
disp('Частота противофазных колебаний (w2):'); disp(omega2);
disp('Закон движения системы (суперпозиция нормальных мод):');
theta1 = A*cos(omega1*t + phi1) + B*cos(omega2*t + phi2);
theta2 = A*cos(omega1*t + phi1) - B*cos(omega2*t + phi2);
disp('Угол отклонения 1-го маятника:'); disp(theta1);
disp('Угол отклонения 2-го маятника:'); disp(theta2);

% Произвольные значения для визуализации биений
m_val = 1; l_val = 1; g_val = 9.81; k_val = 5; h_val = 0.5;
w1_num = sqrt(g_val / l_val);
w2_num = sqrt((m_val*g_val*l_val + 2*k_val*h_val^2) / (m_val*l_val^2));
t_num = 0:0.05:20;
% Начальные условия: отклонили только первый маятник
A_num = 0.1; B_num = 0.1; 
th1_num = A_num*cos(w1_num*t_num) + B_num*cos(w2_num*t_num);
th2_num = A_num*cos(w1_num*t_num) - B_num*cos(w2_num*t_num);
figure;
plot(t_num, th1_num, 'r-', 'LineWidth', 1.5); hold on;
plot(t_num, th2_num, 'b--', 'LineWidth', 1.5);
grid on;
title('Закон движения связанных маятников (явление биений)');
xlabel('Время t, с');
ylabel('Угол отклонения \theta, рад');
legend('Маятник 1', 'Маятник 2');