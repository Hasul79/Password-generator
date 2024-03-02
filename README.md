# Password-generator

![password-generator](https://github.com/Hasul79/Password-generator/assets/95657084/0df1f6b2-8947-4282-bfc4-cfd57b583028)

<h2>Этот скрипт на Python создает случайные пароли заданной длины, используя библиотеку random и строки ASCII-символов.</h2>

<br/>

<ol>


  <li>import random и import string:</li>
  
<br/>

<ul>
  
  <li>random - библиотека Python для работы с случайными числами.</li>
  <li>string - модуль Python, предоставляющий набор стандартных строковых констант.</li>
  
</ul>

<li>def generate_password(length):</li>

<br/>

<ul>
  <li>Определение функции generate_password, которая принимает аргумент length (длина пароля).</li>
</ul>

<br/>

<li>random.choice(string.ascii_letters + string.digits + string.punctuation)</li>

<ul>
  <li>Генерация случайного символа, выбранного из строк string.ascii_letters (буквы ASCII), string.digits (цифры) и string.punctuation (специальные символы).</li>
</ul>

<br/>

<li>for _ in range(length):</li>

<ul>
  <li>Цикл, в котором генерируется каждый символ пароля указанной длины.</li>
</ul>

<br/>

<li>return ''.join(...)</li>

<ul>
  <li>Объединение сгенерированных символов в строку и возврат этой строки.</li>
</ul>

<br/>


<li>password_length = 12</li>

<ul>
  <li>Установка переменной password_length в значение 12 (может быть изменено на другую длину по вашему усмотрению).</li>
</ul>

<br/>

<li>print("Generated Password:", generate_password(password_length))</li>

<ul>
  <li>Вывод сгенерированного пароля на экран.</li>
</ul>

<br/>

</ol>

<br/>

# Таким образом, при запуске скрипта он создаст и выведет случайный пароль указанной длины, используя буквы, цифры и специальные символы.

![Screenshot 2024-02-29 195108](https://github.com/Hasul79/Password-generator/assets/95657084/c2ae2884-8704-466d-b224-0d81727867e6)



![Screenshot 2024-03-02 234504](https://github.com/Hasul79/Password-generator/assets/95657084/b1557b3a-e22b-4b95-badd-04a833b18350)

# Author: Hasmik Minasyan 02.03.2024
