% x^2/16 + y^2/4 - z^2 = 9
% При z = 0: x^2/16 + y^2/4 = 9
% x^2/16 + y^2/4 = 9 | : 9 => x^2/(16*9) + y^2/(4*9) = 1  =>  x^2/144 + y^2/36 = 1
% a^2 = 144 => a = 12
% b^2 = 36  => b = 6
% Площадь эллипса S = pi * a * b
a = sqrt(16 * 9);
b = sqrt(4 * 9);
S = pi * a * b;
fprintf('Полуоси сечения при z=0: a = %.0f, b = %.0f\n', a, b);
fprintf('Площадь сечения (z=0): S = %.4f = %d*pi\n', S, a*b);
figure;
f = @(x, y, z) (x.^2)/16 + (y.^2)/4 - z.^2 - 9;
fimplicit3(f, [-20 20 -10 10 -10 10], 'EdgeColor', 'none');
colormap jet;
shading interp;     
colorbar;           
camlight;           
lighting gouraud;
title('x^2/16 + y^2/4 - z^2 = 9');
xlabel('Ось X');
ylabel('Ось Y');
zlabel('Ось Z');