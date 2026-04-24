> [!example]- Задача 2. Доказательство базиса и матрица перехода
> **Условие:**
> Заданы векторы $a_1 = \begin{pmatrix} 1 \\ -2 \end{pmatrix}, a_2 = \begin{pmatrix} 2 \\ 5 \end{pmatrix}$ и $b_1 = \begin{pmatrix} 1 \\ 5 \end{pmatrix}, b_2 = \begin{pmatrix} 2 \\ 9 \end{pmatrix}$.
> Доказать, что данные системы — базисы в $L$. Написать матрицу перехода $T_{b \to a}$.
> 
> **Решение:**
> **1. Доказательство базисов**
> Векторы образуют базис в $\mathbb{R}^2$, если они линейно независимы. Составим матрицы из координатных столбцов векторов и вычислим их определители.
> 
> Для системы $\{a\}$: 
> $$ \det A = \begin{vmatrix} 1 & 2 \\ -2 & 5 \end{vmatrix} = 1\cdot 5 - 2\cdot (-2) = 5 + 4 = 9 $$
> Так как $\det A \neq 0$, система $\{a\}$ линейно независима и образует базис.
> 
> Для системы $\{b\}$: 
> $$ \det B = \begin{vmatrix} 1 & 2 \\ 5 & 9 \end{vmatrix} = 1\cdot 9 - 2\cdot 5 = 9 - 10 = -1 $$
> Так как $\det B \neq 0$, система $\{b\}$ линейно независима и образует базис.
> 
> **2. Нахождение матрицы перехода $T_{b \to a}$**
> Известно, что матрицы базисов $A$ и $B$ (в некотором исходном стандартном базисе) связаны с матрицей перехода формулой:
> $$ A = B \cdot T_{b \to a} $$
> Отсюда выражаем искомую матрицу перехода:
> $$ T_{b \to a} = B^{-1} \cdot A $$
> 
> Найдем обратную матрицу $B^{-1}$. Для матрицы 2x2 меняем элементы главной диагонали местами, у побочной диагонали меняем знаки и делим на определитель ($\det B = -1$):
> $$ B^{-1} = \frac{1}{-1} \begin{pmatrix} 9 & -2 \\ -5 & 1 \end{pmatrix} = \begin{pmatrix} -9 & 2 \\ 5 & -1 \end{pmatrix} $$
> 
> Умножим $B^{-1}$ на $A$:
> $$ T_{b \to a} = \begin{pmatrix} -9 & 2 \\ 5 & -1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ -2 & 5 \end{pmatrix} = \begin{pmatrix} (-9)\cdot 1 + 2\cdot (-2) & (-9)\cdot 2 + 2\cdot 5 \\ 5\cdot 1 + (-1)\cdot (-2) & 5\cdot 2 + (-1)\cdot 5 \end{pmatrix} $$
> $$ T_{b \to a} = \begin{pmatrix} -9 - 4 & -18 + 10 \\ 5 + 2 & 10 - 5 \end{pmatrix} = \begin{pmatrix} -13 & -8 \\ 7 & 5 \end{pmatrix} $$
> 
> **Ответ:** Матрица перехода $T_{b \to a} = \begin{pmatrix} -13 & -8 \\ 7 & 5 \end{pmatrix}$.

