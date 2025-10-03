# this week u will learn what a system of linear equation is and saome of its reporestnations
# one of them is the set of lines in the plane and another one is the an array of numbers called matrix
# for theremore  you will learn what singular and nonsingular systems are, why is this so important in linear algebra?

# linear algebra has many applications in many filed of science and technology and machine learning is certainly not the exception

# infact it is a stretch to say that linear algebara is the most useful math field in the machine learning 

# some best application of linear algebra in machine learning 
# most popluar is linear regression


# main topic is systems of linear equation
# a common machine learning approach to modeling systems is called linear regression
# linear regression is supervised machine learning approach, which means u have already collected data on many inputs and outputs and u goo to this to disvcover the relationships between them
# for example supposre you want to predict the electrical power outpiut from a wind turbine if u had just one feature like in this case wind speed showns herew on the x axis which is the horizental axis and u plot ur target which is the horizetnal x and u plot ur taeget of power outpuit on the y axis wwhich is the veritcal x axis then the data points here are representating real measurements of wind speed and power output
# clearly there is a paattertn and the goal of lineasr regression would be fo;und the line of best fit for the data 
# for example this one  with a model like this you re making the assumption that this relationship is literally lkinear that it can be modeled by a line

# in other words that if you know the wind speed uo can mulitiply it by a constant at a scecond constant
# and make a reasonable estimate of the power outpuit from the wind turbione

# for example with this model i can say that iof the wind is blowing at five meters per sewcond then i predict the power output from the wind turbine is going to be 1500 kilowatts

# now this model is not perfect
# you can see the actual data scattered about the line representing the model but its doing resonable job

# the model here is the familier linear equation y = mx + b
# where y is thje power output
# x is the wind speed 
# your goal is to find the best values for m and b that fit the data
# 

# in machine learning you will ofthen see the equation of this model written as y = wx + b
#beacasue the number multipled by x is called a weight  the b is called the bias

# so so lluckly  doesnt need to change now linear regressioin jsut one feature like this it is easy to visualize but in many machine learning problems, you will be considering more features. in the case of predicting power output from a wind turbine you may want to include not only wind speed
# but temperature as well

# in order to account for the new input the equation of ur line would need to change
# now y = w_1 times wind speed plus w_2 times temperatire plus b with a new weight added for the second input variable

# if u graph  this equation  it no longer would form a line

# instead it would graphed  as a plane in three dimewnsional space

# but what if u wnated to considfer more feature like pressure
# humidity or anything else that might affect the performance of the wind turbine>?


# the idea is exaclty the same as with one or two features u simply add a new weight for each new feature even as the equatrion  of this model gets longer conceptually it works as same by fiunding  the right value for the weight and the baised terms it should be possible to make accurate prediction of the output or target under the ASSUmption that this is linear the relationship

# if we write that out eplictiy 
# then you have 
'

# this is very fujndatemtal topic cale