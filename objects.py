
class run_chart:

    def __init__(self) -> None:
        pass

    data     = []
    labels   = []
    run_mean = int
    grouping = list
    
    def _check_labels(self, new_labels, data_length):
        # uploading new data -> labels empty
        # appending data (no provided labels) -> numbers with increment
        # appending data (provided labels) -> return provided labels if correct length

        if isinstance(new_labels, type(None)):
            new_labels = list(range(len(self.labels), len(self.labels + data_length)))
        else:
            if data_length != len(new_labels):
                raise ValueError("Provided labels should be the same length as provided data.")
        return new_labels

    def _update_attributes(self):
        self.run_mean = sum(self.data)/len(self.data)

        return self


    def add_data(self, new_data, new_labels = None):
        # Check data can be coerced to numeric
        try:
            sum(new_data)
        except:
            raise TypeError("Data contains non-numeric types.")

        #Append new data and labels to existing data.    
        self.data.extend(new_data) 
        self.labels.extend(self._check_labels(new_labels, len(new_data)))
        self._update_attributes()
        return self

    def from_csv(self, data_col, label_col, grouping_col):
        # parse data from csv into a run_chart object
        pass

    def from_dataframe(self, data_col, label_col, grouping_col):
        # parse data from dataframe object into a run_chart object
        pass

    def to_csv():
        # converts csv to dataframe and parses object. 
        # not suggested unless you know what the columns contain
        pass

    def to_dataframe():
        pass


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

    def _update_attributes(self):
        self.run_mean = sum(self.data)/len(self.data)
        
        # make modifiable
        #self.Upper_Ctrl_Lmt = 
        #self.Lower_Ctrl_Lmt = 
        return self

    def __str__(self):
        return f"\nControl Chart Object \nLabels: {self.labels} \nValues: {self.data} \nRun Average: {self.run_mean}\n"
        


print("Regular addition with update")
a = run_chart()
a.add_data([0,1,2],["1st","2nd","3rd"])
print(a)
a.add_data([3,4,5], ["4th","5th","6th"])
print(a)

print("\n")
print("Fail data type")
b = run_chart()
b.add_data([0,"1",2],["1st","2nd","3rd"])
print(b)

#c = control_chart()
#c.add_data([0,1,2],["1st","2nd","3rd"])
#c.append([5,8,20])
#print(c)



#https://en.wikipedia.org/wiki/Nelson_rules
#https://en.wikipedia.org/wiki/Western_Electric_rules