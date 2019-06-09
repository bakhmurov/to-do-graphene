from datetime import datetime
from graphene_sqlalchemy import SQLAlchemyObjectType
from database.base import db_session
from database.model_card import ModelCard
import graphene
import utils


class CardAttribute:
    card_name = graphene.String(description="Название карточки")
    created = graphene.String(description="Дата создания карточки")


class Card(SQLAlchemyObjectType):
    """Card node."""

    class Meta:
        model = ModelCard
        interfaces = (graphene.relay.Node,)


class CreateCardInput(graphene.InputObjectType, CardAttribute):
    """Аргументы для создания карточки"""
    pass


class CreateCard(graphene.Mutation):
    """Создание карточки"""
    card = graphene.Field(lambda: Card, description="Карточка создается этой мутацией")

    class Arguments:
        input = CreateCardInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)
        data['created'] = datetime.utcnow()

        card = ModelCard(**data)
        db_session.add(card)
        db_session.commit()

        return CreateCard(card=card)


class UpdateCardInput(graphene.InputObjectType, CardAttribute):
    """Аргументы для изменения карточки"""
    id = graphene.ID(required=True, description="Global Id карточки")


class UpdateCard(graphene.Mutation):
    """Изменение карточки"""
    card = graphene.Field(lambda: Card, description="Карточка изменяется этой мутацией")

    class Arguments:
        input = UpdateCardInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)

        card = db_session.query(ModelCard).filter_by(id=data['id'])
        # card = db_session.query(ModelCard).filter_by(id=data['id']).first()
        card.update(data)
        db_session.commit()
        card = db_session.query(ModelCard).filter_by(id=data['id']).first()

        return UpdateCard(card=card)


class DeleteCard(graphene.Mutation):
    """Удаление карточки"""
    card = graphene.Field(lambda: Card, description="Карточка удаляется этой мутацией")

    class Arguments:
        id = graphene.ID(required=True)

    status = graphene.String()

    def mutate(self, info, **kwargs):
        card = db_session.query(ModelCard).filter_by(id=kwargs.get('id')).first()

        db_session.delete(card)
        db_session.commit()
        return DeleteCard(status="OK")
