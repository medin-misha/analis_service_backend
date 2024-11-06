# Backend
Этот проект создан для того что бы у меня была статистика данных своего здоровья. Цель этого бекенда заключаеться в заемодействе с базой данных с помощью sqlalchemy и отдавать данные через FastAPI. Фишка проекта заключаеться в том что бы загружать и хранить в нём результаты анализов, допустим тестостерона и когда их соберёться достаточно много получить чёткий график который показывает что когда у тебя было и куда идёт. Это должно очень сильно помагать врачам но я пока не проверял.
## как запустить это всё дело?
После копирования репозитория заходишь в него после скачиваешь командой все зависимости: 
`pip install -r requirements.txt`. Далее можешь воспользоваться уже созданой базой данных, но лучше создать свою. База данных по умолчанию находиться в `app/database` её можно удалить и создать новую прописав в `app/` `alembic upgrade head`. Далее в том же `app/` пишешь: `uvicorn main:app` всё. Документация swagger по `/docs`
## как тестировать?
В app/core/config.py нужно разкоментировать строчку с вызовом функции:
```settings.test_mode()```
после в tests/ запускаешь pytest на нужный тебе файл, и тестируешь
## как заупстить через докер?
Очень и очень просто. `docker-compose up --build` Незабывайте переодически копировать базу данных которая находиться в app/database

C платонической любовью MISHA