class Dialysis:

    def analyse(self, threshold, blood_concentrations):
        if not blood_concentrations:
            return 0 
        
        current = blood_concentrations[0]
        threshold_and_negative_errors = current>=threshold + current<0
        growth_errors=0
        for i,c in enumerate(blood_concentrations[1:]):
            current = c 
            previous = blood_concentrations[i]
            threshold_and_negative_errors+= (previous < threshold) and (current>=threshold or current<0)
            rate = current - previous
            next_value = current+rate/2
            growth_errors += (0<=current<threshold) and (next_value>= threshold or next_value<0)
            
        errors = threshold_and_negative_errors+growth_errors
        return errors
