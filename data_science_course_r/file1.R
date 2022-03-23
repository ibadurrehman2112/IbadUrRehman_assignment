# packages
#install.packages("readxl")
library(readxl)
r_data_file <- read_excel("r_data_file.xlsx", 
                          sheet = "data02", range = "A2:C11", col_types = c("text", 
                                                                            "numeric", "numeric"))
summary(r_data_file)
mean(r_data_file)
plot(r_data_file$Height ~ r_data_file$Weight)
hist(r_data_file$Height)



