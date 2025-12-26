**2.**
Вектора образуют базис, если они линейно независимы.
$|(\mathbf{a}, \mathbf{b}, \mathbf{c})| = \begin{vmatrix} 3 & -2 & -3 \\ 2 & 0 & 1 \\ 2 & -1 & -1 \end{vmatrix} = 3 \cdot \begin{vmatrix} 0 & 1 \\ -1 & -1 \end{vmatrix} - (-2) \cdot \begin{vmatrix} 2 & 1 \\ 2 & -1 \end{vmatrix} + (-3) \cdot \begin{vmatrix} 2 & 0 \\ 2 & -1 \end{vmatrix} =$
$= 3(0 - (-1)) + 2(-2 - 2) - 3(-2 - 0) = 3(1) + 2(-4) + 6 = 3 - 8 + 6 = 1 \neq 0$.
$\Rightarrow$ вектора линейно независимы $\Rightarrow$ векторы образуют базис.

$x\mathbf{a} + y\mathbf{b} + z\mathbf{c} = \mathbf{d}$
$\begin{cases} 3x - 2y - 3z = -1 \\ 2x + 0y + z = 5 \\ 2x - y - z = 1 \end{cases}$
Из второго уравнения: $z = 5 - 2x$.
Подставим в третье уравнение:
$2x - y - (5 - 2x) = 1 \Rightarrow 4x - y = 6 \Rightarrow y = 4x - 6$.
Подставим $y$ и $z$ в первое уравнение:
$3x - 2(4x - 6) - 3(5 - 2x) = -1$
$3x - 8x + 12 - 15 + 6x = -1$
$x - 3 = -1 \Rightarrow x = 2$.
$y = 4(2) - 6 = 2$.
$z = 5 - 2(2) = 1$.
$\mathbf{d} = 2\mathbf{a} + 2\mathbf{b} + \mathbf{c}$.

**3.**
$|\mathbf{m}| = 1, |\mathbf{n}| = 2, (\widehat{\mathbf{m}, \mathbf{n}}) = \frac{\pi}{3}$.
$\mathbf{m}^2 = |\mathbf{m}|^2 = 1$.
$\mathbf{n}^2 = |\mathbf{n}|^2 = 4$.
$\mathbf{m}\cdot\mathbf{n} = |\mathbf{m}||\mathbf{n}|\cos\frac{\pi}{3} = 1 \cdot 2 \cdot \frac{1}{2} = 1$.

$\mathbf{a} \cdot \mathbf{b} = (3\mathbf{m} + \mathbf{n})(2\mathbf{m} - \mathbf{n}) = 6\mathbf{m}^2 - 3\mathbf{m}\mathbf{n} + 2\mathbf{m}\mathbf{n} - \mathbf{n}^2 = 6(1) - 1(1) - 4 = 1$.
$|\mathbf{a}| = \sqrt{(3\mathbf{m} + \mathbf{n})^2} = \sqrt{9\mathbf{m}^2 + 6\mathbf{m}\mathbf{n} + \mathbf{n}^2} = \sqrt{9(1) + 6(1) + 4} = \sqrt{19}$.
$|\mathbf{b}| = \sqrt{(2\mathbf{m} - \mathbf{n})^2} = \sqrt{4\mathbf{m}^2 - 4\mathbf{m}\mathbf{n} + \mathbf{n}^2} = \sqrt{4(1) - 4(1) + 4} = \sqrt{4} = 2$.
$\cos \varphi = \frac{\mathbf{a} \cdot \mathbf{b}}{|\mathbf{a}| |\mathbf{b}|} = \frac{1}{2\sqrt{19}}$.

**4.**
$\mathbf{x} = \mathbf{b} + \mathbf{c} = (5-5; 2+1; -1-1) = (0; 3; -2)$.
$\mathbf{y} = \mathbf{a} = (5; 2; -2)$.
$\text{пр}_{\mathbf{y}} \mathbf{x} = \frac{\mathbf{x} \cdot \mathbf{y}}{|\mathbf{y}|}$.
$\mathbf{x} \cdot \mathbf{y} = 0 \cdot 5 + 3 \cdot 2 + (-2) \cdot (-2) = 0 + 6 + 4 = 10$.
$|\mathbf{y}| = \sqrt{5^2 + 2^2 + (-2)^2} = \sqrt{25 + 4 + 4} = \sqrt{33}$.
$\text{пр}_{\mathbf{y}} \mathbf{x} = \frac{10}{\sqrt{33}}$.

**5.**
$\mathbf{N} = \vec{AB} \times \vec{AC} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -1 & 3 & 1 \\ -2 & 8 & 1 \end{vmatrix} = \mathbf{i}(3-8) - \mathbf{j}(-1-(-2)) + \mathbf{k}(-8-(-6)) = -5\mathbf{i} - \mathbf{j} - 2\mathbf{k}$.
$\mathbf{N} = (-5; -1; -2)$.
$|\mathbf{N}| = \sqrt{(-5)^2 + (-1)^2 + (-2)^2} = \sqrt{25 + 1 + 4} = \sqrt{30}$.
$\mathbf{n}_0 = \pm \frac{\mathbf{N}}{|\mathbf{N}|} = \pm \left( -\frac{5}{\sqrt{30}}; -\frac{1}{\sqrt{30}}; -\frac{2}{\sqrt{30}} \right)$.

