# Certificate-Generator
This is a simple certificate generator using python, which uses small libraries like PIL, pandas and OS. The certificate generator is capable to generate as many certificates with just a simple limitation of only texts. Which means the generator can handle entities like Names, ID's, College/School names, etc. 

For now the code is such a way that it can change only names from certificates. Changes should me made which are pretty easy to add up texts inside the certificate. Also the images generated have the names of the people in certificate so its easy to identify.

#Things to remember
1. The data should be clean - this is not a complete automated process. [The excel sheet which will be used as a source to generate names in certificates].
2. The NAME_POSITION_Y = 580, line of code marks the template's location where the name should be present. It varies according to each template of user.
3. Same way as mentioned earlier if many entities to be generated in certificate...the logic follows, variables need to be created, assigned and then to be used for marking positions in the certificate. 
4. Marking positions is a trial and error process.
5. IMPORTANT NOTE: Dependent columns in excel / any form of data should be cleaned and verified carefully.