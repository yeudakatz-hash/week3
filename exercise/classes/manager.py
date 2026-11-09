from .employee import Employee



class Manager(Employee):
    def manage(self, team_size):
        return self.name + "manages" + str(team_size)
