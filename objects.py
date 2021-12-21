
class run_chart:

    data     = []
    labels   = []
    run_mean = int
    
    def add_data(self, run_data, labels = None):

        # Check data can be coerced to numeric
        try:
            sum(run_data)
        except:
            raise TypeError("Run data contains non-numeric types.")
            
        # Assign labels if missing, check length is equivalent to run_data
        if isinstance(labels, type(None)):
            labels = range(1,len(run_data))
        else:
            if len(run_data) != len(labels):
                raise ValueError("Labels should be the same length as run_data.")

        self.data = run_data
        self.labels = labels
        self.run_mean = sum(run_data)/len(run_data)
        
        return self

    def from_csv():
        # parse data from csv into a run_chart object
        pass

    def from_dataframe():
        # parse data from dataframe object into a run_chart object
        pass

    def append(self, new_data, new_labels = None):
        self.data.append(new_data) 
        self.labels.append(new_labels)
        return self


    def _check_data(*args):
        # args is dictionary with "value_name" : value
        # check that value meets type requirements of value_name
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
print(c)



#https://en.wikipedia.org/wiki/Nelson_rules
#https://en.wikipedia.org/wiki/Western_Electric_rules