import pandas as pd
class Solution:

    def remove_tags(self, input_string):
        # Your code goes here
        table_html = pd.read_html('https://www.w3schools.com/TAGS/default.asp')
        table_html[0]["Tag"].to_list()
        html_closing = [x[0]+"/"+x[1:] for x in table_html]
        html = table_html+html_closing
        for t in html:
            input_string = input_string.replace(t,"")
        return input_string