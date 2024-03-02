# Password-generator

![password-generator](https://github.com/Hasul79/Password-generator/assets/95657084/0df1f6b2-8947-4282-bfc4-cfd57b583028)

<h2>Этот скрипт на Python создает случайные пароли заданной длины, используя библиотеку random и строки ASCII-символов.</h2>

<h3>ASCII (American Standard Code for Information Interchange) </h3>
<p> это стандартный набор символов, представленных числовыми кодами. ASCII-символы включают в себя</p>
<nr/>
<ul list-style-type: "&#10003;">
  
  <li>Буквы латинского алфавита:</li>
  
</ul>

![Screenshot 2024-03-02 234504](https://github.com/Hasul79/Password-generator/assets/95657084/b1557b3a-e22b-4b95-badd-04a833b18350)

<br/>

<ol>

  <li>import random и import string:</li>
  
<br/>

<ul>
  
  <li>random - библиотека Python для работы с случайными числами.</li>
  
  <li>string - модуль Python, предоставляющий набор стандартных строковых констант.</li>
  
</ul>
<br/>

<li>def generate_password(length)`</li>

<br/>

<ul>
  <li>Определение функции generate_password, которая принимает аргумент length (длина пароля).</li>
</ul>

<br/>

<li>random.choice(string.ascii_letters + string.digits + string.punctuation)`</li>

<br/>
<ul>
  <li>Генерация случайного символа, выбранного из строк string.ascii_letters (буквы ASCII), string.digits (цифры) и string.punctuation (специальные символы).</li>
</ul>

<br/>

<li>for _ in range(length)`</li>
<br/>
<ul>
  <li>Цикл, в котором генерируется каждый символ пароля указанной длины.</li>
</ul>

<br/>

<li>return ''.join(...)`</li>
<br/>
<ul>
  <li>Объединение сгенерированных символов в строку и возврат этой строки.</li>
</ul>

<br/>


<li>password_length = 12`</li>
<br/>
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


![Screenshot 2024-03-02 230621](https://github.com/Hasul79/Password-generator/assets/95657084/be11bdfb-02ee-4981-bcf8-db23b3e6ddc4)




# Author: Hasmik Minasyan 02.03.2024
