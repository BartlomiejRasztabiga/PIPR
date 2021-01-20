import argparse
import json
from datetime import datetime

import matplotlib.pyplot as plt


class Plotter:

    def parse_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--timestamp', metavar='TIMESTAMP', type=str, nargs='?', default='timestamp')
        parser.add_argument('--value', metavar='VALUE', type=str, nargs='*')
        parser.add_argument('--from', metavar='FROM', type=str, nargs='?')
        parser.add_argument('--to', metavar='TO', type=str, nargs='?')
        parser.add_argument('data', metavar='DATA_FILE', type=argparse.FileType('r'), nargs=1)

        args = parser.parse_args()
        arguments = vars(args)

        return arguments

    def extract_time(self, jsn, timestamp_field_name):
        try:
            return datetime.fromisoformat(jsn[timestamp_field_name])
        except KeyError:
            return 0

    def read_file_to_json(self, file_name):
        with open(file_name, 'r') as f:
            return json.load(f)

    def prepare_data_for_plotting(self, data, from_date, to_date, timestamp_field_name):
        data.sort(key=lambda x: self.extract_time(x, timestamp_field_name))

        if from_date:
            from_date = datetime.fromisoformat(from_date)
            data = list(filter(lambda jsn: self.extract_time(jsn, timestamp_field_name) >= from_date, data))

        if to_date:
            to_date = datetime.fromisoformat(to_date)
            data = list(filter(lambda jsn: self.extract_time(jsn, timestamp_field_name) <= to_date, data))

        return data

    def run(self):
        arguments = self.parse_arguments()

        value_fields_names = arguments['value']
        if not value_fields_names:
            value_fields_names = ['value']

        timestamp_field_name = arguments['timestamp']
        from_date = arguments['from']
        to_date = arguments['to']

        input_file = arguments['data']
        file_name = input_file[0].name

        data = self.read_file_to_json(file_name)
        data = self.prepare_data_for_plotting(data, from_date, to_date, timestamp_field_name)

        x = []
        ys = []

        for value in data:
            x.append(value["timestamp"])

        for value_field_name in value_fields_names:
            y = []
            for value in data:
                try:
                    y.append(value[value_field_name])
                except KeyError:
                    y.append(None)
            ys.append(y)

        for i in range(len(value_fields_names)):
            y = ys[i]
            label = value_fields_names[i]
            plt.plot(x, y, label=label)

        plt.legend(loc='upper right')
        plt.xticks(rotation=90)
        plt.show()


def main():
    plotter = Plotter()
    plotter.run()


if __name__ == '__main__':
    main()
