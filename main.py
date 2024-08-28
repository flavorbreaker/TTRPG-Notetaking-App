class Campaign():
    def __init__(self, title, system) -> None:
        self.title = title
        self.system = system

campaigns = {}      # Empty dict to store Campaign objects

def new_campaign():
    new_title = input("Campaign name: ")
    new_system = input("Campaign system: ")

    campaign = Campaign(new_title, new_system)

    campaigns.update({new_title : campaign})

new_campaign()