**6.**
$S = |\mathbf{a} \times \mathbf{b}| = |(-4\mathbf{m} - 4\mathbf{n}) \times (2\mathbf{m} - 3\mathbf{n})|$.
$\mathbf{a} \times \mathbf{b} = -8(\mathbf{m} \times \mathbf{m}) + 12(\mathbf{m} \times \mathbf{n}) - 8(\mathbf{n} \times \mathbf{m}) + 12(\mathbf{n} \times \mathbf{n})$.
Так как $\mathbf{m} \times \mathbf{m} = \mathbf{0}$, $\mathbf{n} \times \mathbf{n} = \mathbf{0}$ и $\mathbf{n} \times \mathbf{m} = -(\mathbf{m} \times \mathbf{n})$:
$\mathbf{a} \times \mathbf{b} = 12(\mathbf{m} \times \mathbf{n}) + 8(\mathbf{m} \times \mathbf{n}) = 20(\mathbf{m} \times \mathbf{n})$.
$S = 20 |\mathbf{m}| |\mathbf{n}| \sin(\widehat{\mathbf{m}, \mathbf{n}}) = 20 \cdot 2 \cdot 5 \cdot \sin \frac{3\pi}{4} = 200 \cdot \frac{\sqrt{2}}{2} = 100\sqrt{2}$.

**7.**
$\vec{AB} = (-1-0; 2-3; 7-9) = (-1; -1; -2)$.
$\vec{AC} = (2-0; 4-3; 12-9) = (2; 1; 3)$.
$\vec{AD} = (0-0; 2-3; 8-9) = (0; -1; -1)$.
$(\vec{AB}, \vec{AC}, \vec{AD}) = \begin{vmatrix} -1 & -1 & -2 \\ 2 & 1 & 3 \\ 0 & -1 & -1 \end{vmatrix} = -1(-1 - (-3)) - (-1)(-2 - 0) + (-2)(-2 - 0) = -2 - 2 + 4 = 0$.
Смешанное произведение равно 0, значит точки лежат в одной плоскости.

**8.**
$\vec{A_1A_2} = (6 - (-2); 3 - 6; 5 - 0) = (8; -3; 5)$.
$\vec{A_1A_4} = (5 - (-2); 2 - 6; 5 - 0) = (7; -4; 5)$.
$\vec{A_1B_1} = (-1 - (-2); 4 - 6; 1 - 0) = (1; -2; 1)$.
$V = |(\vec{A_1A_2}, \vec{A_1A_4}, \vec{A_1B_1})| = \left| \begin{vmatrix} 8 & -3 & 5 \\ 7 & -4 & 5 \\ 1 & -2 & 1 \end{vmatrix} \right|$.
$\begin{vmatrix} 1 & -2 & 1 \\ 8 & -3 & 5 \\ 7 & -4 & 5 \end{vmatrix} = 1(-15 - (-20)) - (-2)(40 - 35) + 1(-32 - (-21)) = 5 + 10 - 11 = 4$.
$V = 4$.
Площадь основания $S = |\vec{A_1A_2} \times \vec{A_1A_4}|$.
$\vec{A_1A_2} \times \vec{A_1A_4} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 8 & -3 & 5 \\ 7 & -4 & 5 \end{vmatrix} = \mathbf{i}(-15 + 20) - \mathbf{j}(40 - 35) + \mathbf{k}(-32 + 21) = 5\mathbf{i} - 5\mathbf{j} - 11\mathbf{k} = (5; -5; -11)$.
$S = \sqrt{5^2 + (-5)^2 + (-11)^2} = \sqrt{25 + 25 + 121} = \sqrt{171} = 3\sqrt{19}$.
$h = \frac{V}{S} = \frac{4}{3\sqrt{19}}$.

**9.**
$\mathbf{n}_{\alpha} = (-2; 2; 4)$.
$\mathbf{n}_{\beta} = (0; 1; 2)$.
$\cos \varphi = \frac{|\mathbf{n}_{\alpha} \cdot \mathbf{n}_{\beta}|}{|\mathbf{n}_{\alpha}| |\mathbf{n}_{\beta}|} = \frac{|-2(0) + 2(1) + 4(2)|}{\sqrt{4+4+16}\sqrt{0+1+4}} = \frac{10}{\sqrt{24}\sqrt{5}} = \frac{10}{2\sqrt{6}\sqrt{5}} = \frac{5}{\sqrt{30}}$.

