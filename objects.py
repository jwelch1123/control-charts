
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

    def __str__(self):
        return "My name's Carl!"



a = run_chart()
a.add_data([0,1,2],["1st","2nd","3rd"])
print(a)

b = run_chart()
b.add_data([0,"1",2],["1st","2nd","3rd"])
print(b)



#https://en.wikipedia.org/wiki/Nelson_rules
#https://en.wikipedia.org/wiki/Western_Electric_rules