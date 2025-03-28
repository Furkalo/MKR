Для вирішення задачі написати Python-скрипт.
Умову задачі надає викладач безпосередньо під час проведення модульного контролю.

Під час вирішення задачі необхідно ОБОВ'ЯЗКОВО дотримуватися основних принципів Continuous Integration:
1. Користуватися системою контролю версій Git:
 - додати проєкт під версійний контроль;
 - згенерувати файл .gitignore;
 - для кожної функції / методу класу - окремий коміт.
2. Для розроблених функцій написати unit-тести за допомогою бібліотеки pytest.
Для створення unit-тестів необхідно використати такі інструменти pytest: фікстури (fixtures); параметризація (parametrization).
3. За допомогою pytest-html згенерувати звіт по виконанню unit-тестів.
4. Додати файл requirements.txt із всіма залежностями проєкту.
5. Створити на GitHub віддалений публічний репозиторій, в який залити виконану роботу (коміти). У віддаленому репозиторію МАЄ ЗБЕРІГАТИСЯ вся історія комітів.
6. Додати налаштування GithubAction для автоматичного запуску тестів у віддаленому репозиторію та перевірки коду на відповідність стандарту PEP8.


На перевірку необхідно в classroom-і до завдання Middle Test #01 прикріпити посилання на Ваш GitHub репозиторій.
Останній коміт має бути зроблений не пізніше відведеного часу на виконання роботи.
Оцінювання (максимум 10 б.):
- вирішення задачі - максимум 4 б.
- використання Git - максимум 2 б.
- наявність unit-тестів - максимум 3 б.
- використання GithubAction - максимум 1 б.


Варіант 1 +

Напишіть Python-скрипт, який зчитує вміст файлу з розширенням ".txt" та повертає кількість слів і речень у цьому файлі.
Символи, які закінсують файл: ".", "!", "?", "..."
Символи-розділювачі: ",", "пробіл", ":", ";"
 
 
