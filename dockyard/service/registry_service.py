from abc import ABC, abstractmethod

from ..dependency_injection import di
from ..models.paths.name_path import NamePath

class RegistryService(ABC):

    @abstractmethod
    def get_tags_for_repository_by_name(self, name_path: NamePath):
        raise NotImplementedError()

    pass

class RegistryServiceImpl(RegistryService):
    pass

di.register_scoped(RegistryService, RegistryServiceImpl)