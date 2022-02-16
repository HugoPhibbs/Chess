class UIShell:

    def __init__(self, logic : 'UILogic'):
        self.logic = 'UILogic'

    @property
    def logic(self):
        return self.__logic

    @logic.setter
    def logic(self, logic):
        self.__logic = logic
