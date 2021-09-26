<p align="center">
    <h1 align="center">ВАЖНО!!!</h1>
    </p>
<p>Не указывать название команды, не указывать наименование хакатона и название проекта.</p>
<p>Ниже приведено то что должно быть в вашем README </p>

<h4>Реализованная функциональность</h4>
<ul>
    <li>Функционал Система ролей;</li>
    <li>Функционал Чат-система;</li>
    <li>Функционал Система аунтификации;</li>
</ul> 
<h4>Особенность проекта в следующем:</h4>
<ul>
 <li>Грантовая система;</li>
 <li>Практическая система;</li>  
 </ul>
<h4>Основной стек технологий:</h4>
<ul>
    <li>Django,Python.</li>
	<li>HTML, CSS, JavaScript</li>
	<li>SQLLite</li>
	<li>Websokets.</li>
	<li>Git, Github.</li>
  
 </ul>
<h4>Демо</h4>
<p>Реквизиты тестового пользователя: email: <b>admin</b>, пароль: <b>admin</b></p>




СРЕДА ЗАПУСКА
------------
1) развертывание сервиса производится в локальном окружении virtualenv);
2) требуется установленная СУБД SQLLITE;
4) требуется установленный фреймворк Django, Pillow, pyth для работы с;


УСТАНОВКА
------------
### Установка пакета name

Выполните 
~~~
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install name1
sudo apt-get install mariadb-client mariadb-server
git clone https://github.com/Sinclear/default_readme
cd default_readme
...
~~~
### База данных

Необходимо создать пустую базу данных, а подключение к базе прописать в конфигурационный файл сервиса по адресу: папка_сервиса/...
~~~
sudo systemctl restart mariadb
sudo mysql_secure_installation
mysql -u root -p
mypassword
CREATE DATABASE mynewdb;
quit
~~~
### Выполнение миграций

Для заполнения базы данных системной информацией выполните в корневой папке сервиса: 
~~~
mysql -u root -p -f mynewdb < папка_сервиса/...
mypassword
~~~
и согласитесь с запросом

### Установка зависимостей проекта

Установка зависимостей осуществляется с помощью [Composer](http://getcomposer.org/). Если у вас его нет вы можете установить его по инструкции
на [getcomposer.org](http://getcomposer.org/doc/00-intro.md#installation-nix).

После этого выполнить команду в директории проекта:

~~~
composer install
~~~

РАЗРАБОТЧИКИ

<h4>Иванов Иван fullstack https://t.me/test@name1 </h4>


