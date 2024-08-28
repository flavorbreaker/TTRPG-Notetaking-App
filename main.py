import pymongo

class Campaign():
    def __init__(self, title, system) -> None:
        self.title = title
        self.system = system

campaigns = {}      # Empty dict to store Campaign objects

def main():

    action = select_action().upper()
    if action == 'C':
        campaign_menu()

    elif action == 'Q':
        exit()

def select_action():
    return input("""Please select your action:
        C - Campaigns
        Q - Quit Program
Selection: """)

def campaign_menu():
    return input(
"""Please input the name of the campaign you'd like to open, 
or type \"new\" to create a new campaign notebook: """)

         
def new_campaign():
    new_title = input("Campaign name: ")
    new_system = input("Campaign system: ")

    campaign = Campaign(new_title, new_system)

    campaigns.update({new_title : campaign})

campaign_menu()