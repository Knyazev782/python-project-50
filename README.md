### Hexlet tests and linter status:
[![Actions Status](https://github.com/Knyazev782/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Knyazev782/python-project-50/actions)
[![Test Coverage](https://api.codeclimate.com/v1/badges/af5d452e8a4a4d9ccbd6/test_coverage)](https://codeclimate.com/github/Knyazev782/python-project-50/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/af5d452e8a4a4d9ccbd6/maintainability)](https://codeclimate.com/github/Knyazev782/python-project-50/maintainability)

"Вычислитель отличий"

Вычислитель отличий - это мой второй учебный проект в рамках курса на Hexlet.
Это утилита командной строки, которая сравнивает два файла конфигурации (JSON или YAML) и выводит различия между ними в удобном формате.

Основыне возможности:

- Сравнение файлов JSON и YAML.

- Поддержка вложенных структур.

- Вывод различий в трёх форматах:

Stylish - вывод установленный по умолчанию, читаемый формат с отступами и выделением символами "+" при схожести инормации или "-" при различии.

Plain - простой текстовый формат.

Json - вывод в формате JSON.

Использование

Запуск из командной строки:

"gendiff --format <указать нужный формат> file1 file2"