> [!example]- Задача 3. Приведение квадратичной формы к каноническому виду ортогональным преобразованием
> **Условие:** $F(x,y,z) = x^2 + z^2 - 2xy + 4xz + 2yz$.
> 
> **Решение:**
> **1. Составление матрицы квадратичной формы**
> Коэффициенты при квадратах ставим на диагональ ($a_{22} = 0$, так как нет $y^2$). Остальные делим на 2.
> $$ A = \begin{pmatrix} 1 & -1 & 2 \\ -1 & 0 & 1 \\ 2 & 1 & 1 \end{pmatrix} $$
> 
> **2. Характеристическое уравнение и собственные значения**
> $$ \det(A - \lambda E) = \begin{vmatrix} 1-\lambda & -1 & 2 \\ -1 & -\lambda & 1 \\ 2 & 1 & 1-\lambda \end{vmatrix} = 0 $$
> Раскроем определитель:
> $$ (1-\lambda)(-\lambda(1-\lambda) - 1) - (-1)(-(1-\lambda) - 2) + 2(-1 - (-2\lambda)) = 0 $$
> $$ (1-\lambda)(\lambda^2 - \lambda - 1) + 1(\lambda - 3) + 2(2\lambda - 1) = 0 $$
> $$ (\lambda^2 - \lambda - 1 - \lambda^3 + \lambda^2 + \lambda) + \lambda - 3 + 4\lambda - 2 = 0 $$
> $$ -\lambda^3 + 2\lambda^2 + 5\lambda - 6 = 0 \Rightarrow \lambda^3 - 2\lambda^2 - 5\lambda + 6 = 0 $$
> Подбором находим первый корень: при $\lambda=1$ получим $1-2-5+6=0$. $\lambda_1 = 1$.
> Делим многочлен на $(\lambda - 1)$ и решаем оставшееся квадратное уравнение $\lambda^2 - \lambda - 6 = 0$.
> Его корни: $\lambda_2 = -2, \lambda_3 = 3$.
> Упорядочим корни: $\lambda_1 = -2, \lambda_2 = 1, \lambda_3 = 3$.
> 
> **Канонический вид:** $F(x', y', z') = -2(x')^2 + (y')^2 + 3(z')^2$.
> 
> **3. Нахождение собственных векторов**
> Решаем системы $(A - \lambda_i E)\vec{v}_i = 0$.
> 
> *Для $\lambda_1 = -2$*:
> $$ \begin{pmatrix} 3 & -1 & 2 \\ -1 & 2 & 1 \\ 2 & 1 & 3 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = 0 \Rightarrow \begin{cases} -x + 2y + z = 0 \\ 2x + y + 3z = 0 \end{cases} \Rightarrow \text{Пусть } y = 1 \Rightarrow \vec{v}_1 = \begin{pmatrix} 1 \\ 1 \\ -1 \end{pmatrix} $$
> 
> *Для $\lambda_2 = 1$*:
> $$ \begin{pmatrix} 0 & -1 & 2 \\ -1 & -1 & 1 \\ 2 & 1 & 0 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = 0 \Rightarrow \begin{cases} -y + 2z = 0 \\ 2x + y = 0 \end{cases} \Rightarrow \text{Пусть } z = 1 \Rightarrow \vec{v}_2 = \begin{pmatrix} -1 \\ 2 \\ 1 \end{pmatrix} $$
> 
> *Для $\lambda_3 = 3$*:
> $$ \begin{pmatrix} -2 & -1 & 2 \\ -1 & -3 & 1 \\ 2 & 1 & -2 \end{pmatrix} \begin{pmatrix} x \\ y \\ z \end{pmatrix} = 0 \Rightarrow \begin{cases} -2x - y + 2z = 0 \\ 2x + y - 2z = 0 \end{cases} \Rightarrow \text{Пусть } x = 1 \Rightarrow \vec{v}_3 = \begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix} $$
> 
> *(Проверка: векторы ортогональны, скалярные произведения попарно равны нулю).*
> 
> **4. Нормировка и матрица преобразования**
> Вычисляем длины векторов:
> $|\vec{v}_1| = \sqrt{1^2+1^2+(-1)^2} = \sqrt{3}$
> $|\vec{v}_2| = \sqrt{(-1)^2+2^2+1^2} = \sqrt{6}$
> $|\vec{v}_3| = \sqrt{1^2+0^2+1^2} = \sqrt{2}$
> 
> Составляем ортогональную матрицу перехода $T$, деля каждый вектор на его длину:
> $$ T = \begin{pmatrix} 1/\sqrt{3} & -1/\sqrt{6} & 1/\sqrt{2} \\ 1/\sqrt{3} & 2/\sqrt{6} & 0 \\ -1/\sqrt{3} & 1/\sqrt{6} & 1/\sqrt{2} \end{pmatrix} $$
> *Проверка определителя:* $\det T = 1$ (Преобразование является чистым поворотом).
> 
> **Ответ:** 
> Канонический вид: $F = -2(x')^2 + (y')^2 + 3(z')^2$.
> Преобразование: $\begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} 1/\sqrt{3} & -1/\sqrt{6} & 1/\sqrt{2} \\ 1/\sqrt{3} & 2/\sqrt{6} & 0 \\ -1/\sqrt{3} & 1/\sqrt{6} & 1/\sqrt{2} \end{pmatrix} \begin{pmatrix} x' \\ y' \\ z' \end{pmatrix}$.

