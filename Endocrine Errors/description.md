# Challenge description


The invention of dialysis, the process where waste blood is filtered and then returned to the body, has significantly improved the outcomes for patients who have kidney diseases. You are writing a piece of software which is part of the next generation of dialysis, which can respond in real time to hormonal levels in the blood. This would allow dialysis to mimic the endocrine system (the system which manages hormonal levels in the blood) and so help people with thyroidal and other endocrine conditions.

You will be given a list of decimals, which represent the blood concentration of a hormone in parts per million (ppm) every second. Your system should record an error for a datapoint if ANY of the following occur:

* The value is >= the threshold limit,
* The recorded value is negative and should be treated as 0 for any other purpose,
* The value is increasing at a rate which would cross the threshold in $\leq$ 0.5 seconds,
* The data is decreasing at a rate which would go < zero in  $\leq$ 0.5 seconds,

unless the concentration is already above the threshold. Also don't count decreasing errors when the concentration is already negative. Return the number of errors recorded across the dataset. (The threshold will be >0)!
