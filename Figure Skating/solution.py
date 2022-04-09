class FigureSkating:

    def evaluate_score_cards(self, scorecards, base_scores):
        # Your code goes here
        program_cat = 4
        technical = len(base_scores)
        categories = program_cat + technical
        num_scorecards = [list(map(lambda x: float(x), score.split(","))) for score in scorecards if
                          len(score.split(",")) == categories]
        if not num_scorecards:
            return 5 * program_cat + sum(base_scores)  # give a 5 to each program category and add base score

        tech_scores = [scores[:technical] for scores in num_scorecards]  # grouped by judge
        pro_scores = [scores[technical:] for scores in num_scorecards]

        tech_element_scores = [[tech_scores[j][s] for j in range(len(tech_scores)) if -5 <= tech_scores[j][s] <= 5]
                               for s in range(technical)]  # grouped by element
        pro_element_scores = [[pro_scores[j][s] for j in range(len(pro_scores)) if 0.25 <= pro_scores[j][s] <= 10]
                              for s in range(program_cat)]

        tech_element_scores = [list(map(lambda y: round(y * 4) / 4, self.cut(sorted(x))))
                               for x in tech_element_scores]  # this rounds up
        pro_element_scores = [list(map(lambda y: round(y * 4) / 4, self.cut(sorted(x)))) for x in
                              pro_element_scores]

        tech_score = sum(self.mean(tech_element_scores[i], 0) + base_scores[i] for i in range(technical))
        pro_score = sum(self.mean(pro_element_scores[i], 5) for i in range(program_cat))

        total_score = tech_score + pro_score
        return round(total_score, 4)

        # rounded_scores = [self.rounding(score_list) for score_list in num_scorecards]
        # for rounding, if I get 1.325 this is equally close to 1.25 and to 1.5, which one should I chose? (round(a.5)=a so it  would go to the lower)

    # check whether rounding each step or rounding the final result makes a difference in example 2
    def cut(self, score_list):
        return score_list[1:-1] if len(score_list) > 2 else score_list

    def mean(self, score_list, default):
        return sum(score_list) / len(score_list) if score_list else default

    #TEST SOME MORE CASES, EMPTY THINGS, NOT 0.25 AND SO ON
    # probably won't need it
    #def rounding(self, score_list):
        # check this function
     #   rounded_list = []
      #  for x in score_list:
       #     y = round(100 * x)  # python rounds 5 down
        #    q = y // 25
         ##   rounded = q * 25 / 100 if abs(q * 25 - x) < abs((q + 1) * 25) else (q + 1) * 25 / 100
           # rounded_list.append(rounded)
        # return rounded_list
#