> [!example]- Задача 4. Процесс ортогонализации Грама-Шмидта
> **Условие:**
> Заданы векторы $a_1 = (2, 2, 1)^T$, $a_2 = (3, 0, 3)^T$, $a_3 = (6, -3, 3)^T$. Построить ОНБ.
> 
> **Решение:**
> **Шаг 1. Построение ортогонального базиса $\{\bar{b}\}$**
> 1) Полагаем $\bar{b}_1 = \bar{a}_1 = \begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix}$.
> Скалярный квадрат: $(\bar{b}_1, \bar{b}_1) = 2^2 + 2^2 + 1^2 = 4 + 4 + 1 = 9$.
> 
> 2) $\bar{b}_2 = \bar{a}_2 - \frac{(\bar{a}_2, \bar{b}_1)}{(\bar{b}_1, \bar{b}_1)} \bar{b}_1$.
> $(\bar{a}_2, \bar{b}_1) = 3\cdot 2 + 0\cdot 2 + 3\cdot 1 = 6 + 0 + 3 = 9$.
> $\alpha = 9 / 9 = 1$.
> $\bar{b}_2 = \begin{pmatrix} 3 \\ 0 \\ 3 \end{pmatrix} - 1 \begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix} = \begin{pmatrix} 1 \\ -2 \\ 2 \end{pmatrix}$.
> *(Проверка: $(\bar{b}_1, \bar{b}_2) = 2 - 4 + 2 = 0$)*.
> Скалярный квадрат: $(\bar{b}_2, \bar{b}_2) = 1^2 + (-2)^2 + 2^2 = 1 + 4 + 4 = 9$.
> 
> 3) $\bar{b}_3 = \bar{a}_3 - \frac{(\bar{a}_3, \bar{b}_1)}{(\bar{b}_1, \bar{b}_1)} \bar{b}_1 - \frac{(\bar{a}_3, \bar{b}_2)}{(\bar{b}_2, \bar{b}_2)} \bar{b}_2$.
> $(\bar{a}_3, \bar{b}_1) = 6\cdot 2 + (-3)\cdot 2 + 3\cdot 1 = 12 - 6 + 3 = 9$. $\Rightarrow \beta_1 = 9/9 = 1$.
> $(\bar{a}_3, \bar{b}_2) = 6\cdot 1 + (-3)\cdot (-2) + 3\cdot 2 = 6 + 6 + 6 = 18$. $\Rightarrow \beta_2 = 18/9 = 2$.
> $\bar{b}_3 = \begin{pmatrix} 6 \\ -3 \\ 3 \end{pmatrix} - 1 \begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix} - 2 \begin{pmatrix} 1 \\ -2 \\ 2 \end{pmatrix} = \begin{pmatrix} 6 - 2 - 2 \\ -3 - 2 + 4 \\ 3 - 1 - 4 \end{pmatrix} = \begin{pmatrix} 2 \\ -1 \\ -2 \end{pmatrix}$.
> *(Проверка: $(\bar{b}_3, \bar{b}_1) = 4-2-2=0$, $(\bar{b}_3, \bar{b}_2) = 2+2-4=0$)*.
> Скалярный квадрат: $(\bar{b}_3, \bar{b}_3) = 2^2 + (-1)^2 + (-2)^2 = 4 + 1 + 4 = 9$.
> 
> **Шаг 2. Нормировка**
> Длины всех векторов одинаковые: $||\bar{b}_1|| = ||\bar{b}_2|| = ||\bar{b}_3|| = \sqrt{9} = 3$.
> Разделим каждый вектор на $3$ и получим ортонормированный базис $\{\bar{e}\}$:
> 
> **Ответ:** 
> $\bar{e}_1 = \begin{pmatrix} 2/3 \\ 2/3 \\ 1/3 \end{pmatrix}, \quad \bar{e}_2 = \begin{pmatrix} 1/3 \\ -2/3 \\ 2/3 \end{pmatrix}, \quad \bar{e}_3 = \begin{pmatrix} 2/3 \\ -1/3 \\ -2/3 \end{pmatrix}$.


