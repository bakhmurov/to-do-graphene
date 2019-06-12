from sqlalchemy import func
from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
import schema_task
from database.model_task import ModelTask
import schema_card
from database.model_card import ModelCard


class Query(graphene.ObjectType):
    """Ноды которые могут быть запрошены по API"""
    node = graphene.relay.Node.Field()

    # Tasks
    task = graphene.relay.Node.Field(schema_task.Task, description="Задача")
    taskList = SQLAlchemyConnectionField(schema_task.Task, description="Список задач")


    # Cards
    card = graphene.relay.Node.Field(schema_card.Card, description="Карточка")
    cardList = SQLAlchemyConnectionField(schema_card.Card, description="Список карточек")
    search_card_name = graphene.Field(lambda: graphene.List(schema_card.Card), q=graphene.String(),
                                      description="Поиск по названию карточки")
    order_by_name = graphene.Field(lambda: graphene.List(schema_card.Card),
                                   description="Сортировка карточек по названию")
    order_by_tasks = SQLAlchemyConnectionField(schema_card.Card,
                                               description="Сортировка карточек по количеству задач")

    def resolve_search_card_name(self, info, **kwargs):
        query = schema_card.Card.get_query(info)
        q = kwargs.get("q")
        cards = query.filter(ModelCard.card_name.contains(q)).all()
        return cards

    def resolve_order_by_name(self, info, **kwargs):
        query = schema_card.Card.get_query(info)
        cards = query.order_by(ModelCard.card_name)
        return cards

    def resolve_order_by_tasks(self, info, **kwargs):
        query = schema_card.Card.get_query(info)
        cards = query.join(ModelTask).group_by(ModelCard.card_name).order_by(func.count(ModelTask.card_id).desc())
        return cards


class Mutation(graphene.ObjectType):
    """
    Мутации которые могут быть выполнены по API.
    """
    # Card mutation
    createCard = schema_card.CreateCard.Field()
    updateCard = schema_card.UpdateCard.Field()
    deleteCard = schema_card.DeleteCard.Field()

    # Task mutations
    createTask = schema_task.CreateTask.Field()
    updateTask = schema_task.UpdateTask.Field()
    deleteTask = schema_task.DeleteTask.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