**10.**
а) $\vec{AB} = (1; -4; 0)$. $\vec{AC} = (-3; 7; 1)$.
$\mathbf{n} = \vec{AB} \times \vec{AC} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 & -4 & 0 \\ -3 & 7 & 1 \end{vmatrix} = \mathbf{i}(-4) - \mathbf{j}(1) + \mathbf{k}(7-12) = -4\mathbf{i} - \mathbf{j} - 5\mathbf{k} = (-4; -1; -5)$.
Уравнение плоскости: $-4(x - (-1)) - 1(y - (-1)) - 5(z - (-5)) = 0$.
$-4x - 4 - y - 1 - 5z - 25 = 0$.
$4x + y + 5z + 30 = 0$.

б) $S(6; 8; -7)$.
$d = \frac{|Ax_0 + By_0 + Cz_0 + D|}{\sqrt{A^2 + B^2 + C^2}} = \frac{|4(6) + 1(8) + 5(-7) + 30|}{\sqrt{16 + 1 + 25}} = \frac{|24 + 8 - 35 + 30|}{\sqrt{42}} = \frac{27}{\sqrt{42}}$.

**11.**
$\mathbf{n}_1 = (4; -1; -7)$.
$\mathbf{n}_2 = (-3; 1; 5)$.
$\mathbf{N} = \mathbf{n}_1 \times \mathbf{n}_2 = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 4 & -1 & -7 \\ -3 & 1 & 5 \end{vmatrix} = \mathbf{i}(-5+7) - \mathbf{j}(20-21) + \mathbf{k}(4-3) = 2\mathbf{i} + \mathbf{j} + \mathbf{k} = (2; 1; 1)$.
Уравнение плоскости через точку $M(4; 5; 2)$:
$2(x - 4) + 1(y - 5) + 1(z - 2) = 0$.
$2x - 8 + y - 5 + z - 2 = 0$.
$2x + y + z - 15 = 0$.

**12.**
Сторона $AB$: $\vec{AB} = (1; 2; -3)$. Уравнение: $\frac{x-2}{1} = \frac{y-3}{2} = \frac{z-9}{-3}$.
Сторона $BC$: $\vec{BC} = (-2; -3; 5)$. Уравнение: $\frac{x-3}{-2} = \frac{y-5}{-3} = \frac{z-6}{5}$.
Сторона $AC$: $\vec{AC} = (-1; -1; 2)$. Уравнение: $\frac{x-2}{-1} = \frac{y-3}{-1} = \frac{z-9}{2}$.

**13.**
$\mathbf{n}_1 = (-2; 2; -1)$.
$\mathbf{n}_2 = (5; -1; 1)$.
$\mathbf{s} = \mathbf{n}_1 \times \mathbf{n}_2 = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -2 & 2 & -1 \\ 5 & -1 & 1 \end{vmatrix} = \mathbf{i}(2-1) - \mathbf{j}(-2+5) + \mathbf{k}(2-10) = \mathbf{i} - 3\mathbf{j} - 8\mathbf{k} = (1; -3; -8)$.
Точка на прямой (пусть $x=0$):
$\begin{cases} 2y - z = 7 \\ -y + z = -8 \end{cases} \Rightarrow y = -1, z = -9$.
$M_0(0; -1; -9)$.
Каноническое уравнение: $\frac{x}{1} = \frac{y+1}{-3} = \frac{z+9}{-8}$.

**14.**
Нормаль плоскости $\mathbf{n} = (6; -1; -5)$.
Прямая $MM_1$ перпендикулярна плоскости, значит $\mathbf{s} = \mathbf{n} = (6; -1; -5)$.
Уравнение прямой: $x = -7 + 6t$, $y = 1 - t$, $z = 5 - 5t$.
Точка пересечения с плоскостью:
$6(-7 + 6t) - (1 - t) - 5(5 - 5t) - 25 = 0$.
$-42 + 36t - 1 + t - 25 + 25t - 25 = 0$.
$62t - 93 = 0 \Rightarrow t = \frac{93}{62} = \frac{3}{2} = 1.5$.
Координаты точки пересечения $O$:
$x_0 = -7 + 6(1.5) = 2$.
$y_0 = 1 - 1.5 = -0.5$.
$z_0 = 5 - 5(1.5) = -2.5$.
$O$ — середина $MM_1$.
$x_1 = 2x_0 - x = 4 - (-7) = 11$.
$y_1 = 2y_0 - y = -1 - 1 = -2$.
$z_1 = 2z_0 - z = -5 - 5 = -10$.
$M_1(11; -2; -10)$.

**15.**
Направляющий вектор прямой $\mathbf{s} = (-1; -6; 1)$.
Нормаль плоскости $\mathbf{n} = (-1; 1; -1)$.
$\sin \varphi = \frac{|\mathbf{s} \cdot \mathbf{n}|}{|\mathbf{s}| |\mathbf{n}|} = \frac{|(-1)(-1) + (-6)(1) + 1(-1)|}{\sqrt{1+36+1}\sqrt{1+1+1}} = \frac{|1 - 6 - 1|}{\sqrt{38}\sqrt{3}} = \frac{6}{\sqrt{114}}$.
$\varphi = \arcsin \frac{6}{\sqrt{114}}$.