import logging


class KeywordFilter(logging.Filter):

    def __init__(self, keywords):
        super(KeywordFilter, self).__init__()
        self._keywords = keywords

    def filter(self, record):
        if isinstance(record.args, dict):
            record.args = record.args.copy()
            for k in record.args.keys():
                if k in self._keywords:
                    record.args[k] = '***censored***'

        return True