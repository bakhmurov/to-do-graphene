# to-do-graphene
TO-DO backend with Flask, SQL Alchemy, Graphene

Примеры мутаций:
Создание карточки
``mutation {
  createCard(input: {
    cardName: "Название карточки"
  }){
    card {
      cardName
    }
  }
}``

Изменение карточки
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

Создание задачи для карточки
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

Изменение задачи
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
