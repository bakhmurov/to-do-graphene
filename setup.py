from ast import literal_eval
from database.model_task import ModelTask
from database.model_card import ModelCard
from database import base
import logging
import sys


log = logging.getLogger(__name__)
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


if __name__ == '__main__':
    log.info('Создаем базу данных {}'.format(base.db_name))
    base.Base.metadata.create_all(base.engine)

    log.info('Заполняем карточками')
    with open('database/data/cards.json', 'r') as file:
        data = literal_eval(file.read())
        for record in data:
            card = ModelCard(**record)
            base.db_session.add(card)
        base.db_session.commit()

    log.info('Заполняем задачами')
    with open('database/data/tasks.json', 'r') as file:
        data = literal_eval(file.read())
        for record in data:
            task = ModelTask(**record)
            base.db_session.add(task)
        base.db_session.commit()
