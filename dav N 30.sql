-- 1. დაწერეთ SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ მხოლოდ customerName, phone, city, country ველებს. 
select customerName, phone, city, country
from it_step.customers
LIMIT 10;

-- 2. დაწერეთ SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ ყველა იმ ჩანაწერს რომლის ფოსტის კოდი მეტია 1370ზე ან salesRepEmployeeNumber მეტია 150 
select * from it_step.customers
where  postalCode > 1370 or salesRepEmployeeNumber > 150
LIMIT 10;

-- 3. დაწერეთ SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ ისეთ ჩანაწერს, რომელშიც customerName შეიცავს 'Mini' ტექსტს
select * from it_step.customers
where customerName like '%Mini%'
limit 10;

-- 4. დაწერეთ SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ მონაცემებს, რომელსაც აქვს state 'CA' ან 'NY' 
select * from it_step.customers
where state = 'CA' or state = 'NY'
LIMIT 10;

select * from it_step.customers
where state in ('CA','NY')
LIMIT 10;

-- 5. დაწერეთ SQL ბრძანება, რომლის საშუალებითაც customers ცხრილიდან წამოიღებთ მონცემებს, რომელსაც აქვს creditLimit 10000-ზე მეტი 
select * from it_step.customers
where creditLimit > 10000
LIMIT 10;