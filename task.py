class Manager:
    def __init__(self, name, hours, id):
        self.name = name
        self.hours = hours
        self.id = id
        self.salary = 45000
        self.productivity = round(self.hours/40*100, 1)
    def manager_salary(self):
        print(f'{self.name}\'s salary (id - {self.id}): {self.salary}')
    def manager_productivity(self):
        print(f'percent of productivity of {self.name}: {self.productivity}')

class Secretary:
    def __init__(self, name, hours, id):
        self.name = name
        self.hours = hours
        self.id = id
        self.salary = 20000
        self.productivity = round(self.hours/40*100, 1)
    def secretary_salary(self):
        print(f'{self.name}\'s salary (id - {self.id}): {self.salary}')
    def secretary_productivity(self):
        print(f'percent of productivity of {self.name}: {self.productivity}')

class Salesperson:
    def __init__(self, name, hours, id, sales):
        self.name = name
        self.hours = hours
        self.id = id
        self.sales = sales
        self.salary = 20000 + 50*self.sales
        self.productivity = round(self.hours/40*100, 1)
    def salesperson_salary(self):
        print(f'{self.name}\'s salary (id - {self.id}): {self.salary}')
    def salesperson_productivity(self):
        print(f'percent of productivity of {self.name}: {self.productivity}')

class ShopWorker:
    def __init__(self, name, hours, id):
        self.name = name
        self.hours = hours
        self.id = id
        self.salary = 0 + self.hours*100
        self.productivity = round(self.hours/40*100, 1)
    def worker_salary(self):
        print(f'{self.name}\'s salary (id - {self.id}): {self.salary}')
    def shopworker_productivity(self):
        print(f'percent of productivity of {self.name}: {self.productivity}')

class ReplacementSecretary:
    def __init__(self, name, hours, id):
        self.name = name
        self.hours = hours
        self.id = id
        self.salary = 0 + self.hours*100
        self.productivity = round(self.hours/40*100, 1)
    def rpl_secretary_salary(self):
        print(f'{self.name}\'s salary (id - {self.id}): {self.salary}')
    def rpl_secretary_productivity(self):
        print(f'percent of productivity of {self.name}: {self.productivity}')

class Result():
    def __init__(self, summ_of_salaries, most_productive):
        self.summ_of_salaries = summ_of_salaries
        self.most_productive = most_productive
    def summ(self):
        total = 0
        for i in self.summ_of_salaries.values():
            total += i[0]
        print(f'total amount: {total}')
        print(f'salaries of all employees: {self.summ_of_salaries}')
        for key, value in self.most_productive.items():
            if value == max(self.most_productive.values()):
                print(f'the most productive employee - {key}: {value}')
            elif value == min(self.most_productive.values()):
                print(f'most unproductive employee - {key}: {value}')
        print(f'percentage of productivity of all employees: {self.most_productive}')

manager = Manager('Барсбек Канаткулов', 18, 1)

secretary = Secretary('Алымкул Тилекбаев', 38, 2)
rpl_secretary = Secretary('Жанар Рыскулов', 33, 6)

salesperson = Salesperson('Айпери Шалымбекова', 38, 3, 20)

worker1 = ShopWorker('Бакыт Рустамов', 25, 4)
worker2 = ShopWorker('Алтынай Ширинбаева', 40, 5)

result = Result(summ_of_salaries = {manager.name: [manager.salary, manager.id], secretary.name: [secretary.salary, secretary.id], rpl_secretary.name: [rpl_secretary.salary, rpl_secretary.id], salesperson.name: [salesperson.salary, salesperson.id], worker1.name: [worker1.salary, worker1.id], worker2.name: [worker2.salary, worker2.id]}, most_productive={manager.name: manager.productivity, secretary.name: secretary.productivity, rpl_secretary.name: rpl_secretary.productivity, salesperson.name: salesperson.productivity, worker1.name: worker1.productivity, worker2.name: worker2.productivity})
result.summ()

#также через вызов функции одного из экземпляров можно получить его зп
