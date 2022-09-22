rm(list=ls())

library(tidyverse)

dat <- read.csv('C:/Users/bethany.kilpatrick/Boa Technology Inc/PFL - General/BigData/FootScan Data/MasterSubjectSizes_Female.csv') 

dat$TypeofTester <- as.factor(dat$TypeofTester)

num_list <- sample(1:1000, 500)

intOrExt <- vector()
for (row in 1:dim(dat)[1]){
    if (dat[row,2] == 'External'){
      
      intOrExt[row] <- num_list[row]
    }
    else {
      intOrExt[row] <- dat$Subject[row]
    }
} 
 

# 



# 
EU_Size <- c(dat$ShoeSize +33) #Male EU size conversion
dat$EU_Size <- c(dat$ShoeSize +33) 



EU_Size <- c(dat$ShoeSize +31)  # Female EU size conversion
dat$EU_Size <- c(dat$ShoeSize +31)



dat$codedNames <- intOrExt 
 


write.csv(dat,"C:\\Users\\bethany.kilpatrick\\OneDrive - Boa Technology Inc\\Documents\\MasterSubjectSizes_Female_CodedKey.csv" , all(T) ) 

