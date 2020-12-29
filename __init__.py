from mycroft import MycroftSkill, intent_file_handler


class Winston(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('winston.about.intent')
    def winston_about(self, message):
        self.speak_dialog('winston.about')

    def stop(self):
        pass


def create_skill():
    return Winston()
