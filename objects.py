
class run_chart:

    data     = list
    labels   = list
    run_mean = int
    Grouping       = list
    
    def _check_labels(self, labels,data_length, append = False):
        if isinstance(labels, type(None)):
            labels = list(range(1,data_length))
            if append:
                labels = [x+ data_length for x in labels]
        else:
            if data_length != len(labels):
                raise ValueError("Labels should be the same length as run_data.")
        return labels


    def add_data(self, run_data, labels = None):
        # Check data can be coerced to numeric
        try:
            sum(run_data)
        except:
            raise TypeError("Data contains non-numeric types.")
            
        self.data = run_data
        self.labels = self._check_labels(labels, len(run_data))
        self.run_mean = sum(run_data)/len(run_data)
        
        return self

    def from_csv(self, data_col, label_col, grouping_col):
        # parse data from csv into a run_chart object
        pass

    def from_dataframe(self, data_col, label_col, grouping_col):
        # parse data from dataframe object into a run_chart object
        pass

    def to_csv():
        pass

    def to_dataframe():
        pass

    def append(self, new_data, new_labels = None):
        self.data.extend(new_data) 
        self.labels.extend(self._check_labels(new_labels, len(new_data), append=True))
        self.run_mean = sum(self.data)/len(self.data)
        return self


    def _check_data(*args):
        # args is dictionary with "value_name" : value
        # check that value meets type requirements of value_name
        validation = {"Data": sum}
        pass

    

    

    def __str__(self):
        return f"\nRun Chart Object \nLabels: {self.labels} \nValues: {self.data} \nRun Average: {self.run_mean}\n"


class control_chart(run_chart):
    
    Upper_Ctrl_Lmt = int
    Lower_Ctrl_Lmt = int 

    

    def __str__(self):
        return f"\nControl Chart Object \nLabels: {self.labels} \nValues: {self.data} \nRun Average: {self.run_mean}\n"
        



a = run_chart()
a.add_data([0,1,2],["1st","2nd","3rd"])
print(a)

#b = run_chart()
#b.add_data([0,"1",2],["1st","2nd","3rd"])
#print(b)

c = control_chart()
c.add_data([0,1,2],["1st","2nd","3rd"])
c.append([5,8,20])
print(c)



#https://en.wikipedia.org/wiki/Nelson_rules
#https://en.wikipedia.org/wiki/Western_Electric_rules