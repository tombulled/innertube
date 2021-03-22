import abc

from typing import \
(
    Dict,
    Any,
)

class Object(object, metaclass = abc.ABCMeta):
    @abc.abstractmethod
    def __repr__(self, **fields: Dict[str, Any]) -> str:
        return '{class_name}({fields})'.format \
        (
            class_name = self.__class__.__name__,
            fields     = ', '.join \
            (
                f'{key}={value!r}'
                for key, value in fields.items()
            )
        )
