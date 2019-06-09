from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
import schema_card
from database.model_card import ModelCard
import schema_task


class Query(graphene.ObjectType):
    """Ноды которые могут быть запрошены по API"""
    node = graphene.relay.Node.Field()

    # Cards
    card = graphene.relay.Node.Field(schema_card.Card)
    cardList = SQLAlchemyConnectionField(schema_card.Card, description="Список карточек")
    search_card_name = graphene.Field(lambda: graphene.List(schema_card.Card), q=graphene.String(),
                                      description="Поиск по названию карточки")
    order_by_name = graphene.Field(lambda: graphene.List(schema_card.Card),
                                   description="Сортировка карточек по названию")
    order_by_tasks = graphene.Field(lambda: graphene.List(schema_card.Card),
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

    def resolve_order_by_task(self, info, **kwargs):
        query = schema_card.Card.get_query(info)
        cards = query.order_by(ModelCard.taskList).count()
        return cards


    # Tasks
    task = graphene.relay.Node.Field(schema_task.Task)
    taskList = SQLAlchemyConnectionField(schema_task.Task)


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
