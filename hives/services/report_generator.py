from SmartBeeHive.settings import BASE_DIR


class ReportHive:
    def __init__(self, hive_id, aver_temp, aver_humid, change_weight, start_date, end_date):
        self.hive_id = hive_id
        self.aver_temp = aver_temp
        self.aver_humid = aver_humid
        self.change_weight = change_weight
        self.start_date = start_date
        self.end_date = end_date

        self.generate_report_txt()

    def generate_report_txt(self):
        with open(f'{BASE_DIR}/download/reports/{self.end_date}_{self.hive_id}.txt', 'w+') as file:
            file.write(
                f"Номер улья: {self.hive_id} \n Начало: {self.start_date} \n "
                f"Конец: {self.end_date} \n Средняя температура: {self.aver_temp} \n "
                f"Средняя влажность воздуха: {self.aver_humid} \n"
            )

            print("Generator worked")


def generteReport_pdf(self):
    pass
