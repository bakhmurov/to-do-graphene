# to-do-graphene
##TO-DO backend with Flask, SQL Alchemy, Graphene
### Запуск приложения
- python setup.py
- python app.py

### Примеры мутаций
#### Создание карточки
``mutation {
  createCard(input: {
    cardName: "Название карточки"
  }){
    card {
      cardName
    }
  }
}``

#### Изменение карточки
``mutation {
  updateCard(input: {
    id: "id карточки"
    cardName: "Новое название"
  }){
    card {
      id
      cardName
    }
  }
}``

#### Удаление карточки
``mutation {
  deleteCard(id: номер id в базе) {
    status
  }
}``

#### Создание задачи для карточки
``mutation {
  createTask(input: {
    taskName: "Название задачи"
    cardId: "id карточки"
  }){
    task {
      taskName
      cardId
    }
  }
}``

#### Изменение задачи
``mutation {
  updateTask(input: {
    id: "id задачи"
    taskName: "Название задачи"
  }){
    task {
      id
      taskName
    }
  }
}``

#### Удаление задачи
``mutation {
  deleteTask(id: номер id в базе) {
    status
  }
}``

### Примеры запросов
#### Получение всех карточек
``{
  cardList
}``

#### Сортировка по имени
``{
orderByName
}``

#### Получение карточки со списком задач
``{
card(id:"id карточки") {
  id
  cardName
  created
  taskList {
    edges {
      node {
        id
        taskName
      }
    }
  }
}
}``

#### Поиск по названию карточки
``{
searchCardName(q: "запрос") {
  id
  cardName
}
}``

#### Получение списка задач
``{
taskList
}``

#### Получение задачи
``{
task(id: "id задачи") {
  id
  taskName
}
}``
