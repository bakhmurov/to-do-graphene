from graphene_sqlalchemy import SQLAlchemyObjectType
from database.base import db_session
from database.model_task import ModelTask
import graphene
import utils


class TaskAttribute:
    task_name = graphene.String(description="Название задачи")
    card_id = graphene.ID(description="Id карточки товара")


class Task(SQLAlchemyObjectType):
    """Task node."""

    class Meta:
        model = ModelTask
        interfaces = (graphene.relay.Node,)


class CreateTaskInput(graphene.InputObjectType, TaskAttribute):
    """Аргументы для создания задачи"""
    pass


class CreateTask(graphene.Mutation):
    """Создание задачи"""
    task = graphene.Field(lambda: Task, description="Задача создается этой мутацией")

    class Arguments:
        input = CreateTaskInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)

        task = ModelTask(**data)
        db_session.add(task)
        db_session.commit()

        return CreateTask(task=task)


class UpdateTaskInput(graphene.InputObjectType, TaskAttribute):
    """Аргументы для изменения задачи"""
    id = graphene.ID(required=True, description="Id задачи")


class UpdateTask(graphene.Mutation):
    """Изменение задачи"""
    task = graphene.Field(lambda: Task, description="Задача изменяется этой мутацией")

    class Arguments:
        input = UpdateTaskInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)

        task = db_session.query(ModelTask).filter_by(id=data['id'])
        task.update(data)
        db_session.commit()
        task = db_session.query(ModelTask).filter_by(id=data['id']).first()

        return UpdateTask(task=task)


class DeleteTask(graphene.Mutation):
    """Удаление задачи"""
    card = graphene.Field(lambda: Task, description="Задача удаляется этой мутацией")

    class Arguments:
        id = graphene.ID(required=True)

    status = graphene.String()

    def mutate(self, info, **kwargs):
        card = db_session.query(ModelTask).filter_by(id=kwargs.get('id')).first()

        db_session.delete(card)
        db_session.commit()
        return DeleteTask(status="OK")
