> [!note]- Алгоритмы решения задач на сложные и неявные ФНП
> Здесь собраны паттерны решения задач на дифференцирование абстрактных функций. Во всех задачах предполагается, что $z$ — это функция от независимых переменных $x$ и $y$, то есть $z = z(x,y)$.

> [!example]- Задача 1 (Первое уравнение). Неявная функция со сложным аргументом
> **Условие:** Для функции $x^2 + z^3 + f(x - y^2) = 0$ найти $\frac{\partial z}{\partial x}, \frac{\partial z}{\partial y}$.
> 
> **Решение:**
> Уравнение задано неявно в виде $\Phi(x,y,z) = 0$, где $\Phi(x,y,z) = x^2 + z^3 + f(x - y^2)$.
> Используем формулы производной неявной функции (Лекция 14):
> $$ \frac{\partial z}{\partial x} = -\frac{\Phi'_x}{\Phi'_z}, \quad \frac{\partial z}{\partial y} = -\frac{\Phi'_y}{\Phi'_z} $$
> 
> Обозначим внутренний аргумент функции $f$ как $u = x - y^2$. Тогда $f(x-y^2) = f(u)$. 
> Найдём частные производные $\Phi$ по всем трём переменным, считая остальные константами (для взятия производной от $f$ используем правило сложной функции: $f'_x = f'_u \cdot u'_x$):
> 
> 1. По $x$ ($y, z = \text{const}$): 
>    $$ \Phi'_x = 2x + 0 + f'_u \cdot (x - y^2)'_x = 2x + f'_u \cdot 1 = 2x + f'_u $$
> 2. По $y$ ($x, z = \text{const}$): 
>    $$ \Phi'_y = 0 + 0 + f'_u \cdot (x - y^2)'_y = f'_u \cdot (-2y) = -2y f'_u $$
> 3. По $z$ ($x, y = \text{const}$): 
>    $$ \Phi'_z = 0 + 3z^2 + 0 = 3z^2 $$
> 
> Подставляем в формулы неявной функции:
> $$ \frac{\partial z}{\partial x} = -\frac{2x + f'_u}{3z^2} $$
> $$ \frac{\partial z}{\partial y} = -\frac{-2y f'_u}{3z^2} = \frac{2y f'_u}{3z^2} $$
> *(В ответе можно оставить $f'_u$ или написать $f'_{(x-y^2)}$, это одно и то же).*

> [!example]- Задача 1 (Второе уравнение). Метод полных дифференциалов
> **Условие:** Для функции $F\left(\frac{y}{x}, \frac{z}{y}\right) = 0$ найти $\frac{\partial z}{\partial x}, \frac{\partial z}{\partial y}$.
> 
> **Решение:**
> Здесь функция $z$ "зашита" прямо внутрь аргумента $F$. Если решать через формулы $-\frac{F'_x}{F'_z}$, можно легко запутаться в производных дробей. **Самый надёжный способ (из Лекции 14) — взять полный дифференциал от обеих частей.**
> 
> Обозначим аргументы $F$ как $u = \frac{y}{x}$ и $v = \frac{z}{y}$. Тогда $F(u,v) = 0$.
> Берем полный дифференциал $dF = 0$:
> $$ F'_u du + F'_v dv = 0 \quad (*) $$
> 
> Распишем дифференциалы аргументов $u$ и $v$, используя правила дифференцирования дроби:
> $$ du = d\left(\frac{y}{x}\right) = \frac{x\,dy - y\,dx}{x^2} $$
> $$ dv = d\left(\frac{z}{y}\right) = \frac{y\,dz - z\,dy}{y^2} $$
> 
> Подставим их в $(*)$:
> $$ F'_u \frac{x\,dy - y\,dx}{x^2} + F'_v \frac{y\,dz - z\,dy}{y^2} = 0 $$
> 
> Наша цель — выразить $dz$ через $dx$ и $dy$, чтобы получить вид $dz = \frac{\partial z}{\partial x}dx + \frac{\partial z}{\partial y}dy$.
> Оставим слагаемое с $dz$ слева, остальное перенесем вправо:
> $$ F'_v \frac{y\,dz}{y^2} = - F'_u \frac{x\,dy - y\,dx}{x^2} + F'_v \frac{z\,dy}{y^2} $$
> $$ \frac{F'_v}{y} dz = F'_u \frac{y}{x^2} dx - F'_u \frac{1}{x} dy + F'_v \frac{z}{y^2} dy $$
> 
> Вынесем $dx$ и $dy$ за скобки справа:
> $$ \frac{F'_v}{y} dz = \left( F'_u \frac{y}{x^2} \right) dx + \left( F'_v \frac{z}{y^2} - F'_u \frac{1}{x} \right) dy $$
> 
> Умножим обе части на $\frac{y}{F'_v}$:
> $$ dz = \left( \frac{F'_u}{F'_v} \frac{y^2}{x^2} \right) dx + \left( \frac{z}{y} - \frac{F'_u}{F'_v} \frac{y}{x} \right) dy $$
> 
> Коэффициент при $dx$ — это $\frac{\partial z}{\partial x}$, а при $dy$ — это $\frac{\partial z}{\partial y}$.
> **Ответ:**
> $$ \frac{\partial z}{\partial x} = \frac{F'_u}{F'_v} \frac{y^2}{x^2}, \quad \frac{\partial z}{\partial y} = \frac{z}{y} - \frac{F'_u}{F'_v} \frac{y}{x} $$

> [!example]- Задача 2. Явно заданная сложная функция
> **Условие:** Для функции $z = f\left(\frac{2xy}{x+y}, x^3 - 2y\right)$ найти $\frac{\partial z}{\partial x}, \frac{\partial z}{\partial y}$.
> 
> **Решение:**
> Функция задана **явно** ($z = \dots$), но является сложной.
> Пусть $z = f(u, v)$, где $u = \frac{2xy}{x+y}$, а $v = x^3 - 2y$.
> По теореме о производной сложной функции (Лекция 13):
> $$ \frac{\partial z}{\partial x} = f'_u \cdot \frac{\partial u}{\partial x} + f'_v \cdot \frac{\partial v}{\partial x} $$
> $$ \frac{\partial z}{\partial y} = f'_u \cdot \frac{\partial u}{\partial y} + f'_v \cdot \frac{\partial v}{\partial y} $$
> 
> Считаем внутренние производные по $x$ ($y = \text{const}$):
> $$ u'_x = \left(\frac{2xy}{x+y}\right)'_x = \frac{(2y)(x+y) - (2xy)(1)}{(x+y)^2} = \frac{2xy + 2y^2 - 2xy}{(x+y)^2} = \frac{2y^2}{(x+y)^2} $$
> $$ v'_x = (x^3 - 2y)'_x = 3x^2 $$
> Собираем первую производную:
> $$ \frac{\partial z}{\partial x} = f'_u \cdot \frac{2y^2}{(x+y)^2} + f'_v \cdot 3x^2 $$
> 
> Считаем внутренние производные по $y$ ($x = \text{const}$):
> $$ u'_y = \left(\frac{2xy}{x+y}\right)'_y = \frac{(2x)(x+y) - (2xy)(1)}{(x+y)^2} = \frac{2x^2 + 2xy - 2xy}{(x+y)^2} = \frac{2x^2}{(x+y)^2} $$
> $$ v'_y = (x^3 - 2y)'_y = -2 $$
> Собираем вторую производную:
> $$ \frac{\partial z}{\partial y} = f'_u \cdot \frac{2x^2}{(x+y)^2} - 2 f'_v $$
> **Ответ получен.**

> [!example]- Дополнительный пример 1 (Неявная сложная функция)
> **Условие:** Найти $\frac{\partial z}{\partial x}, \frac{\partial z}{\partial y}$, если $z^2 + x\sin(y) - G(x^2 z) = 0$.
> 
> **Решение:**
> Используем формулы $\frac{\partial z}{\partial x} = -\frac{\Phi'_x}{\Phi'_z}$, $\frac{\partial z}{\partial y} = -\frac{\Phi'_y}{\Phi'_z}$.
> $\Phi(x,y,z) = z^2 + x\sin(y) - G(u)$, где $u = x^2 z$.
> 
> 4. $\Phi'_x = 0 + \sin(y) - G'_u \cdot (x^2 z)'_x = \sin(y) - G'_u \cdot 2xz$
> 5. $\Phi'_y = 0 + x\cos(y) - 0 = x\cos(y)$
> 6. $\Phi'_z = 2z + 0 - G'_u \cdot (x^2 z)'_z = 2z - G'_u \cdot x^2$
> 
> Собираем ответ:
> $$ \frac{\partial z}{\partial x} = -\frac{\sin(y) - 2xz \cdot G'_u}{2z - x^2 \cdot G'_u} $$
> $$ \frac{\partial z}{\partial y} = -\frac{x\cos(y)}{2z - x^2 \cdot G'_u} $$

> [!example]- Дополнительный пример 2 (Явная сложная функция)
> **Условие:** Найти $\frac{\partial z}{\partial x}, \frac{\partial z}{\partial y}$, если $z = f(x^2 - y^2, e^{xy})$.
> 
> **Решение:**
> $z = f(u,v)$, где $u = x^2 - y^2$, $v = e^{xy}$.
> Используем цепное правило (Лекция 13):
> $u'_x = 2x, \quad v'_x = e^{xy} \cdot y$
> $u'_y = -2y, \quad v'_y = e^{xy} \cdot x$
> 
> Подставляем:
> $$ \frac{\partial z}{\partial x} = f'_u \cdot (2x) + f'_v \cdot (y e^{xy}) $$
> $$ \frac{\partial z}{\partial y} = f'_u \cdot (-2y) + f'_v \cdot (x e^{xy}) $$

---

> [!note]- Формулы: Дифференцирование сложной функции (Задачи 2, 5)
> Пусть $z = f(u, v)$, где промежуточные аргументы зависят от независимых переменных $u = u(x, y)$ и $v = v(x, y)$.
> Частные производные вычисляются по цепному правилу:
> $$ \frac{\partial z}{\partial x} = f'_u \cdot \frac{\partial u}{\partial x} + f'_v \cdot \frac{\partial v}{\partial x} $$
> $$ \frac{\partial z}{\partial y} = f'_u \cdot \frac{\partial u}{\partial y} + f'_v \cdot \frac{\partial v}{\partial y} $$

> [!note]- Формулы: Производные неявно заданной функции (Задачи 1)
> Если функция задана уравнением $F(x, y, z) = 0$, то её частные производные вычисляются по формулам:
> $$ \frac{\partial z}{\partial x} = -\frac{F'_x}{F'_z} $$
> $$ \frac{\partial z}{\partial y} = -\frac{F'_y}{F'_z} $$
> Условие: $F'_z \neq 0$.
> 
> Если функция спрятана в аргументах $F(u, v) = 0$, где $u = u(x,y,z)$ и $v = v(x,y,z)$, используется метод взятия полного дифференциала от обеих частей: $dF = F'_u du + F'_v dv = 0$, из которого алгебраически выражается $dz$.

> [!note]- Формулы: Полный дифференциал (Задачи 3, 4)
> Полный дифференциал функции 2-х переменных $z = f(x, y)$:
> $$ dz = \frac{\partial z}{\partial x}dx + \frac{\partial z}{\partial y}dy $$
> 
> Полный дифференциал функции 3-х переменных $u = f(x, y, z)$:
> $$ du = \frac{\partial u}{\partial x}dx + \frac{\partial u}{\partial y}dy + \frac{\partial u}{\partial z}dz $$
> *Алгоритм для неявной функции $F(x,y,z)=0$:* Взять полный дифференциал от обеих частей $F'_x dx + F'_y dy + F'_z dz = 0$, подставить координаты точки $M$ и выразить $dz$.

> [!note]- Формулы: Линии и поверхности уровня (Задачи 6, 7, 8)
> **Линия уровня** для функции двух переменных $z = f(x,y)$:
> $$ f(x,y) = C $$
> **Поверхность уровня** для функции трех переменных $u = f(x,y,z)$:
> $$ f(x,y,z) = C $$
> *(где $C$ — константа, которую можно найти, подставив координаты заданной точки $M_0$ в функцию).*

> [!note]- Формулы: Градиент и производная по направлению (Задачи 6, 7, 8)
> **Градиент** (вектор, указывающий направление наискорейшего роста):
> Для 2D: $\text{grad } z = \left( \frac{\partial z}{\partial x}, \frac{\partial z}{\partial y} \right)$
> Для 3D: $\text{grad } u = \left( \frac{\partial u}{\partial x}, \frac{\partial u}{\partial y}, \frac{\partial u}{\partial z} \right)$
> 
> **Единичный вектор направления** $\bar{l}^0$:
> Если задан вектор $\bar{l} = (l_x, l_y, l_z)$, его длина $|\bar{l}| = \sqrt{l_x^2 + l_y^2 + l_z^2}$.
> Направляющие косинусы:
> $$ \cos\alpha = \frac{l_x}{|\bar{l}|}, \quad \cos\beta = \frac{l_y}{|\bar{l}|}, \quad \cos\gamma = \frac{l_z}{|\bar{l}|} $$
> 
> **Производная по направлению вектора $\bar{l}$:**
> Вычисляется как скалярное произведение градиента на единичный вектор направления:
> $$ \frac{\partial u}{\partial l} = \frac{\partial u}{\partial x}\cos\alpha + \frac{\partial u}{\partial y}\cos\beta + \frac{\partial u}{\partial z}\cos\gamma $$
> 
> **Наибольшее значение производной по направлению:**
> Совпадает с длиной градиента в данной точке:
> $$ \max \frac{\partial u}{\partial l} = |\text{grad } u| = \sqrt{\left(\frac{\partial u}{\partial x}\right)^2 + \left(\frac{\partial u}{\partial y}\right)^2 + \left(\frac{\partial u}{\partial z}\right)^2} $$

> [!note]- Формулы: Касательная плоскость и нормаль (Задачи 9, 10)
> Поверхность задана неявно: $F(x,y,z) = 0$. Точка касания: $M_0(x_0, y_0, z_0)$.
> 
> **Уравнение касательной плоскости:**
> $$ F'_x(M_0) \cdot (x - x_0) + F'_y(M_0) \cdot (y - y_0) + F'_z(M_0) \cdot (z - z_0) = 0 $$
> 
> **Уравнение нормали (канонические уравнения прямой):**
> $$ \frac{x - x_0}{F'_x(M_0)} = \frac{y - y_0}{F'_y(M_0)} = \frac{z - z_0}{F'_z(M_0)} $$
> 
> **Условие параллельности плоскостей (для задачи 10):**
> Если касательная плоскость параллельна заданной плоскости $Ax + By + Cz + D = 0$, то их нормальные векторы коллинеарны. Составляется пропорция:
> $$ \frac{F'_x}{A} = \frac{F'_y}{B} = \frac{F'_z}{C} $$
> Из этой пропорции совместно с уравнением $F(x,y,z)=0$ находятся координаты точки касания $M_0$.