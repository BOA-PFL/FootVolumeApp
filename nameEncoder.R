rm(list=ls())

library(tidyverse)

dat <- read.csv('C:/Users/daniel.feeney/Boa Technology Inc/PFL Team - General/BigData2021/FootScan Data/MasterSubjectSizes_Male.csv')
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

dat$codedNames <- intOrExt

